import os.path

def Extras(FileName, NewFile):

    Preset = open(os.getcwd() + "/Lists/Calls.txt", "r")
    Address = []
    Names = []
    
    for Line in Preset:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Line != []):
            Address.append(Line[1])
            Names.append(Line[0])
# -----------------------------------------------------------
    Temps = open(os.getcwd() + "/Lists/Temp.txt", "r")
    TempAddress = []
    TempNames = []
    
    for Line in Temps:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Line != []):
            TempAddress.append(Line[1])
            TempNames.append(Line[0])
# -----------------------------------------------------------
    Tasks = open(os.getcwd() + "/Lists/Task.txt", "r")
    TaskAddress = []
    NamesTasks = []
    
    for Line in Tasks:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Line != []):
            TaskAddress.append(Line[1])
            NamesTasks.append(Line[0])
# -----------------------------------------------------------
    for Line in FileName:
            Line = Line.strip()
            Line = Line.split()

            Set = 0
            Branch = -1
            PresetNum = 0

            Particles = []
            Sounds = []
            BG = []
            Task = 0
            
            Calls = []
            Presets = []
            
            Templates = []
            Tasks = []
            TemplateName = []
            TaskNames = []

            if(len(Line) == 0):
                continue

            for i in range(len(Line)):
                
                if Set > 0:
                    Set -= 1
                    continue
                
                if(Line[i] == "00"):  #   LoadParticle
                    if(Line[i+2]+Line[i+1] not in Particles):
                        Particles.append(Line[i+2]+Line[i+1])
                    Set = 2

                elif(Line[i] == "01"):  #   UnloadParticle
                    Set = 2
                    
                elif(Line[i] == "02"):  #   LaunchTemplate
                    THING = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]     # Address
                    Length = int(Line[i+6], 16)
                    if(THING not in Templates):
                        Templates.append(THING)
                        
                        for i in range(len(TempAddress)):
                            if(TempAddress[i] == THING):
                                TemplateName.append([TempAddress[i], TempNames[i]])

                        TemplateName.append([0,0])

                    Set = 6 + Length*2
                        
                elif(Line[i] == "03"):  #   LaunchTask
                    THING = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]     # Address
                    Length = int(Line[i+6], 16)
                    if(THING not in Tasks):
                        Tasks.append(THING)
                        
                        for i in range(len(TaskAddress)):
                            if(TaskAddress[i] == THING):
                                TaskNames.append([TaskAddress[i], NamesTasks[i]])

                        TaskNames.append([0,0])

                    Set = 6 + Length*2

                elif(Line[i] == "04"):  #   Pause
                    Set = 1

                elif(Line[i] == "08"):  #   End
                    Branch += 1
                    
                elif(Line[i] == "09"):  #   PlaySound1
                    if(Line[i+2]+Line[i+1] not in Sounds):
                        Sounds.append(Line[i+2]+Line[i+1])
                    Set = 2

                elif(Line[i] == "0A"):  #   MoveSpriteToBG
                    Set = 1

                elif(Line[i] == "0B"):  #   MoveSpriteFromBG
                    Set = 1

                elif(Line[i] == "0C"):  #   SetBlends
                    Set = 2

                elif(Line[i] == "0E"):  #   Call
                    THING = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]     # Address
                    if(THING not in Calls):
                        Calls.append(THING)
                        
                        for i in range(len(Address)):
                            if(Address[i] == THING):
                                Presets.append([Address[i], Names[i]])
                                PresetNum += 1

                        Presets.append([0,0])
                                       
                    Set = 4

                elif(Line[i] == "0F"):  #   Return
                    Branch += 1

                elif(Line[i] == "10"):  #   SetArgument
                    Set = 3

                elif(Line[i] == "11"):  #   ChooseTwoTurnAnimation
                    THING = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]     # Address
                    THING2 = Line[i+8]+Line[i+7]+Line[i+6]+Line[i+5]
                    if(THING not in Calls):
                        Calls.append(THING)
                        
                        for i in range(len(Address)):
                            if(Address[i] == THING):
                                Presets.append([Address[i], Names[i]])
                                PresetNum += 1

                        Presets.append([0,0])
                        
                    if(THING2 not in Calls):
                        Calls.append(THING2)
                        
                        for i in range(len(Address)):
                            if(Address[i] == THING2):
                                Presets.append([Address[i], Names[i]])
                                PresetNum += 1

                        Presets.append([0,0])
                    Branch += 1
                    Set = 8
                    
                elif(Line[i] == "12"):  #   JumpIfMoveTurnEquals
                    THING = Line[i+5]+Line[i+4]+Line[i+3]+Line[i+2]     # Address
                    if(THING not in Calls):
                        Calls.append(THING)
                        
                        for i in range(len(Address)):
                            if(Address[i] == THING):
                                Presets.append([Address[i], Names[i]])
                                PresetNum += 1

                        Presets.append([0,0])
                    Set = 5

                elif(Line[i] == "13"):  #   Jump
                    THING = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]     # Address
                    if(THING not in Calls):
                        Calls.append(THING)
                        
                        for i in range(len(Address)):
                            if(Address[i] == THING):
                                Presets.append([Address[i], Names[i]])
                                PresetNum += 1

                        Presets.append([0,0])
                    Branch += 1
                    Set = 4

                elif(Line[i] == "14"):  #   LoadBG1
                    if(Line[i+1] not in BG):
                        BG.append(Line[i+1])
                    Set = 1

                elif(Line[i] == "18"):  #   LoadBG2
                    if(Line[i+1] not in BG):
                        BG.append(Line[i+1])
                    Set = 1

                elif(Line[i] == "19"):  #   PlaySound2
                    if(Line[i+2]+Line[i+1] not in Sounds):
                        Sounds.append(Line[i+2]+Line[i+1])
                    Set = 3
                    
                elif(Line[i] == "1A"):  #   PanControl
                    Set = 1
            
                elif(Line[i] == "1B"):  #   PlaySoundPanChange
                    if(Line[i+2]+Line[i+1] not in Sounds):
                        Sounds.append(Line[i+2]+Line[i+1])
                    Set = 6

                elif(Line[i] == "1C"):  #   AdvancedPlaySound
                    if(Line[i+2]+Line[i+1] not in Sounds):
                        Sounds.append(Line[i+2]+Line[i+1])
                    Set = 5

                elif(Line[i] == "1D"):  #   PlaySound3
                    if(Line[i+2]+Line[i+1] not in Sounds):
                        Sounds.append(Line[i+2]+Line[i+1])
                    Set = 4

                elif(Line[i] == "1E"):  #   SetBlendCount
                    Set = 2

                elif(Line[i] == "1F"):  #   LaunchSoundTask
                    Task += 1

                    THING = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]     # Address
                    Length = int(Line[i+5], 16)
                    if(THING not in Tasks):
                        Tasks.append(THING)
                        
                        for i in range(len(TaskAddress)):
                            if(TaskAddress[i] == THING):
                                TaskNames.append([TaskAddress[i], NamesTasks[i]])

                        TaskNames.append([0,0])

                    Set = 5 + Length*2

                elif(Line[i] == "21"):  #   JumpIfArgumentEquals
                    THING = Line[i+7]+Line[i+6]+Line[i+5]+Line[i+4]     # Address
                    if(THING not in Calls):
                        Calls.append(THING)
                        
                        for i in range(len(Address)):
                            if(Address[i] == THING):
                                Presets.append([Address[i], Names[i]])
                                PresetNum += 1

                        Presets.append([0,0])
                    Set = 7

                elif(Line[i] == "22"):  #   Cmd22
                    Set = 1

                elif(Line[i] == "23"):  #   Cmd23
                    Set = 1

                elif(Line[i] == "24"):  #   JumpIfContest
                    THING = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]     # Address
                    if(THING not in Calls):
                        Calls.append(THING)
                        
                        for i in range(len(Address)):
                            if(Address[i] == THING):
                                Presets.append([Address[i], Names[i]])
                                PresetNum += 1

                        Presets.append([0,0])
                    Set = 4

                elif(Line[i] == "25"):  #   ChooseBG
                    if(Line[i+1] not in BG):
                        BG.append(Line[i+1])
                        
                    if(Line[i+2] not in BG):
                        BG.append(Line[i+2])
                        
                    if(Line[i+3] not in BG):
                        BG.append(Line[i+3])
                    Set = 3

                elif(Line[i] == "26"):  #   PlaySoundPanChange2
                    if(Line[i+2]+Line[i+1] not in Sounds):
                        Sounds.append(Line[i+2]+Line[i+1])
                    Set = 6

                elif(Line[i] == "27"):  #   PlaySoundPanChange3
                    if(Line[i+2]+Line[i+1] not in Sounds):
                        Sounds.append(Line[i+2]+Line[i+1])
                    Set = 6

                elif(Line[i] == "28"):  #   LeftOverPartner
                    Set = 1

                elif(Line[i] == "2A"):  #   LeftFoeOverPartner
                    Set = 1

                elif(Line[i] == "2B"):  #   MakeInvisible
                    Set = 1

                elif(Line[i] == "2C"):  #   MakeVisible
                    Set = 1

    for i in Particles:
        NewFile.write("Particle: 0x%s \n" % i)

    if(len(Particles) > 0):
        NewFile.write("\n")
    
    for i in Sounds:
        NewFile.write("Sound: 0x%s \n" % i)

    if(len(Sounds) > 0):
        NewFile.write("\n")

    for i in BG:
        NewFile.write("Background: 0x%s \n" % i)

    if(len(BG) > 0):
        NewFile.write("\n")

    for i in Calls:
        NewFile.write("Branch to: %s " % i)
        for j in Presets:
            if(i == j[0]):
                NewFile.write("- "+j[1][:-4])
        NewFile.write("\n")

    if(len(Calls) > 0):
        NewFile.write("\n")

    for i in Templates:
        NewFile.write("Template: %s " % i)
        for j in TemplateName:
            if(i == j[0]):
                NewFile.write("- "+j[1].replace("\\",""))
        NewFile.write("\n")

    if(len(Templates) > 0):
        NewFile.write("\n")

    for i in Tasks:
        NewFile.write("Task: %s " % i)
        for j in TaskNames:
            if(i == j[0]):
                NewFile.write("- " + j[1].replace("\\",""))
        NewFile.write("\n")

    if(len(Tasks) > 0):
        NewFile.write("\n")
        
    NewFile.write("There are %d Sound Tasks. \n" % Task)
    NewFile.write("\n")

    NewFile.write("There are %d branches and %d unique call statements. \n" % (Branch, len(Calls)))
    NewFile.write("%d of those %d call statements are presets. \n" % (PresetNum, len(Calls)))
    if(Branch != (len(Calls)-PresetNum)):
        NewFile.write("\n")
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
                    NewFile = open(os.getcwd() + "/Output/Extra Files/MegaFile.txt", "w")
                    Set2 = 1
                    
                elif(AllOne != 1):
                    X += 1
                    NewFile = open(os.getcwd() + "/Output/Extra Files/" + str(X) + ".txt", "w")

                print("Now starting: %s" % FileName)
                print(" ")

                MoveName = FileName[:-4]

                NewFile.write("-----------------------------------------")
                NewFile.write("\n")
                NewFile.write(MoveName)
                NewFile.write("\n")
                NewFile.write("-----------------------------------------")
                NewFile.write("\n")
                
                Extras(DataFile, NewFile)

                if(AllOne != 1):
                    NewFile.close()
                    
        if(AllOne == 1):
            NewFile.close()
            
    else:
        Set = 0
        
        while(Set == 0):
            NewName = input("Enter the name of the file to create: ")
            print(" ")
            if(os.path.isfile(os.getcwd() + "/Output/Extra Files/" + NewName + ".txt") == True):
                Overwrite = int(input(("File already exists. Press 1 to overwrite. ")))
                if(Overwrite == 1):
                    Set = 1
            else:
                Set = 1

        NewFile = open(os.getcwd() + "/Output/Extra Files/" + NewName + ".txt", "w")

        NewFile.write("-----------------------------------------")
        NewFile.write("\n")
        NewFile.write(OldName)
        NewFile.write("\n")
        NewFile.write("-----------------------------------------")
        NewFile.write("\n")
        
        Extras(DataFile, NewFile)

        NewFile.write("\n")

        NewFile.close()
        
    Continue = input("Again? Press 1 to quit. ")

print("Goodbye!")
