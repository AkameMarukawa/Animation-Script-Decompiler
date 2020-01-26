import os.path

def SplitUp(FileName, NewFile):
    
    Preset = open(os.getcwd() + "/Lists/Calls.txt", "r")
    Address = []
    
    for Line in Preset:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Line != []):
            Address.append(Line[1])

    for Line in FileName:
            Line = Line.strip()
            Line = Line.split()

            Set = 0

            CallList = []
            Branch = -1
            Calls = 0
            Presets = 0

            if(len(Line) == 0):
                continue

            for i in range(len(Line)):
                
                if Set > 0:
                    Set -= 1
                    continue
                
                if(Line[i] == "00"):  #   LoadParticle
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write("\n")
                    Set = 2
                    
                elif(Line[i] == "01"):  #   UnloadParticle
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write("\n")
                    Set = 2
                    
                elif(Line[i] == "02"):  #   LaunchTemplate
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write(Line[i+6]+" ")
                    NewFile.write("\n")

                    Length = int(Line[i+6], 16)
                    for j in range(Length):
                        NewFile.write("\t"+Line[i+7+(j+j)]+" ")
                        NewFile.write(Line[i+8+(j+j)]+" ")
                        NewFile.write("\n")
                    
                    Set = 6 + Length*2
                        
                elif(Line[i] == "03"):  #   LaunchTask
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write(Line[i+6]+" ")
                    NewFile.write("\n")

                    Length = int(Line[i+6], 16)
                    for j in range(Length):
                        NewFile.write("\t"+Line[i+7+(j+j)]+" ")
                        NewFile.write(Line[i+8+(j+j)]+" ")
                        NewFile.write("\n")
                    
                    Set = 6 + Length*2

                elif(Line[i] == "04"):  #   Pause
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "05"):  #   WaitAnimation
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "06"):  #   Cmd6
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "07"):  #   Cmd6
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")
                    
                elif(Line[i] == "08"):  #   End
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")
                    NewFile.write("-----------------------------------------")
                    NewFile.write("\n")
                    Branch += 1

                elif(Line[i] == "09"):  #   PlaySound1
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write("\n")
                    Set = 2

                elif(Line[i] == "0A"):  #   MoveSpriteToBG
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "0B"):  #   MoveSpriteFromBG
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "0C"):  #   SetBlends
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write("\n")
                    Set = 2
                    
                elif(Line[i] == "0D"):  #   ResetBlends
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "0E"):  #   Call
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write("\n")
                    Set = 4

                    Offset = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                    if(Offset not in CallList):
                        CallList.append(Offset)
                        Calls += 1
                        
                        if(Offset in Address):
                            Presets += 1
                        

                elif(Line[i] == "0F"):  #   Return
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")
                    NewFile.write("-----------------------------------------")
                    NewFile.write("\n")
                    Branch += 1

                elif(Line[i] == "10"):  #   SetArgument
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write("\n")
                    Set = 3

                elif(Line[i] == "11"):  #   ChooseTwoTurnAnimation
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write(Line[i+6]+" ")
                    NewFile.write(Line[i+7]+" ")
                    NewFile.write(Line[i+8]+" ")
                    NewFile.write("\n")
                    NewFile.write("-----------------------------------------")
                    NewFile.write("\n")
                    Set = 8
                    Branch += 1


                    Offset = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                    if(Offset not in CallList):
                        CallList.append(Offset)
                        Calls += 1
                        if(Offset in Address):
                            Presets += 1

                    Offset = Line[i+8]+Line[i+7]+Line[i+6]+Line[i+5]
                    if(Offset not in CallList):
                        CallList.append(Offset)
                        Calls += 1
                        if(Offset in Address):
                            Presets += 1
                    
                elif(Line[i] == "12"):  #   JumpIfMoveTurnEquals
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write("\n")
                    Set = 5
                    
                    Offset = Line[i+5]+Line[i+4]+Line[i+3]+Line[i+2]
                    if(Offset not in CallList):
                        CallList.append(Offset)
                        Calls += 1
                        if(Offset in Address):
                            Presets += 1

                elif(Line[i] == "13"):  #   Jump
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write("\n")
                    NewFile.write("-----------------------------------------")
                    NewFile.write("\n")
                    Set = 4
                    Branch += 1

                    Offset = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                    if(Offset not in CallList):
                        CallList.append(Offset)
                        Calls += 1
                        if(Offset in Address):
                            Presets += 1

                elif(Line[i] == "14"):  #   LoadBG1
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1
                    
                elif(Line[i] == "15"):  #   LoadDefaultBG
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "16"):  #   WaitForBG
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "17"):  #   WaitForTransparentBG
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "18"):  #   LoadBG2
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "19"):  #   PlaySound2
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write("\n")
                    Set = 3

                elif(Line[i] == "1A"):  #   PanControl
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "1B"):  #   PlaySoundPanChange
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write(Line[i+6]+" ")
                    NewFile.write("\n")
                    Set = 6

                elif(Line[i] == "1C"):  #   AdvancedPlaySound
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write("\n")
                    Set = 5

                elif(Line[i] == "1D"):  #   PlaySound3
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write("\n")
                    NewFile.write("\n")
                    Set = 4

                elif(Line[i] == "1E"):  #   SetBlendCount
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write("\n")
                    Set = 2

                elif(Line[i] == "1F"):  #   LaunchSoundTask
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write("\n")

                    Length = int(Line[i+5], 16)
                    for j in range(Length):
                        NewFile.write("\t"+Line[i+6+(j+j)]+" ")
                        NewFile.write(Line[i+7+(j+j)]+" ")
                        NewFile.write("\n")
                    
                    Set = 5 + Length*2
                    
                elif(Line[i] == "20"):  #   WaitForSound
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "21"):  #   JumpIfArgumentEquals
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write(Line[i+6]+" ")
                    NewFile.write(Line[i+7]+" ")
                    NewFile.write("\n")
                    Set = 7

                    Offset = Line[i+7]+Line[i+6]+Line[i+5]+Line[i+4]
                    if(Offset not in CallList):
                        CallList.append(Offset)
                        Calls += 1
                        if(Offset in Address):
                            Presets += 1

                elif(Line[i] == "22"):  #   Cmd22
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "23"):  #   Cmd23
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "24"):  #   JumpIfContest
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write("\n")
                    Set = 4
                    
                    Offset = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                    if(Offset not in CallList):
                        CallList.append(Offset)
                        Calls += 1
                        if(Offset in Address):
                            Presets += 1

                elif(Line[i] == "25"):  #   ChooseBG
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write("\n")
                    Set = 3

                elif(Line[i] == "26"):  #   PlaySoundPanChange2
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write(Line[i+6]+" ")
                    NewFile.write("\n")
                    Set = 6

                elif(Line[i] == "27"):  #   PlaySoundPanChange3
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write(Line[i+2]+" ")
                    NewFile.write(Line[i+3]+" ")
                    NewFile.write(Line[i+4]+" ")
                    NewFile.write(Line[i+5]+" ")
                    NewFile.write(Line[i+6]+" ")
                    NewFile.write("\n")
                    Set = 6

                elif(Line[i] == "28"):  #   LeftOverPartner
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "29"):  #   BankOverPartner
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "2A"):  #   LeftFoeOverPartner
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "2B"):  #   MakeInvisible
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "2C"):  #   MakeVisible
                    NewFile.write(Line[i]+" ")
                    NewFile.write(Line[i+1]+" ")
                    NewFile.write("\n")
                    Set = 1

                elif(Line[i] == "2D"):  #   Cmd2D
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "2E"):  #   Cmd2E
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

                elif(Line[i] == "2F"):  #   StopMusic
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")
                    
                else:
                    NewFile.write(Line[i]+" ")
                    NewFile.write("\n")

    NewFile.write("\n")
    NewFile.write("There are %d branches and %d unique call statements \n" % (Branch, Calls))
    NewFile.write("%d of those %d call statements are presets. \n" % (Presets, Calls))
    if(Branch != (Calls-Presets)):
        NewFile.write("Uneven number of branches and calls! Check in more detail! \n")
                
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
        
        for FileName in os.listdir(os.getcwd() + "/Input/"):
            if FileName.endswith(".txt"):
                
                DataFile = open(os.getcwd() + "/Input/"+ FileName, "r")

                if(AllOne == 1 and Set2 == 0):
                    NewFile = open(os.getcwd() + "/Output/Split/MegaFile.txt", "w")
                    Set2 = 1
                    
                elif(AllOne != 1):
                    X += 1
                    NewFile = open(os.getcwd() + "/Output/Split/" + str(X) + ".txt", "w")

                print("Now starting: %s" % FileName)
                print(" ")

                MoveName = FileName[:-4]

                NewFile.write("-----------------------------------------")
                NewFile.write("\n")
                NewFile.write(MoveName)
                NewFile.write("\n")
                NewFile.write("-----------------------------------------")
                NewFile.write("\n")
                
                SplitUp(DataFile, NewFile)

                if(AllOne != 1):
                    NewFile.close()
                    
        if(AllOne == 1):
            NewFile.close()
            
    else:
        Set = 0
        
        while(Set == 0):
            NewName = input("Enter the name of the file to create: ")
            print(" ")
            if(os.path.isfile(os.getcwd() + "/Output/Split/" + NewName + ".txt") == True):
                Overwrite = int(input(("File already exists. Press 1 to overwrite. ")))
                if(Overwrite == 1):
                    Set = 1
            else:
                Set = 1

        NewFile = open(os.getcwd() + "/Output/Split/" + NewName + ".txt", "w")

        NewFile.write("-----------------------------------------")
        NewFile.write("\n")
        NewFile.write(OldName)
        NewFile.write("\n")
        NewFile.write("-----------------------------------------")
        NewFile.write("\n")
        
        SplitUp(DataFile, NewFile)

        NewFile.write("\n")

        NewFile.close()
        
    Continue = input("Again? Press 1 to quit. ")

print("Goodbye!")
