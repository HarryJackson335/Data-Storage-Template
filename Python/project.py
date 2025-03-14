

def InitiateProject():
    print("\nHi, I am HJ. I am a data-storing assistant and I can store whatever data u want me to store.")
    print('Please give a label and a value u want me to store.')
    start()

def start():
    global Label, Value, Data
    Label = input('Label: ')
    Value = input("Value: ")
    Data = {Label: Value}
    choice()

def choice():
    print("""\nPlease choose one of the options
    1. Continue to add more data
    2. View the stored data
    3. Change the stored data
    4. Exit""")
    global Choice 
    Choice = input('Please enter a number: ')
    if Choice == '1':
        continueData()
    elif Choice == '2':
        print(Data)
        choice()
    elif Choice == '3':
        updateData()
    elif Choice == '4':
        exit()
    else:
        print('Invalid Choice')
        choice()
    print('\n')

def continueData():
    global NewLabel, NewValue
    NewLabel = input('New Label: ')
    NewValue = input('New Value: ')
    if NewLabel == Label or NewValue == Value:
        print('Same data, not valid. Please choose another option.')
        choice()
    elif ':' in NewLabel or ':' in NewValue:
        print('Invalid input. Please choose another option.')
        choice()
    else: 
        NewData()
        choice()

def NewData():
    global Data, NewValue, NewLabel, Choice
    Label = NewLabel
    Value = NewValue
    Data.update({Label:Value})

def updateData():
    global NewLabel, NewValue, Label, Value, Data
    print(Data)
    print('Please rewrite the Label and Value you would like to update. For example: in Name: Daiwik ---> Name is the Label and Daiwik is the Value.')
    ProcessedData = input('Data to be updated: ')
    if " " in ProcessedData:
        try:
            ProcessedData.removeprefix(' ').removesuffix(" ").replace(' ', "")
        except:
            if " " in Data:
                pass
    if ":" in ProcessedData:
        ProcessedData = ProcessedData.split(':')
        Label = ProcessedData[0].removeprefix(';').removeprefix(' ').removesuffix(' ').removesuffix(':')
        Value = ProcessedData[1].removeprefix(';').removeprefix(" ").removesuffix(" ").removesuffix(":")
        if Label in Data:
            Data.__delitem__(Label)
            NewLabel = input('New Label: ')
            NewValue = input('New Value: ')
            if ':' in NewLabel or ':' in NewValue:
                print('Invalid input. Please choose another option.')
                choice()
            else:
                NewData()
                choice()
        else:
            print('Invalid input')
            choice()
    else:
        print("Invalid input")
        choice()

def exit():
    print('End of Code')



InitiateProject()