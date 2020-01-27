# Animation-Script-Decompiler
A program to help decompile Pokemon Animations from hexadecimal bytes to text (either plain text or LaTeX code). This works with FireRed only so far, but support for Emerald is in the works. This code is written in Python 3, so if you have Python 2, it may not run.

# How to Set It Up
First you will need have a folder called "Input" (spelled in that exact way). You will also need a folder called "Output". These need to be in the same directory as the program. Inside of the Output folder, you will also need four folders named: "Extra Files", "LaTeX", "Plain" and "Split" (capitalised and spelled in exactly these ways). Make sure that the included "ListsFR" and "ListsE" folders are also in that directory.

# How to Use
There are a few things to note before using. The main thing is that if your animation has more than one part (such as it calling other branches of code), then you will need to have the pieces in the input file be in the order they are called. I've included a couple of programs that can help you format things correctly. This was necessary to do so that labeling the branches in the decompiled script worked correctly.

If your compiled animation script has errors in it, such as an improper number of arguments for a command, this program will crash, letting you know there is something wrong.

# What's In Here
1. AnimationScript LaTeX: This decompiles the script into LaTeX code that can be put into your favourite LaTeX typesetter and turned into a PDF. Using this one will have your script be in colour, so it will look the prettiest. You will need to use the following at the beginning of your document if you want it to compile though:

\usepackage[dvipsnames]{xcolor}

\definecolor{fern}{RGB}{64, 128, 0}

\definecolor{eggplant}{RGB}{83, 27, 147}

\definecolor{emerald}{RGB}{102, 156, 53}

\definecolor{firered}{RGB}{227, 36, 0}

\definecolor{title}{RGB}{148, 33, 147}

\definecolor{magenta}{rgb}{0.8, 0.0, 0.8}

I also suggest using \usepackage[letterpaper, total={8in, 10in}]{geometry} too, just to get the margains to look right.

2. AnimationScript Plain: This decompiles the script into a plain .txt file. No colours or anything fancy.

3. SplitUp: This doesn't decompile, but it splits up the bytes so that each command + arguments is on one line, and so that separate branches of the script have a line between them. It will also tell you if there are an uneven number of unique call/jump statements and branches. The output is a plain .txt file.

4. Extras: This creates a .txt file where it lists some basic properties of the animation. This include: Particles, Templates/Tasks, Call/Jump statements, and Sounds. It will also tell you if you have an uneven number of calls/jumps and branches.
