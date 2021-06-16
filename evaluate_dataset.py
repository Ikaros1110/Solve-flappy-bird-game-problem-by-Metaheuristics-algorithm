from flappy import mainFlappy
def write_to_file(fileName, message, openMode = 'a'):
    f = open(fileName, openMode)
    f.write(message)
    f.close()

def evaluate_dataset():
    version = 'Ver3_'
    datasetType = 'GA'
    times = 100 # evalutimes
    groupSizeList = [200, 500] #, 1000
    generateTimesList = [50, 100] #
    allGATimes = 10
    writeFileName = 'result/'+version +'_' + datasetType +'_'+ 'evaluate_dataset.txt'
    for groupSize in groupSizeList:
        for generateTimes in generateTimesList:
            resultList = []
            for GATimes in range(allGATimes):
                readFileName = 'result/'+version + datasetType + '_' +str(groupSize)+'_'+str(generateTimes)+ '_' + str(GATimes) +'.txt'
                avg_result = mainFlappy(readFileName, times)
                resultList.append(avg_result)
                storeMessage = 'GA' + 'size: ' + str(groupSize) + ',times: ' + str(generateTimes)+',Number: ' + str(GATimes) + ',result =  ' + str(avg_result) +'\n'
                write_to_file(writeFileName, storeMessage)
            storeMessage = 'GA' + 'size: ' + str(groupSize) + ',times: ' + str(generateTimes) +', all result average = ' + str(sum(resultList)/len(resultList)) +'\n\n'
            write_to_file(writeFileName, storeMessage)
evaluate_dataset()