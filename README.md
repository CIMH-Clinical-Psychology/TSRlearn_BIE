# TSRlearn_BIE – PsychoPy Task Files

This repository contains the PsychoPy experiment files for the TSRlearn project.  
The task is split into multiple blocks (practice, localizers, main task blocks), each implemented as a separate PsychoPy experiment file.

## Requirements

This task was created using PsychoPy 2025.1.1. I'm not sur eif it works with other psychopy versions.

## Running the Task

Paths to stimuli and sequence files are defined relative to the project structure.  
The task can therefore be run without changing any path settings.

When the task is run:
- A new folder called `data/` will be created automatically
- All behavioural output files (e.g. `.csv`, `.tsv`) will be stored there

Language can be changed in the first routine of each task block.

- In a code component named `exp_settings`, a variable controls language selection
- The language must be provided as a string: for example "english" or "german"
