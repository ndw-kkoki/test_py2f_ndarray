import numpy as np
import pandas as pd
from ctypes import *

# Fortran サブルーチンの読み込み（引数、返値の型指定）
fmath = np.ctypeslib.load_library("fmath_pandas.so",".")
fmath.add_one.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64),
    np.ctypeslib.ndpointer(dtype=np.float64),
    POINTER(c_int64),
    POINTER(c_int64)]
fmath.add_one.restype = c_void_p

# 引数、返値の作成
calc_data = pd.read_excel("calc_data.xlsx", dtype=np.float64).values
outArray = np.empty_like(calc_data)
M = byref(c_int64(calc_data.shape[0]))
N = byref(c_int64(calc_data.shape[1]))

# サブルーチンの呼び出し
fmath.add_one(calc_data, outArray, M, N)

# 結果の出力
print (calc_data)       # 元データ
print (outArray)        # Fortran 計算後のデータ