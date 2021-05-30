# Solve flappy-bird-game problem, by Metaheuristics algorithm

## mutation.py
用 Sigmoid 對 random(-1,1) 做模擬常態分布位置，以原始點作為中央比例擾動

## mating.py
實作方式為 Tournament Selection
即隨機取兩筆資料比較大小，較大的選擇，做兩次後提出一對pair，回傳值為n對pair組成的python list，n為data筆數

## evaluation.py
Not implements

## Use
實作皆為"\__call\__"function

## Test
可使用 class.test()來檢查資料集是否可以正常運作
