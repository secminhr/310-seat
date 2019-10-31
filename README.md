# 210-seat

## Overview
一個抽籤選座位程式。先生成一張隨機座位表，再根據所有人輸入的需求進行移動，以達到較為公平的結果。

## Environment
 * Node.js with mongodb installed
 * Python 3.X
 
## Run
 ```bash
cd web
npm install
npm start
```

### Export
`node export.js`

### Run requirements
```bash
cd ../cli
python seats.py run
```
Result will be saved in `seats.txt`.

### Current shifting methods
In the following examples, we show how the code move the number 4 to index `1`.

```
inst:
inserts the number into the index
[1,2,3,4,5,6] -> [1,4,2,3,5,6]
```
```
push:
rotates the whole list
[1,2,3,4,5,6] -> [3,4,5,6,1,2]
```
```
swap: 
switches places of the number and the target
[1,2,3,4,5,6] -> [1,4,3,2,5,6]
```

### Create shifting methods
Currently, the default method to switch the seats is `inst`, and it can be changed at `cli/seat.py`.
To add/remove/modify the methods, please take a look at `cli/method.py`
