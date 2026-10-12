---
title: "Standard Task Add-in"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/StandardTaskAddIn.htm"
---

# Standard Task Add-in

You can write your own [task](Tasks.htm) add-in using SOLIDWORKS PDM Professional API's methods and interfaces. Doing so gives you full control over what the task should do.

However, if you simply want a task to open files in SOLIDWORKS and run VBScripts on them, then you can reuse the standard task add-in shipped with SOLIDWORKS PDM Professional.

The standard task add-in provides two tasks:

- Printing files using SOLIDWORKS.
- Converting SOLIDWORKS files to other file formats.

Additionally you can modify the standard task add-in to execute any script.

1. Make sure that the add-in, SWTaskAddIn, is installed in the vault.
2. Start the Administration tool, right-click **Tasks** in the tree, and select **New Task**.
3. Select the SWTaskAddIn add-in in the first page of the dialog box.
4. Go to the Script page and edit the code in the main function.
  The **Insert Macro** button makes it possible to insert macros that will be replaced with data from SOLIDWORKS PDM Professional when the script is executed. Read more about macros in the following section.
5. Set all other tasks settings, such as computer on which to execute, notifications, etc.

### Macros

The macros in the Insert Macro menu work inconsistently. Keep in mind:

| Menu Option | Macro | Note |
| --- | --- | --- |
| Source File Name | <Filename> | This option is added as the literal string "<Filename>" to the script. The script has to scan for the string and replace it with the real file name. |
| Source File Extension | <Extension> | This option works like <Filename> in the sense that the macro is not resolved. |
| Configuration Name | <Configuration> | This option works like <Filename> in the sense that the macro is not resolved. |
| Source Folder Path | <Path> | This macro will be replaced with the file system path to the parent folder of the source file. Add double quotes around "<Path>" to use it as a string. Example: C:\MyVault\Drawings\ |
| Vault Root Folder Path | <VaultPath> | Resolves to the root folder of the vault. For instance: C:\MyVault\ |
| Task Instance GUID | <TaskInstanceGuid> | A GUID (Globally Unique Identifier) that identifies the task instance. |
| Source File Path | <Filepath> | Resolves to the full path to the source file. Example: C:\MyVault\Drawings\Part.sldprt |

You can create an input card using the card editor to provide a user interface when the task is launched. The data entered in the card can then be used in the script. Refer to a card variable value in the script by enclosing it with { }, for example {Description}, to insert a value from variable, Description.

It is a good idea to have a look at the scripts for printing and converting, which are shipped with SOLIDWORKS PDM Professional, for hints on how to write scripts. The SOLIDWORKS PDM Professional Help contains additional information about the Administration tool and using the standard task add-in.

### See Also

[Task Add-in Sample](TaskSample.htm)

[Task Add-in Sample (C#)](TaskSample_CSharp.htm)
