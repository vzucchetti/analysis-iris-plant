# --------------------------------------------------------------------------------------------------------------------------------------------
# IRIS PROJECT
# --------------------------------------------------------------------------------------------------------------------------------------------
# Write a Python program to process the file available with data from the Iris plant.
# Create a new file with a sample of the original one. The sample must have 30% of the original data.
# From this sample, calculate and write:
# 1) distribution of samples by class (Iris species)
# 2) indicate the class (Iris species) with most number of samples
# 3) show the data by class (Iris species), using a bar plot
# 4) for each numeric attribute, determine the minimum value, the maximum value, mean, and standart deviation
# --------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import random
import math


# --------------------------------------------------------------------------------------------------------------------------------------------
# Reading the file
# --------------------------------------------------------------------------------------------------------------------------------------------
def readFile(name):
    file = open(name)
    data = []
    for row in file:
        row1 = row[:-1]  # removing the last character (\n) from the row
        data.append(row1)
    file.close()
    return data


# --------------------------------------------------------------------------------------------------------------------------------------------
# Write data of a list
# --------------------------------------------------------------------------------------------------------------------------------------------
def writeList(list):
    for item in list:
        print(item)


# --------------------------------------------------------------------------------------------------------------------------------------------
# Excluding the header
# --------------------------------------------------------------------------------------------------------------------------------------------
def makeListWithoutHeader(list):
    new = []
    ind = 1
    while ind < len(list):
        new.append(list[ind])
        ind = ind + 1
    return new


# --------------------------------------------------------------------------------------------------------------------------------------------
# Mixing the data
# --------------------------------------------------------------------------------------------------------------------------------------------
def mixing(list, amount):
    while amount > 0:
        amount = amount - 1
        # Take two index of the list randomly, and mix them
        ind1 = random.randint(0, len(list) - 1)
        ind2 = random.randint(0, len(list) - 1)
        aux = list[ind1]
        list[ind1] = list[ind2]
        list[ind2] = aux


# --------------------------------------------------------------------------------------------------------------------------------------------
# Generating a sample
# --------------------------------------------------------------------------------------------------------------------------------------------
def sampling(list, index):
    mixing(list, 90)
    writeList(list)
    amount = len(list) * index
    sample = []
    count = 0
    while count < amount:
        sample.append(list[count])
        count = count + 1
    return sample


# --------------------------------------------------------------------------------------------------------------------------------------------
# Recording sample
# --------------------------------------------------------------------------------------------------------------------------------------------
def recordSample(header, sample, name):
    file = open(name, "w")
    file.write(header + "\n")
    for item in sample:
        file.write(item + "\n")
    file.close()


# --------------------------------------------------------------------------------------------------------------------------------------------
# Running the functions to obtain the sample
# --------------------------------------------------------------------------------------------------------------------------------------------
plants = readFile("iris.csv")
writeList(plants)
header = plants[0]
print(header)
plants1 = makeListWithoutHeader(plants)
writeList(plants1)
samples = sampling(plants1, 0.3)
writeList(samples)
recordSample(header, samples, "sample_Iris.txt")


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to count the samples by Iris species in the order ["Iris-virginica","Iris-setosa","Iris-versicolor"]
# --------------------------------------------------------------------------------------------------------------------------------------------
def countSamples(sample, species):
    count0 = 0
    count1 = 0
    count2 = 0
    for item in sample:
        if species[0] in item:
            count0 += 1
        elif species[1] in item:
            count1 += 1
        else:
            count2 += 1
    return [count0, count1, count2]


# --------------------------------------------------------------------------------------------------------------------------------------------
# Reading the file with sampled Iris data
# --------------------------------------------------------------------------------------------------------------------------------------------
samples = readFile("sample_Iris.txt")
writeList(samples)
header = samples[0]
sample1 = makeListWithoutHeader(samples)

# --------------------------------------------------------------------------------------------------------------------------------------------
# Defining the species of Iris and its order on countSamples
# --------------------------------------------------------------------------------------------------------------------------------------------
spp = ["Iris-virginica", "Iris-setosa", "Iris-versicolor"]
amount = countSamples(sample1, spp)


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to generate bar plot
# --------------------------------------------------------------------------------------------------------------------------------------------
def makePlot(spp, amount):
    plt.bar(spp, amount, color="blue")
    plt.title("Distribution of samples by Iris species")
    plt.xlabel("Iris species")
    plt.ylabel("Amount of samples")
    plt.show()


# --------------------------------------------------------------------------------------------------------------------------------------------
# Functions to generate the mean and standart deviation values
# --------------------------------------------------------------------------------------------------------------------------------------------
# Mean
def mean(list):
    sum = 0
    for item in list:
        sum += item
    return sum / len(list)


# SD
def sd(list):
    var = []
    for item in list:
        var.append((item - mean(list)) ** 2)
    return math.sqrt(mean(var))


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to generate expecified values for each one of the numeric attributes
# --------------------------------------------------------------------------------------------------------------------------------------------
def analyzeNumericAttributes(header, data):
    list0 = []
    list1 = []
    list2 = []
    list3 = []
    for item in data:
        columns = item.split(",")
        list0.append(float(columns[1]))
        list1.append(float(columns[2]))
        list2.append(float(columns[3]))
        list3.append(float(columns[4]))
    itens = header.split(",")
    print(
        f"{itens[1]} \t - Minimum: {min(list0)}, Maximum: {max(list0)}, Mean: {mean(list0):.2f}, SD: {sd(list0):.2f}"
    )
    print(
        f"{itens[2]} \t - Minimum: {min(list1)}, Maximum: {max(list1)}, Mean: {mean(list1):.2f}, SD: {sd(list1):.2f}"
    )
    print(
        f"{itens[3]} \t - Minimum: {min(list2)}, Maximum: {max(list2)}, Mean: {mean(list2):.2f}, SD: {sd(list2):.2f}"
    )
    print(
        f"{itens[4]} \t - Minimum: {min(list3)}, Maximum: {max(list3)}, Mean: {mean(list3):.2f}, SD: {sd(list3):.2f}"
    )


# --------------------------------------------------------------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # 1) Distributing the samples of Iris by its species
    # --------------------------------------------------------------------------------------------------------------------------------------------
    ind = 0
    sp = spp[0]
    most = amount[0]
    print("\nResults: \n")
    # Navigating through the list of Iris species and defining the most common in the sample
    while ind < len(spp):
        print(
            spp[ind],
            " - samples: ",
            amount[ind],
            f"({amount[ind]*100/len(sample1):.2f}%)",
        )
        if amount[ind] > most:
            most = amount[ind]
            sp = spp[ind]
        ind = ind + 1
    # Printing the total of samples in the sampled list
    print(f"Total of samples: {len(sample1)}")
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # 2) Showing the specie most commom in the sample
    # --------------------------------------------------------------------------------------------------------------------------------------------
    print(f"\nSpecies with more samples: {sp}\n")
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # 3) Bar plot of samples by species
    # --------------------------------------------------------------------------------------------------------------------------------------------
    makePlot(spp, amount)
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # 4) Minimum, maximum, mean and standart deviation for each numeric atribute of sample
    # --------------------------------------------------------------------------------------------------------------------------------------------
    analyzeNumericAttributes(header, sample1)
