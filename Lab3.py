"""
 Name: Beck Faubion
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: 20xx
 Instructor: Dr. Cao
 Date: 10/12/2023
 Sources consulted: any books, individuals, etc consulted

 Known Bugs: description of known bugs and other program imperfections

 Creativity: anything extra that you added to the lab

 Instructions: instructions to user on how to execute your program

"""
import csv
import random
import sys
import argparse
import math

def splitData(data, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """
    splitIndex = int(len(data) * ratio)

    trainData = data[:splitIndex]
    testData = data[splitIndex:]

    return trainData, testData
    

def splitDataRandom(data,ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    random.shuffle(data)
  
    
    splitIndex = int(len(data) * ratio)

    trainData = data[:splitIndex]
    testData = data[splitIndex:]

    return trainData, testData


def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """
    if mode == "R":
        """
        Random splitting
        """
        ratio = 0.7
        [trainOutFile, testOutFile] = options.output
        inputFile = options.input
        data = readFile(inputFile)
        trainData, testData = splitDataRandom(data, ratio)
        writeFile(trainOutFile, testOutFile, trainData,testData)
        
    if mode == "N":
        """
        Normal splitting
        """
        ratio = 0.7
        [trainOutFile, testOutFile] = options.output
        inputFile = options.input
        data = readFile(inputFile)
        trainData, testData = splitData(data, ratio)
        writeFile(trainOutFile, testOutFile, trainData,testData)
        

def readFile(filePath):
    data = []
    with open(filePath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def writeFile(trainFilePath,testFilePath, trainData, testData):
        with open(trainFilePath, 'w', newline='') as train_csvfile:
                fieldnames = trainData[0].keys() 
                train_writer = csv.DictWriter(train_csvfile, fieldnames=fieldnames)
                train_writer.writeheader()
                for row in trainData:
                        train_writer.writerow(row)

        with open(testFilePath, 'w', newline='') as test_csvfile:
                fieldnames = testData[0].keys() 
                test_writer = csv.DictWriter(test_csvfile, fieldnames=fieldnames)
                test_writer.writeheader()
                for row in testData:
                        test_writer.writerow(row)

def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    print("Please provide input argument. Here are examples:")
    print("python " + sys.argv[0] + " --mode N --input DATA/epidemiology.csv --output TrainingData.txt TestData.txt")
    print("python " + sys.argv[0] + " --mode R --input DATA/epidemiology.csv --output TrainingDataRandom.txt TestDataRandom.txt") 
    sys.exit(0)


if __name__ == "__main__":
        #------------------------arguments------------------------------#
        #Shows help to the users                                        #
        #---------------------------------------------------------------#
        parser = argparse.ArgumentParser()
        parser._optionals.title = "Arguments"
        parser.add_argument('--mode', dest='mode',
                                default='',  # default empty!
                                help='Mode: R for random splitting, and N for normal splitting')
        parser.add_argument('--input', dest='input',
                                default='',  # default empty! 
                                )
        parser.add_argument('--output', nargs=2, dest='output',
                                default='',  # default empty!
                                )
        parser.add_argument('--modelPath', dest='modelPath',
                                default='',  # default empty!
                                help='The path of the machine learning model ')
        parser.add_argument('--trueLabel', dest='trueLabel',
                                default='',  # default empty!
                                help='The path of the correct label ')
        options = parser.parse_args()
        if not options.mode or not options.input or not options.output:
                showHelper()
        main()
