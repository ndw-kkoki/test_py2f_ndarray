import numpy as np
from ctypes import *

# Fortran サブルーチンの読み込み（引数、返値の型指定）
fmath = np.ctypeslib.load_library("fmath.so",".")
fmath.add_one.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64),
    np.ctypeslib.ndpointer(dtype=np.float64),
    POINTER(c_int64) ]
fmath.add_one.restype = c_void_p

# 引数、返値の作成
inArray = np.arange(0.,10.,dtype=np.float64)
outArray = np.empty_like(inArray)
size = byref(c_int64(inArray.size))

# サブルーチンの呼び出し
fmath.add_one(inArray, outArray, size)

# 結果の出力
print (inArray) # 0,1,2,..,9
print (outArray) # 1,2,3,..,10