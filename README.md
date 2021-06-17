# Solve flappy-bird-game problem, by Metaheuristics algorithm

## mutation.py
輸入:
```python
  data: python list
  upperBound: python list
```
輸出:
```python
  python list
```
給予資料與他們的上限值
用 Sigmoid 對 random(-1,1) 做模擬常態分布位置，以原始點作為中央比例擾動

## mating.py
輸入:
```python
  data: python list
  score: python list
```
輸出:
```python
  python list
```
給予資料與他們的得分
實作方式為 Tournament Selection
即隨機取兩筆資料比較大小，較小的選擇，做兩次後提出一對pair，回傳值為n對pair組成的python list，n為data筆數

## evaluation.py
輸入:
```python
  data: python list
```
輸出:
```python
  float
```
給予資料，算出得分
有兩個class, evaluation跟miniGame
miniGame為模擬遊戲狀態並取得環境值, 不開放使用

> Class evaluation
evaluation以死亡點到下水管左上角的點距離為分數，越近則分數越小(越好)

## Use
實作皆為"\__call\__"function

## Test
可使用 class.test()來檢查資料集是否可以正常運作
