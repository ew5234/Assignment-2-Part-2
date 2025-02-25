#-------------------------------------------------------------------------
# AUTHOR: Eric Wong
# FILENAME: decision_tree_2.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#Importing some Python libraries
from sklearn import tree
import csv

dataSets = ['C:\\Users\\Munchy\\Downloads\\contact_lens_training_1.csv', 'C:\\Users\\Munchy\\Downloads\\contact_lens_training_2.csv', 'C:\\Users\\Munchy\\Downloads\\contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #Reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #Transform the original categorical training features to numbers and add to the 4D array X.
    #For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    for row in dbTraining:
        temp = [] #temporary value to hold values
        #Age: Young = 1, Prepresbyopic = 2, Presbyopic = 3
        if row[0] == 'Young':
            temp.append(1)
        elif row[0] == 'Prepresbyopic':
            temp.append(2)
        else:
            temp.append(3)

        #Spectacle Prescription: Myope = 1, Hypermetrope = 2
        if row[1] == 'Myope':
            temp.append(1)
        else:
            temp.append(2)

        #Astigmatism: Yes = 1, No = 2
        if row[2] in 'Yes':
            temp.append(1)
        else:
            temp.append(2)

        #Tear Production Rate: Reduced = 1, Normal = 2
        if row[3] == 'Reduced':
            temp.append(1)
        else:
            temp.append(2)
        X.append(temp)

    #Transform the original categorical training classes to numbers and add to the vector Y.
    #For instance Yes = 1 and No = 2, Y = [1, 1, 2, 2, ...]
    temp = []
    for row in dbTraining:
        #Recommended Lenses: Yes = 1, No = 2
        if row[4] == 'Yes':
            temp.append(1)
        else:
            temp.append(2)
    Y = temp

    #Loop your training and test tasks 10 times here
    for i in range (10):
        #Fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=5)
        clf = clf.fit(X, Y)

        dbTest = []
        correct = 0
        #Read the test data and add this data to dbTest
        with open('C:\\Users\\Munchy\\Downloads\\contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTest.append (row)


        for data in dbTest:
            #Transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            temp = [] #temporary value to hold values
            #Age: Young = 1, Prepresbyopic = 2, Presbyopic = 3
            if data[0] == 'Young':
                temp.append(1)
            elif data[0] == 'Prepresbyopic':
                temp.append(2)
            else:
                temp.append(3)

            #Spectacle Prescription: Myope = 1, Hypermetrope = 2
            if data[1] == 'Myope':
                temp.append(1)
            else:
                temp.append(2)

            #Astigmatism: Yes = 1, No = 2
            if data[2] in 'Yes':
                temp.append(1)
            else:
                temp.append(2)
            #Tear Production Rate: Reduced = 1, Normal = 2
            if data[3] == 'Reduced':
                temp.append(1)
            else:
                temp.append(2)
            if data[4] == 'Yes':
                corVal = 1
            else:
                corVal = 2
            
            class_predicted = clf.predict([temp])
            #Compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            if  class_predicted == corVal:
                correct+=1


    #Find the average of this model during the 10 runs (training and test set)
    accuracy = correct/len(dbTest)

    #Print the average accuracy of this model during the 10 runs (training and test set).
    #Your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2

    print(str(ds) + ": ", accuracy)




