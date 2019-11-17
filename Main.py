# import for prompting user for file
from tkinter.filedialog import askopenfilename

def main():
    print("Select .txt file to Count Speech")
    realFile = askopenfilename()
    print("File Selected: " + realFile)
    resultFilename = input("Enter filename for results. e.g. results.txt" + "\n")
    speechCountDict = {}

    # opens file to read speech
    with open(realFile, 'r') as f:
        for line in f:

            # split line by spaces attempt to parse speech
            try:
                data = line.split(' ')
                _speech = data[2]
            except:
                continue

            # if speech parsed update speech counter dictionary
            if parseSpeech(_speech):
                value = speechCountDict.get(_speech)
                updateDict(value, _speech, speechCountDict)

    # open results file for writing, write dictonary to file
    # can append multiple input file results
    with open(resultFilename, 'a+') as results:
        results.write("Speech Count for file: " + realFile + "\n")
        print(speechCountDict, file = results)
        results.write("\n")

# params: value -in dict, _speech -parsed speech, speechCountDict -current state of dict
# updates speech count dictionary
# if _speech not in dict -> add _speech with value 1 and update speechCountDict
# if _speech in dict -> add 1 to value and update speechCountDict
def updateDict(value, _speech, speechCountDict):
    if value == None:
        _update = {_speech: 1}
        speechCountDict.update(_update)
    else:
        _update = {_speech: value + 1}
        speechCountDict.update(_update)
        
# params: _speech section of line read to be parsed
# parses line for part of speech
# returns true if value is parsable
def parseSpeech(_speech):
    if _speech == '':
        return False
    elif _speech == '.':
        return False
    elif _speech == "\n":
        return False
    elif _speech == ':':
        return False
    elif _speech == ',':
        return False
    else:
        return True

if __name__ == "__main__":
    main()