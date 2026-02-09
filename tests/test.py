import neuralRaven

def main():
    fileName = '../data-test/configurationData'
    fileName2 = '../data-test/trainingData'
    inp = neuralRaven.IO()
    print(inp.fromFiles(fileName, fileName2))
    print(inp.fromData(200,100,3000,0.0102,0.0125,[2,2,1], [0.0,0.0,1.0,0.0,1.0,1.0],[0.0,1.0,1.0,0.0]))


if __name__ == "__main__":
    main()