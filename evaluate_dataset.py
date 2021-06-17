import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame.key import name
from flappy import mainFlappy
import multiprocessing as mp
def write_to_file(fileName, message, openMode = 'a'):
    f = open(fileName, openMode)
    f.write(message)
    f.close()

def evaluate_GA_dataset(version, groupSize, generateTimes, dataIndex ,playTimes = 10):
    versionStr = 'Ver' +str(version) 
    datasetType = 'GA'
    readFileName = 'result/GA/'+ versionStr + '_' + datasetType + '_' + str(groupSize) + '_'+ str(generateTimes) + '_' + str(dataIndex) +'.txt'
    return mainFlappy(readFileName, playTimes)

def evaluate_RD_dataset(version, dataNum, dataIndex ,playTimes = 10):
    versionStr = 'Ver' +str(version) 
    datasetType = 'randomGenerate'
    readFileName = 'result/RD/'+ versionStr + '_' + datasetType + '_' +str(dataNum)+ '_' + str(dataIndex) +'.txt'
    return mainFlappy(readFileName, playTimes)

def main():
    dataIndexNum = 10
    set_processor_num = min(mp.cpu_count(), dataIndexNum) # parallel processing
    version = 3
    ### run RD ###
    writeRDFileName = 'result/RD_evaluate_dataset.txt'
    for dataNum in [200000]:
        print("In RD ",dataNum)
        args = [[version, dataNum, e] for e in range(dataIndexNum)]
        pool = mp.Pool(set_processor_num)
        resultList = pool.starmap(evaluate_RD_dataset, args)
        print(resultList)
        message = str(dataNum) + '\n'
        message += str(resultList) +'\n'
        message += str(sum(resultList)/len(resultList)) + '\n\n'
        write_to_file(writeRDFileName, message)
    ### run GA ###
    writeGAFileName = 'result/GA_evaluate_dataset.txt'
    for groupSize in [200, 500, 1000]:
        for generateTimes in [50, 100]:
            if groupSize == 200 and generateTimes == 50:
                continue
            print("In GA ", groupSize, generateTimes)
            args = [[version, groupSize, generateTimes, e] for e in range(dataIndexNum)]
            pool = mp.Pool(set_processor_num)
            resultList = pool.starmap(evaluate_GA_dataset, args)
            print(resultList)
            message = str(groupSize) + ' ' + str(generateTimes) + '\n'
            message += str(resultList) +'\n'
            message += str(sum(resultList)/len(resultList)) + '\n\n'
            write_to_file(writeGAFileName, message)
    print("All run OK!")


if __name__ == '__main__':
    main()