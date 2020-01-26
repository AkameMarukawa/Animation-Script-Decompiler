import os.path
import re

# The point of this code is to take a .txt file as an input
# and create another .txt file which contains LaTeX code that
# you can copy-paste right into your document.

# Colour coding:
# red = addresses, names of branches (including temps/tasks)
# blue = commands
# orange = banks, names of sounds/BGs, first arg (if one of
# those three things)
# green/fern = first argument of command
# purple/eggplant = second argument of command
# magneta = third argument of command
# black = fourth argument of command

Item = "\\item[]"

#   The best way I found to format this is to have each line
#   of the animation script be an item in a list.
# ----------------------------------------------------------------
def BankKeyword(Value, File):
# This function takes in a value and loops through the list of
# named banks. Then if the value matches one of them, it will
# write out the keyword instead of the number.

# If not, it writes out the value as given.
# Ex: 00 -> User, 02 -> MySide

    List = open(os.getcwd() + "/Lists/Bank.txt", "r")
    #   os.getcwd() is to get the current directory that the
    #   program is in.

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")
        #   Line has two elements.
        #   The first is the name
        #   The second is the value

        if(Value == Line[1]):
            File.write("\\textcolor{orange}{" + Line[0] + "} ")
            return

    File.write("\\textcolor{orange}{" + Value + "} ")
    return
# ----------------------------------------------------------------
def CallKeyword(Value, Offset, File, CallList, Name):
# This function takes in a value and loops through the list of
# named preset-calls. Then if the value matches one of them, it will
# write out the keyword instead of the number.
# If not, it writes out the value as given.

# As well, it also puts the value (the address being called)
# into a list of all the calls the script invokes (if it is
# not in that list already. It only does this if it is not a
# preset call.

# This is used for later when the names of the branches and the
# names of the calls need to be made the same.

    Calls = open(os.getcwd() + "/Lists/Calls.txt", "r")

    for Line in Calls:
        Line = Line.strip()
        Line = Line.split(", ")
        #   Line has two elements.
        #   The first is the name
        #   The second is the value

        if(Value == Line[1]):
            File.write("\\textcolor{brown}{" + Line[0] + "} ")
            return CallList

    if(Offset not in CallList):
        CallList.append(Offset)
        CallList.sort()

    NewFile.write("\\textcolor{red}{" + Value + Name.replace(" ","") + "+ROM} ")
    return CallList
# ----------------------------------------------------------------
def TempKeyword(Value, File):
# This function is used to print the name of the template being
# called. It takes the address of the template given (Value)
# and loops through the Temp.txt file until it finds an address
# that matches Value.

# If it's not in there, it just prints out the address as given.

    List = open(os.getcwd() + "/Lists/Temp.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")
        #   Line has two elements.
        #   The first is the name
        #   The second is the value

        if(Value == Line[1]):
            File.write("\\textcolor{red}{" + Line[0] + "} ")
            return

    File.write("\\textcolor{red}{" + Value + "} ")
    return
# ----------------------------------------------------------------
def TaskKeyword(Value, File):
# This function is used to print the name of the task being
# called. It takes the address of the template given (Value)
# and loops through the Task.txt file until it finds an address
# that matches Value.

