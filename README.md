TSRlearn_BIE – PsychoPy Task Files
This repository contains the PsychoPy experiment files for the TSRlearn project.
The task is split into multiple blocks (practice, localizers, main task blocks), each implemented as a separate PsychoPy experiment file.
Requirements
PsychoPy
This task was created using PsychoPy 2025.1.1. I'm not sure if it will run with other psychopy versions. 
Running the Task
Paths to stimuli and sequence files are defined relative to the project structure. The task can therefore be run without having to change path settings. 
When the task is run, a new folder called data/ will be created automatically. All behavioural output files (e.g. .csv, .tsv) will be stored there.
Language can be changed in the first routine of each task block. In a code component named exp_settings, there is a variable controlling language selection. The language must be provided as a string, like "english" or "german".
