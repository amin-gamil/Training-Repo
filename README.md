# Task 7.2 – Linux Commands
For this task, basic Linux commands where implemented on Ubuntu, this README documents the process.

List of operations performed:  
1. Print working directory
2. List contents of a directory
3. Change directory
4. Edit text files
5. Copy/Move files between directories
6. View contents of text files
7. Deleting files/directories.

## Print working directory

The Linux terminal launches with the `/home/ubuntu` (and denoted with the tilde `~` symbol) as the working directory. This is demonstrated using the `pwd` command below.

![alt text](01.png)

## List directory contents

Now, we know where the working directory is, the contents can be viewed using `ls` command.

![alt text](02.png)

## Change working directory

Let's focus on the **Documents** folder, we do so by typing ` cd Documents `.  
Inside **Documents**, ` ls `, reveales a folder named **micro**.  
Changing the directory again using ` cd micro `, then viewing its contents using ` ls `,

![alt text](03.png)

## Editing files
Inside **micro**, a C-code file named `wave.c`  needs some edits.
Using `nano wave.c` open the file using **GNU nano**.

![alt text](04.png)

![alt text](05.png)

To save and exit the the code editor, we press  **Ctrl+X**.

## Creating a new directory

To return to the **Documents** directory, ` cd .. ` automatically moves up one level.  
A new folder **test-dir** is created using ` mkdir test-dir ` and this is confirmed by ` ls ` shows the folder just created.

![alt text](06.png)

## Copying files

The `wave.c` file edited earlier can be copied to the new directory using  
`` cp micro/wave.c test-dir/wave_copy.c ``  
A `_copy` suffix is added to distinguish the new file.  

![alt text](07.png)

Using ` ls test-dir ` shows that the file is indeed copied.

## Creating a new file.

To create a simple text file, the command `touch test.txt` is used.

![alt text](08.png)

Writing text to this file using **GNU nano** by typing ` nano test.txt `  

![alt text](09.png)

Which opens the blank file in the text editor, where a string of text is typed.  

![alt text](10.png)

## Moving files between directories
The `test.txt` file just created needs to be moved to **micro** folder (*i just made this up* 🤷‍♂️).  
Using `cd ..` to change directory to **Documents**, then similarly to copying, the file is moved using  
`` mv test-dir/test.txt micro/text_m.txt ``

![alt text](11.png)

Viewing the contents of **micro** using `ls` shows the file is indeed moved.

![alt text](12.png)

## Viewing text files

To ensure the file was moved without modifications, the contents of the file can be viewed using the `cat` command (short for *concatenate*). 

![alt text](13.png)

## Deleting directories

The **test-dir** folder created earlier has saved its purpose of demonstrating Linux commands, and its time has come.🔪  
The ` rm ` command is used for deleting files, and when used with the `-r` option, it can also delete entire folders/directories.

![alt text](14.png)

Finally, checking contents of **Documents** shows no traces of the **test-dir** folder.