# If it's not in there, it just prints out the address as given.

    List = open(os.getcwd() + "/Lists/Task.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Value == Line[1]):
            File.write("\\textcolor{red}{" + Line[0] + "} ")
            return
        
    File.write("\\textcolor{red}{" + Value + "} ")
    return
# ----------------------------------------------------------------
def BGKeyword(Value, File):
# This function takes in a value and loops through the list of
# named backgrounds (BG). Then if the value matches one of them,
# it will write out the keyword instead of the number.
# If not, it writes out the value as given.

    List = open(os.getcwd() + "/Lists/BG.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")

        if(Value == Line[1]):
            File.write("\\textcolor{orange}{" + Line[0] + "} ")
            return

    File.write("\\textcolor{orange}{" + Value + "} ")
    return
# ----------------------------------------------------------------
def SongKeyword(Value, File):
# This function takes in a value and loops through the list of
# named sounds. Then if the value matches one of them,
# it will write out the keyword instead of the number.
# If not, it writes out the value as given.

    List = open(os.getcwd() + "/Lists/Song.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")
        #   Line has two elements.
        #   The first is the name
        #   The second is the value

        if(Value == Line[1]):
            File.write("\\textcolor{orange}{" + Line[0] + "} ")
            return

    File.write("\\textcolor{orange}{0x" + Value + "} ")
    return
# ----------------------------------------------------------------
def CreateHeader(Name, File):
# The point of this function is to create a header for the
# animation script so that when you put multiple scripts into
# LaTeX, you can 
    List = open(os.getcwd() + "/Lists/Moves.txt", "r")

    for Line in List:
        Line = Line.strip()
        Line = Line.split(", ")
        #   Line has two elements.
        #   The first is the name
        #   The second is the value for FireRed
        #   The third is the value for Emerald
        
        if(Name == Line[0]):
            File.write("\\begin{center}" + "\n")
            File.write("\\section*{\\textcolor{title}{" + Name + ":} " + "\\textcolor{firered}{" + Line[1] + "} " + "\\textcolor{emerald}{" + Line[2] + "}}"  + "\n")
            File.write("\\end{center}" + "\n")
            File.write("\n")
            return
        
            # The heading is centred on the page and is also a LaTeX section
            # so the font is bigger. The FireRed offset is written in red and
            # the Emerald font is written in green.
            # Function ends as soon as the correct name and offset is found.

    File.write("\\begin{center}" + "\n")
    File.write("\\section*{\\textcolor{title}{" + Name + ":}} " + "\n")
    File.write("\\end{center}" + "\n")
    File.write("\n")
    return

    # If the name of the move is not found in the preset offsets file
    # then it just prints the name of the move (the name of the input file)
    # and nothing else.
# ----------------------------------------------------------------
def Decompile(FileName, NewFile, Name):
# This is the meat of this program and kind of the main purpose of it
# This loops through the given file (FileName) and converts the bytes
# (in hexadecimal) into human-readable script (NewFile).
# Name is the name of the move (taken from the name of the input file).

# A couple things to note: the input file must be written as a series of
# hexadecimal bytes separated only by spaces.

# Ex: 01 02 03 04 05 = RIGHT

# There can't be any newlines in it or this won't work right.

# Ex: 01 02 03
#     04 05
#     06 07 08
#     = WRONG


    for Line in FileName:
        Line = Line.strip()
        Line = Line.split()

        Set = 0
        #   This variable called Set is very important!
        #   This is what allows the program to skip bytes

        if(len(Line) == 0):
            continue
        #   This is a fail-safe so that it will skip newlines in the
        #   input file (which shoud really not be there anyway).

        CallList = []
        Branch = 0

        #   Branch and CallList 

        for i in range(len(Line)):
            
            if Set > 0:
                Set -= 1
                continue
            
            if(Line[i] == "00"):  #   LoadParticle
                NewFile.write(Item + "\\textcolor{blue}{LoadParticle} ")
                NewFile.write("\\textcolor{orange}{0x")
                NewFile.write(Line[i+2])
                NewFile.write(Line[i+1] + "}")
                NewFile.write("\n")
                Set = 2
                
            elif(Line[i] == "01"):  #   UnloadParticle
                NewFile.write(Item + "\\textcolor{blue}{UnloadParticle} ")
                NewFile.write("\\textcolor{orange}{0x")
                NewFile.write(Line[i+2])
                NewFile.write(Line[i+1] + "}")
                NewFile.write("\n")
                Set = 2
                
            elif(Line[i] == "02"):  #   LaunchTemplate
                NewFile.write(Item + "\\textcolor{blue}{LaunchTemplate} ")
                X = Line[i+4] + Line[i+3] + Line[i+2] + Line[i+1]
                TempKeyword(X, NewFile)
                NewFile.write("\\textcolor{fern}{" + "0x" + Line[i+5] + "} ")
                NewFile.write("\\textcolor{eggplant}{" + "0x" + Line[i+6] + "} ")
                NewFile.write("\n")

                Length = int(Line[i+6], 16)
                for j in range(Length):
                    NewFile.write(Item + "\\textcolor{fern}{.hword 0x")
                    NewFile.write(Line[i+8+(j+j)])
                    NewFile.write(Line[i+7+(j+j)] + "} ")
                    NewFile.write("\n")
                
                Set = 6 + Length*2
                    
            elif(Line[i] == "03"):  #   LaunchTask
                NewFile.write(Item + "\\textcolor{blue}{LaunchTask} ")
                X = Line[i+4] + Line[i+3] + Line[i+2] + Line[i+1]
                TaskKeyword(X, NewFile)
                NewFile.write("\\textcolor{fern}{" + "0x" + Line[i+5] + "} ")
                NewFile.write("\\textcolor{eggplant}{" + "0x" + Line[i+6] + "} ")
                NewFile.write("\n")

                Length = int(Line[i+6], 16)
                for j in range(Length):
                    NewFile.write(Item + "\\textcolor{fern}{.hword 0x")
                    NewFile.write(Line[i+8+(j+j)])
                    NewFile.write(Line[i+7+(j+j)] + "} ")
                    NewFile.write("\n")
                
                Set = 6 + Length*2

            elif(Line[i] == "04"):  #   Pause
                NewFile.write(Item + "\\textcolor{blue}{Pause} ")
                NewFile.write("\\textcolor{fern}{0x" + Line[i+1] + "}")
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "05"):  #   WaitAnimation
                NewFile.write(Item + "\\textcolor{blue}{WaitAnimation} ")
                NewFile.write("\n")

            elif(Line[i] == "06"):  #   Cmd6
                NewFile.write(Item + "\\textcolor{blue}{Cmd6} ")
                NewFile.write("\n")

            elif(Line[i] == "07"):  #   Cmd6
                NewFile.write(Item + "\\textcolor{blue}{Cmd7} ")
                NewFile.write("\n") 
                
            elif(Line[i] == "08"):  #   End
                NewFile.write(Item + "\\textcolor{blue}{End} ")
                NewFile.write("\n")
                NewFile.write("\\end{itemize}")
                NewFile.write("\n")
                if(len(Line[i:i+2]) > 1):
                    NewFile.write("\\vspace{14pt}")
                    NewFile.write("\n")
                    NewFile.write("\n")
                    NewFile.write("\\textcolor{red}{" + Name.replace(" ","") + str(Branch) + ":}")
                    NewFile.write("\n")
                    NewFile.write("\\begin{itemize}")
                    NewFile.write("\n")
                    Branch += 1

            elif(Line[i] == "09"):  #   PlaySound1
                NewFile.write(Item + "\\textcolor{blue}{PlaySound1} ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 2

            elif(Line[i] == "0A"):  #   MoveSpriteToBG
                NewFile.write(Item + "\\textcolor{blue}{MoveSpriteToBG} ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "0B"):  #   MoveSpriteFromBG
                NewFile.write(Item + "\\textcolor{blue}{MoveSpriteFromBG} ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "0C"):  #   SetBlends
                NewFile.write(Item + "\\textcolor{blue}{SetBlends} ")
                NewFile.write("\\textcolor{fern}{0x")
                NewFile.write(Line[i+2])
                NewFile.write(Line[i+1] + "}")
                NewFile.write("\n")
                Set = 2
                
            elif(Line[i] == "0D"):  #   ResetBlends
                NewFile.write(Item + "\\textcolor{blue}{ResetBlends} ")
                NewFile.write("\n")

            elif(Line[i] == "0E"):  #   Call
                NewFile.write(Item + "\\textcolor{blue}{Call} ")
                Value = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                NewFile.write("\n")
                Set = 4

            elif(Line[i] == "0F"):  #   Return
                NewFile.write(Item + "\\textcolor{blue}{Return} ")
                NewFile.write("\n")
                NewFile.write("\\end{itemize}")
                NewFile.write("\n")
                if(len(Line[i:i+2]) > 1):
                    NewFile.write("\\vspace{14pt}")
                    NewFile.write("\n")
                    NewFile.write("\n")
                    NewFile.write("\\textcolor{red}{" + Name.replace(" ","") + str(Branch) + ":}")
                    NewFile.write("\n")
                    NewFile.write("\\begin{itemize}")
                    NewFile.write("\n")
                    Branch += 1

            elif(Line[i] == "10"):  #   SetArgument
                NewFile.write(Item + "\\textcolor{blue}{SetArgument} ")
                NewFile.write("\\textcolor{fern}{0x")
                NewFile.write(Line[i+1] + "} ")
                NewFile.write("\\textcolor{eggplant}{0x")
                NewFile.write(Line[i+3])
                NewFile.write(Line[i+2] + "} ")
                NewFile.write("\n")
                Set = 3

            elif(Line[i] == "11"):  #   ChooseTwoTurnAnimation
                NewFile.write(Item + "\\textcolor{blue}{ChooseTwoTurnAnimation} ")
                
                Value = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                    
                Value = Line[i+8]+Line[i+7]+Line[i+6]+Line[i+5]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                
                NewFile.write("\n")
                NewFile.write("\\end{itemize}")
                NewFile.write("\n")
                
                if(len(Line[i+8:i+10]) > 1):
                    NewFile.write("\\vspace{14pt}")
                    NewFile.write("\n")
                    NewFile.write("\n")
                    NewFile.write("\\textcolor{red}{" + Name.replace(" ","") + str(Branch) + ":}")
                    NewFile.write("\n")
                    NewFile.write("\\begin{itemize}")
                    NewFile.write("\n")
                    Branch += 1
                    
                Set = 8
                
            elif(Line[i] == "12"):  #   JumpIfMoveTurnEquals
                NewFile.write(Item + "\\textcolor{blue}{JumpIfMoveTurnEquals} ")
                NewFile.write("\\textcolor{fern}{0x")
                NewFile.write(Line[i+1] + "} ")

                Value = Line[i+5]+Line[i+4]+Line[i+3]+Line[i+2]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)

                NewFile.write("\n")
                Set = 5

            elif(Line[i] == "13"):  #   Jump
                NewFile.write(Item + "\\textcolor{blue}{Jump} ")
                
                Value = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                
                NewFile.write("\n")
                NewFile.write("\\end{itemize}")
                NewFile.write("\n")
                
                if(len(Line[i+4:i+6]) > 1):
                    NewFile.write("\\vspace{14pt}")
                    NewFile.write("\n")
                    NewFile.write("\n")
                    NewFile.write("\\textcolor{red}{" + Name.replace(" ","") + str(Branch) + ":}")
                    NewFile.write("\n")
                    NewFile.write("\\begin{itemize}")
                    NewFile.write("\n")
                    Branch += 1
                Set = 4

            elif(Line[i] == "14"):  #   LoadBG1
                NewFile.write(Item + "\\textcolor{blue}{LoadBG1} ")
                BGKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1
                
            elif(Line[i] == "15"):  #   LoadDefaultBG
                NewFile.write(Item + "\\textcolor{blue}{LoadDefaultBG} ")
                NewFile.write("\n")

            elif(Line[i] == "16"):  #   WaitForBG
                NewFile.write(Item + "\\textcolor{blue}{WaitForBG} ")
                NewFile.write("\n")

            elif(Line[i] == "17"):  #   WaitForTransparentBG
                NewFile.write(Item + "\\textcolor{blue}{WaitForTransparentBG} ")
                NewFile.write("\n")

            elif(Line[i] == "18"):  #   LoadBG2
                NewFile.write(Item + "\\textcolor{blue}{LoadBG2} ")
                BGKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "19"):  #   PlaySound2
                NewFile.write(Item + "\\textcolor{blue}{PlaySound2} ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("\\textcolor{fern}{0x" + Line[i+3] + "}")
                NewFile.write("\n")
                Set = 3

            elif(Line[i] == "1A"):  #   PanControl
                NewFile.write(Item + "\\textcolor{blue}{PanControl} ")
                NewFile.write("\\textcolor{fern}{0x" + Line[i+1] + "}")
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "1B"):  #   PlaySoundPanChange
                NewFile.write(Item + "\\textcolor{blue}{PlaySoundPanChange} ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("\\textcolor{fern}{0x" + Line[i+3] + "} ")
                NewFile.write("\\textcolor{eggplant}{0x" + Line[i+4] + "} ")
                NewFile.write("\\textcolor{magenta}{0x" + Line[i+5] + "} ")
                NewFile.write("\\textcolor{black}{0x" + Line[i+6] + "}")
                NewFile.write("\n")
                Set = 6

            elif(Line[i] == "1C"):  #   AdvancedPlaySound
                NewFile.write(Item + "\\textcolor{blue}{AdvancedPlaySound} ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("\\textcolor{fern}{0x" + Line[i+3] + "} ")
                NewFile.write("\\textcolor{eggplant}{0x" + Line[i+4] + "} ")
                NewFile.write("\\textcolor{magenta}{0x" + Line[i+5] + "}")
                NewFile.write("\n")
                Set = 5

            elif(Line[i] == "1D"):  #   PlaySound3
                NewFile.write(Item + "\\textcolor{blue}{PlaySound3} ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("\\textcolor{fern}{0x" + Line[i+3] + "} ")
                NewFile.write("\\textcolor{eggplant}{0x" + Line[i+4] + "}")
                NewFile.write("\n")
                Set = 4

            elif(Line[i] == "1E"):  #   SetBlendCount
                NewFile.write(Item + "\\textcolor{blue}{SetBlendCount} ")
                NewFile.write("\\textcolor{fern}{0x")
                NewFile.write(Line[i+2])
                NewFile.write(Line[i+1] + "}" + "\n")
                NewFile.write("\n")
                Set = 2

            elif(Line[i] == "1F"):  #   LaunchSoundTask
                NewFile.write(Item + "\\textcolor{blue}{LaunchSoundTask} ")
                
                X = Line[i+4] + Line[i+3] + Line[i+2] + Line[i+1]
                TaskKeyword(X, NewFile)
                NewFile.write("\\textcolor{fern}{0x" + Line[i+5] + "} ")
                NewFile.write("\n")

                Length = int(Line[i+5], 16)
                for j in range(Length):
                    NewFile.write(Item + "\\textcolor{fern}{.hword 0x")
                    NewFile.write(Line[i+7+(j+j)])
                    NewFile.write(Line[i+6+(j+j)] + "} ")
                    NewFile.write("\n")
                
                Set = 5 + Length*2
                
            elif(Line[i] == "20"):  #   WaitForSound
                NewFile.write(Item + "\\textcolor{blue}{WaitForSound} ")
                NewFile.write("\n")

            elif(Line[i] == "21"):  #   JumpIfArgumentEquals
                NewFile.write(Item + "\\textcolor{blue}{JumpIfArgumentEquals} ")
                NewFile.write("\\textcolor{fern}{0x")
                NewFile.write(Line[i+1] + "} ")
                NewFile.write("\\textcolor{eggplant}{0x")
                NewFile.write(Line[i+3])
                NewFile.write(Line[i+2] + "} ")
                
                Value = Line[i+7]+Line[i+6]+Line[i+5]+Line[i+4]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                
                NewFile.write("\n")
                Set = 7

            elif(Line[i] == "22"):  #   Cmd22
                NewFile.write(Item + "\\textcolor{blue}{Cmd22} ")
                NewFile.write("\\textcolor{fern}{0x" + Line[i+1] + "}")
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "23"):  #   Cmd23
                NewFile.write(Item + "\\textcolor{blue}{Cmd23} ")
                NewFile.write("\\textcolor{fern}{0x" + Line[i+1] + "}")
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "24"):  #   JumpIfContest
                NewFile.write(Item + "\\textcolor{blue}{JumpIfContest} ")

                Value = Line[i+4]+Line[i+3]+Line[i+2]+Line[i+1]
                Offset = Value+Name.replace(" ","")
                CallList = CallKeyword(Value, Offset, NewFile, CallList, Name)
                
                NewFile.write("\n")
                Set = 4

            elif(Line[i] == "25"):  #   ChooseBG
                NewFile.write(Item + "\\textcolor{blue}{ChooseBG} ")
                BGKeyword(Line[i+1], NewFile)
                BGKeyword(Line[i+2], NewFile)
                BGKeyword(Line[i+3], NewFile)
                NewFile.write("\n")
                Set = 3

            elif(Line[i] == "26"):  #   PlaySoundPanChange2
                NewFile.write(Item + "\\textcolor{blue}{PlaySoundPanChange2} ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("\\textcolor{fern}{0x" + Line[i+3] + "} ")
                NewFile.write("\\textcolor{eggplant}{0x" + Line[i+4] + "} ")
                NewFile.write("\\textcolor{magenta}{0x" + Line[i+5] + "} ")
                NewFile.write("\\textcolor{black}{0x" + Line[i+6] + "}")
                NewFile.write("\n")
                Set = 6

            elif(Line[i] == "27"):  #   PlaySoundPanChange3
                NewFile.write(Item + "\\textcolor{blue}{PlaySoundPanChange3} ")
                SongKeyword(Line[i+1], NewFile)
                NewFile.write("\\textcolor{fern}{0x" + Line[i+3] + "} ")
                NewFile.write("\\textcolor{eggplant}{0x" + Line[i+4] + "} ")
                NewFile.write("\\textcolor{magenta}{0x" + Line[i+5] + "} ")
                NewFile.write("\\textcolor{black}{0x" + Line[i+6] + "}")
                NewFile.write("\n")
                Set = 6

            elif(Line[i] == "28"):  #   LeftOverPartner
                NewFile.write(Item + "\\textcolor{blue}{LeftOverPartner} ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "29"):  #   BankOverPartner
                NewFile.write(Item + "\\textcolor{blue}{BankOverPartner} ")
                NewFile.write("\n")

            elif(Line[i] == "2A"):  #   LeftFoeOverPartner
                NewFile.write(Item + "\\textcolor{blue}{LeftFoeOverPartner} ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "2B"):  #   MakeInvisible
                NewFile.write(Item + "\\textcolor{blue}{MakeInvisible} ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "2C"):  #   MakeVisible
                NewFile.write(Item + "\\textcolor{blue}{MakeVisible} ")
                BankKeyword(Line[i+1], NewFile)
                NewFile.write("\n")
                Set = 1

            elif(Line[i] == "2D"):  #   Cmd2D
                NewFile.write(Item + "\\textcolor{blue}{Cmd2D} ")
                NewFile.write("\n")

            elif(Line[i] == "2E"):  #   Cmd2E
                NewFile.write(Item + "\\textcolor{blue}{Cmd2D} ")
                NewFile.write("\n")

            elif(Line[i] == "2F"):  #   StopMusic
                NewFile.write(Item + "\\textcolor{blue}{StopMusic} ")
                NewFile.write("\n")
            else:
                NewFile.write("UNKNOWN COMMAND")
                NewFile.write("\n")

    return CallList
# ----------------------------------------------------------------
def ReplaceCallThing(List, FileName, MoveName):

    with open(FileName, 'r') as file:
        FileData = file.read()

    for i in range(len(List)):
        FileData = FileData.replace(List[i]+"+ROM", MoveName+str(i)+"+ROM")

    with open(FileName, 'w') as file:
        file.write(FileData)
# ----------------------------------------------------------------  
Continue = 0

while(Continue != "1"):
    Set = 0

    while(Set == 0):
        #   This While Loop is here to let the user have the option of
        #   trying another file name if the one they entered is invalid
        #   such as if they spelled the name wrong by accident
        #   or if they thought they put the file in the Input folder but
        #   actually didn't.
        
        print("Enter the name of a .txt file: ")
        OldName = input("Enter 'doall' to do all files in the input folder. ")
        print(" ")

        if(OldName == "doall"):
            Set = 1

        else:
            #   Here we are trying to open a .txt file with the given name in
            #   the Input directory.
            #   If this fails (file DNE), then it will say so.
            #   User will be given another chance to put a new name in.
            
            try:
                DataFile = open(os.getcwd() + "/Input/" + OldName + ".txt", "r")
            except:
                print("Error! File not found.")
                print("Make sure it is a .txt file, inside of the Input folder")
                print("and also that you spelled the name correctly.")
                print(" ")
            else:
                Set = 1
                
    # ----------------------------------------------------------------
    #                           DO ALL
    # ----------------------------------------------------------------
    
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
                    NewFile = open(os.getcwd() + "/Output/LaTeX/MegaFile.txt", "w")
                    Set2 = 1
                    
                elif(AllOne != 1):
                    X += 1
                    NewFile = open(os.getcwd() + "/Output/LaTeX/" + str(X) + ".txt", "w")

                print("Now starting: %s" % FileName)
                print(" ")

                MoveName = FileName[:-4]
                
                CreateHeader(MoveName, NewFile)

                NewFile.write("\\begin{itemize}" + "\n")
                
                CallList = Decompile(DataFile, NewFile, MoveName)
                MasterList.append(CallList)

                NewFile.write("\n")
                NewFile.write("\\newpage" + "\n" + "\n")

                if(AllOne != 1):
                    PutInPresets(NewFile)
                    NewFile.close()
                    
                    NewFile = open(os.getcwd() + "/Output/LaTeX/" + str(X) + ".txt", "r+")
                    ReplaceCallThing(CallList, os.getcwd() + "/Output/LaTeX/" + str(X) + ".txt", MoveName.replace(" ",""))
                    
        if(AllOne == 1):
            NewFile.close()

            NewFile = open(os.getcwd() + "/Output/LaTeX/MegaFile.txt", "r+")
            
            i = -1
            for Element in FileNameList:
                i += 1
                ReplaceCallThing(MasterList[i], os.getcwd() + "/Output/LaTeX/MegaFile.txt", Element.replace(" ",""))
            
    else:
        Set = 0
        
        while(Set == 0):
            NewName = input("Enter the name of the file to create: ")
            print(" ")
            
            if(os.path.isfile(os.getcwd() + "/Output/LaTeX/" + NewName + ".txt") == True):
                Overwrite = int(input(("File already exists. Press 1 to overwrite. ")))
                if(Overwrite == 1):
                    Set = 1
            else:
                Set = 1

        NewFile = open(os.getcwd() + "/Output/LaTeX/" + NewName + ".txt", "w")

        CreateHeader(OldName, NewFile)

        NewFile.write("\\begin{itemize}" + "\n")
        
        CallList = Decompile(DataFile, NewFile, OldName)

        NewFile.write("\n")
        NewFile.write("\\newpage" + "\n")
        NewFile.close()

        #   We need to close the file first before we reopen it in r+ mode
        #   r+ = read/write
        #   This will let us edit without overwriting the whole file.
        #   This will let us replace our invoked Calls with nicer looking names.

        NewFile = open(os.getcwd() + "/Output/LaTeX/" + NewName + ".txt", "r+")
        
        ReplaceCallThing(CallList, os.getcwd() + "/Output/LaTeX/" + NewName + ".txt", OldName.replace(" ",""))

    Continue = input("Again? Press 1 to quit. ")

print("Goodbye!")
