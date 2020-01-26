import os.path
import re

Item = "\\item[]"

def BankKeyword(Value, File):
    List = open(os.getcwd() + "/Lists/Bank.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Value == Line[1]):
            File.write(Line[0] + " ")
            return

    File.write(Value + " ")
    return
# ------------------------------------------------
def CallKeyword(Value, Offset, File, CallList, Name):
    Calls = open(os.getcwd() + "/Lists/Calls.txt", "r")

    for Line in Calls:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Value == Line[1]):
            File.write(Line[0] + " ")
            return CallList

    if(Offset not in CallList):
        CallList.append(Offset)
        CallList.sort()

    NewFile.write(Value + Name.replace(" ","") + "+ROM ")
    return CallList
# ------------------------------------------------
def TempKeyword(Value, File):
    List = open(os.getcwd() + "/Lists/Temp.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Value == Line[1]):
            File.write(Line[0].replace("\\","") + " ")
            return

    File.write(Value + " ")
    return
# ------------------------------------------------

def TaskKeyword(Value, File):
    List = open(os.getcwd() + "/Lists/Task.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Value == Line[1]):
            File.write(Line[0].replace("\\","") + " ")
            return
        
    File.write(Value + " ")
    return
# ------------------------------------------------

def BGKeyword(Value, File):
    List = open(os.getcwd() + "/Lists/BG.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Value == Line[1]):
            File.write(Line[0] + " ")
            return

    File.write(Value + " ")
    return
# ------------------------------------------------

def SongKeyword(Value, File):
    List = open(os.getcwd() + "/Lists/Song.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Value == Line[1]):
            File.write(Line[0] + " ")
            return

    File.write(Value + " ")
    return
# ------------------------------------------------

def CreateHeader(Name, File):
    List = open(os.getcwd() + "/Lists/Moves.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Name == Line[0]):
            NewFile.write("------------------------------------------ \n")
            File.write(Name + ": " + Line[1] + " " + Line[2] + "\n")
            NewFile.write("------------------------------------------ \n")
            return

    NewFile.write("------------------------------------------ \n")
    File.write(Name + ": \n")
    NewFile.write("------------------------------------------ \n")
# ------------------------------------------------

def Decompile(FileName, NewFile, Name):

    for Line in FileName:
        Line = Line.strip()
        Line = Line.split()

        Set = 0

        if(len(Line) == 0):
            continue

        Branch = 0
        CallList = []

        for i in range(len(Line)):
            
            if Set > 0:
                Set -= 1
                continue
            
            if(Line[i] == "00"):  #   LoadParticle
                NewFile.write("LoadParticle ")
                NewFile.write("0x")
                NewFile.write(Line[i+2])
                NewFile.write(Line[i+1])
                NewFile.write("\n")
                Set = 2
                
            elif(Line[i] == "01"):  #   UnloadParticle
                NewFile.write("UnloadParticle ")
                NewFile.write("")
                NewFile.write(Line[i+2])
                NewFile.write(Line[i+1])
                NewFile.write("\n")
                Set = 2
                
            elif(Line[i] == "02"):  #   LaunchTemplate
                NewFile.write("LaunchTemplate ")
                X = Line[i+4] + Line[i+3] + Line[i+2] + Line[i+1]
                TempKeyword(X, NewFile)
                NewFile.write("0x" + Line[i+5] + " ")
                NewFile.write("0x" + Line[i+6] + " ")
                NewFile.write("\n")

                Length = int(Line[i+6], 16)
                for j in range(Length):
                    NewFile.write(".hword 0x")
                    NewFile.write(Line[i+8+(j+j)])
                    NewFile.write(Line[i+7+(j+j)] + " ")
                    NewFile.write("\n")
                
                Set = 6 + Length*2
                    
            elif(Line[i] == "03"):  #   LaunchTask
                NewFile.write("LaunchTask ")
                X = Line[i+4] + Line[i+3] + Line[i+2] + Line[i+1]
                TaskKeyword(X, NewFile)
                NewFile.write("0x" + Line[i+5] + " ")
                NewFile.write("0x" + Line[i+6] + " ")
                NewFile.write("\n")

                Length = int(Line[i+6], 16)
                for j in range(Length):
                    NewFile.write(".hword 0x")
                    NewFile.write(Line[i+8+(j+j)])
                    NewFile.write(Line[i+7+(j+j)] + " ")
                    NewFile.write("\n")
                
                Set = 6 + Length*2

            elif(Line[i] == "04"):  #   Pause
                NewFile.write("Pause ")
                NewFile.write("0x" + Line[i+1])
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "05"):  #   WaitAnimation
                NewFile.write("WaitAnimation ")
                NewFile.write("\n")

            elif(Line[i] == "06"):  #   Cmd6
                NewFile.write("Cmd6 ")
                NewFile.write("\n")

            elif(Line[i] == "07"):  #   Cmd6
                NewFile.write("Cmd7 ")
                NewFile.write("\n") 
                
            elif(Line[i] == "08"):  #   End
                NewFile.write("End ")
                NewFile.write("\n")
                NewFile.write("------------------------------------------")
                NewFile.write("\n")
                if(len(Line[i:i+2]) > 1):
                    NewFile.write(Name.replace(" ","") + str(Branch) + ": \n")
                    Branch += 1

            elif(Line[i] == "09"):  #   PlaySound1
                NewFile.write("PlaySound1 ")
                NewFile.write("0x")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 2

            elif(Line[i] == "0A"):  #   MoveSpriteToBG
                NewFile.write("MoveSpriteToBG ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "0B"):  #   MoveSpriteFromBG
                NewFile.write("MoveSpriteFromBG ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "0C"):  #   SetBlends
                NewFile.write("SetBlends ")
                NewFile.write("0x")
                NewFile.write(Line[i+2])
                NewFile.write(Line[i+1])
                NewFile.write("\n")
                Set = 2
                
            elif(Line[i] == "0D"):  #   ResetBlends
                NewFile.write("ResetBlends ")
                NewFile.write("\n")

            elif(Line[i] == "0E"):  #   Call
                NewFile.write("Call ")
                Value = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                NewFile.write("\n")
                Set = 4

            elif(Line[i] == "0F"):  #   Return
                NewFile.write("Return ")
                NewFile.write("\n")
                NewFile.write("------------------------------------------")
                NewFile.write("\n")
                if(len(Line[i:i+2]) > 1):
                    NewFile.write(Name.replace(" ","") + str(Branch) + ": \n")
                    Branch += 1

            elif(Line[i] == "10"):  #   SetArgument
                NewFile.write("SetArgument ")
                NewFile.write("0x")
                NewFile.write(Line[i+1] + " ")
                NewFile.write("0x")
                NewFile.write(Line[i+3])
                NewFile.write(Line[i+2])
                NewFile.write("\n")
                Set = 3

            elif(Line[i] == "11"):  #   ChooseTwoTurnAnimation
                NewFile.write("ChooseTwoTurnAnimation ")
                Value = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                    
                Value = Line[i+8]+Line[i+7]+Line[i+6]+Line[i+5]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                NewFile.write("\n")
                NewFile.write("------------------------------------------")
                NewFile.write("\n")
                NewFile.write(Name.replace(" ","") + str(Branch) + ": \n")
                NewFile.write("\n")
                Branch += 1
                    
                Set = 8
                
            elif(Line[i] == "12"):  #   JumpIfMoveTurnEquals
                NewFile.write("JumpIfMoveTurnEquals ")
                NewFile.write("0x")
                NewFile.write(Line[i+1] + " ")

                Value = Line[i+5]+Line[i+4]+Line[i+3]+Line[i+2]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                NewFile.write("\n")
                Set = 5

            elif(Line[i] == "13"):  #   Jump
                NewFile.write("Jump ")
                Value = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                NewFile.write("\n")
                NewFile.write("------------------------------------------")
                NewFile.write("\n")
                
                if(len(Line[i+4:i+6]) > 1):
                    NewFile.write(Name.replace(" ","") + str(Branch) + ": \n")
                    Branch += 1

                Set = 4

            elif(Line[i] == "14"):  #   LoadBG1
                NewFile.write("LoadBG1 ")
                BGKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1
                
            elif(Line[i] == "15"):  #   LoadDefaultBG
                NewFile.write("LoadDefaultBG ")
                NewFile.write("\n")

            elif(Line[i] == "16"):  #   WaitForBG
                NewFile.write("WaitForBG ")
                NewFile.write("\n")

            elif(Line[i] == "17"):  #   WaitForTransparentBG
                NewFile.write("WaitForTransparentBG ")
                NewFile.write("\n")

            elif(Line[i] == "18"):  #   LoadBG2
                NewFile.write("LoadBG2 ")
                BGKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "19"):  #   PlaySound2
                NewFile.write("PlaySound2 ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("0x" + Line[i+3])
                NewFile.write("\n")
                Set = 3

            elif(Line[i] == "1A"):  #   PanControl
                NewFile.write("PanControl ")
                NewFile.write("0x" + Line[i+1])
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "1B"):  #   PlaySoundPanChange
                NewFile.write("PlaySoundPanChange ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("0x" + Line[i+3] + " ")
                NewFile.write("0x" + Line[i+4] + " ")
                NewFile.write("0x" + Line[i+5] + " ")
                NewFile.write("0x" + Line[i+6] + " ")
                NewFile.write("\n")
                Set = 6

            elif(Line[i] == "1C"):  #   AdvancedPlaySound
                NewFile.write("AdvancedPlaySound ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("0x" + Line[i+3] + " ")
                NewFile.write("0x" + Line[i+4] + " ")
                NewFile.write("0x" + Line[i+5] + " ")
                NewFile.write("\n")
                Set = 5

            elif(Line[i] == "1D"):  #   PlaySound3
                NewFile.write("PlaySound3 ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("0x" + Line[i+3] + " ")
                NewFile.write("0x" + Line[i+4] + " ")
                NewFile.write("\n")
                Set = 4

            elif(Line[i] == "1E"):  #   SetBlendCount
                NewFile.write("SetBlendCount ")
                NewFile.write("0x")
                NewFile.write(Line[i+2])
                NewFile.write(Line[i+1] + "\n")
                NewFile.write("\n")
                Set = 2

            elif(Line[i] == "1F"):  #   LaunchSoundTask
                NewFile.write("LaunchSoundTask ")
                X = Line[i+4] + Line[i+3] + Line[i+2] + Line[i+1]
                TaskKeyword(X, NewFile)
                NewFile.write("0x" + Line[i+5] + " ")
                NewFile.write("\n")

                Length = int(Line[i+5], 16)
                for j in range(Length):
                    NewFile.write(".hword 0x")
                    NewFile.write(Line[i+7+(j+j)])
                    NewFile.write(Line[i+6+(j+j)] + " ")
                    NewFile.write("\n")
                
                Set = 5 + Length*2
                
            elif(Line[i] == "20"):  #   WaitForSound
                NewFile.write("WaitForSound ")
                NewFile.write("\n")

            elif(Line[i] == "21"):  #   JumpIfArgumentEquals
                NewFile.write("JumpIfArgumentEquals ")
                NewFile.write("0x")
                NewFile.write(Line[i+1] + " ")
                NewFile.write("0x")
                NewFile.write(Line[i+3])
                NewFile.write(Line[i+2] + " ")
                Value = Line[i+7]+Line[i+6]+Line[i+5]+Line[i+4]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                NewFile.write("\n")
                Set = 7

            elif(Line[i] == "22"):  #   Cmd22
                NewFile.write("Cmd22 ")
                NewFile.write("0x" + Line[i+1])
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "23"):  #   Cmd23
                NewFile.write("Cmd23 ")
                NewFile.write("0x" + Line[i+1])
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "24"):  #   JumpIfContest
                NewFile.write("JumpIfContest ")

                Value = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                NewFile.write("\n")
                NewFile.write("------------------------------------------")
                NewFile.write("\n")
                Set = 4

            elif(Line[i] == "25"):  #   ChooseBG
                NewFile.write("ChooseBG ")
                BGKeyword(Line[i+1], NewFile)
                BGKeyword(Line[i+2], NewFile)
                BGKeyword(Line[i+3], NewFile)
                NewFile.write("\n")
                Set = 3

            elif(Line[i] == "26"):  #   PlaySoundPanChange2
                NewFile.write("PlaySoundPanChange2")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("0x" + Line[i+3] + " ")
                NewFile.write("0x" + Line[i+4] + " ")
                NewFile.write("0x" + Line[i+5] + " ")
                NewFile.write("0x" + Line[i+6] + " ")
                NewFile.write("\n")
                Set = 6

            elif(Line[i] == "27"):  #   PlaySoundPanChange3
                NewFile.write("PlaySoundPanChange3 ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("0x" + Line[i+3] + " ")
                NewFile.write("0x" + Line[i+4] + " ")
                NewFile.write("0x" + Line[i+5] + " ")
                NewFile.write("0x" + Line[i+6] + " ")
                NewFile.write("\n")
                Set = 6

            elif(Line[i] == "28"):  #   LeftOverPartner
                NewFile.write("LeftOverPartner ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "29"):  #   BankOverPartner
                NewFile.write("BankOverPartner ")
                NewFile.write("\n")

            elif(Line[i] == "2A"):  #   LeftFoeOverPartner
                NewFile.write("LeftFoeOverPartner ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "2B"):  #   MakeInvisible
                NewFile.write("MakeInvisible ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "2C"):  #   MakeVisible
                NewFile.write("MakeVisible ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "2D"):  #   Cmd2D
                NewFile.write("Cmd2D ")
                NewFile.write("\n")

            elif(Line[i] == "2E"):  #   Cmd2E
                NewFile.write("Cmd2D ")
                NewFile.write("\n")

            elif(Line[i] == "2F"):  #   StopMusic
                NewFile.write("StopMusic ")
                NewFile.write("\n")
            else:
                NewFile.write("UNKNOWN COMMAND")
                NewFile.write("\n")

    return CallList, Branch, 
# ------------------------------------------------
def ReplaceCallThing(List, FileName, MoveName):

    with open(FileName, 'r') as file:
        FileData = file.read()

    for i in range(len(List)):
        FileData = FileData.replace(List[i]+"+ROM ", MoveName+str(i)+"+ROM ")

    with open(FileName, 'w') as file:
        file.write(FileData)
# ------------------------------------------------
Continue = 0

while(Continue != "1"):
    Set = 0

    while(Set == 0):
        print("Enter the name of a .txt file: ")
        OldName = input("Enter 'doall' to do all files in the input folder. ")
        print(" ")

        if(OldName == "doall"):
            Set = 1

        else:   
            try:
                DataFile = open(os.getcwd() + "/Input/" + OldName + ".txt", "r")
            except:
                print("File not found.")
                print(" ")
            else:
                Set = 1

    if(OldName == "doall"):
        AllOne = int(input("Put output all in one file? Press 1 for yes. "))
        Set2 = 0
        
        X = -1
        FileNameList = []
        MasterList = []
        
        for FileName in os.listdir(os.getcwd() + "/Input/"):
            if FileName.endswith(".txt"):
                FileNameList.append(FileName[:-4])
                
                DataFile = open(os.getcwd() + "/Input/"+ FileName, "r")

                if(AllOne == 1 and Set2 == 0):
                    NewFile = open(os.getcwd() + "/Output/Plain/MegaFile.txt", "w")
                    Set2 = 1
                    
                elif(AllOne != 1):
                    X += 1
                    NewFile = open(os.getcwd() + "/Output/Plain/" + str(X) + ".txt", "w")

                print("Now starting: %s" % FileName)
                print(" ")

                MoveName = FileName[:-4]
                
                CreateHeader(MoveName, NewFile)
                
                [List, Branches] = Decompile(DataFile, NewFile, MoveName)
                MasterList.append(List)

                NewFile.write("\n")

                if(AllOne != 1):
                    PutInPresets(NewFile)
                    NewFile.close()
                    
                    NewFile = open(os.getcwd() + "/Output/Plain/" + str(X) + ".txt", "r+")


                    
                    ReplaceCallThing(List, os.getcwd() + "/Output/Plain/" + str(X) + ".txt", MoveName.replace(" ",""))
                    
        if(AllOne == 1):
            NewFile.close()

            NewFile = open(os.getcwd() + "/Output/Plain/MegaFile.txt", "r+")
            i = -1
            for Element in FileNameList:
                i += 1
                ReplaceCallThing(MasterList[i], os.getcwd() + "/Output/Plain/MegaFile.txt", Element.replace(" ",""))
            
    else:
        Set = 0
        
        while(Set == 0):
            NewName = input("Enter the name of the file to create: ")
            print(" ")
            if(os.path.isfile(os.getcwd() + "/Output/Plain/" + NewName + ".txt") == True):
                Overwrite = int(input(("File already exists. Press 1 to overwrite. ")))
                if(Overwrite == 1):
                    Set = 1
            else:
                Set = 1

        NewFile = open(os.getcwd() + "/Output/Plain/" + NewName + ".txt", "w")

        CreateHeader(OldName, NewFile)

        [List, Branches] = Decompile(DataFile, NewFile, OldName)

        NewFile.close()

        NewFile = open(os.getcwd() + "/Output/Plain/" + NewName + ".txt", "r+")
        
        ReplaceCallThing(List, os.getcwd() + "/Output/Plain/" + NewName + ".txt", OldName.replace(" ",""))

    Continue = input("Again? Press 1 to quit. ")

print("Goodbye!")
