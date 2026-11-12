---
title: "Set and Get Paths of Interface Files Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_and_Get_Paths_of_Interface_Files_Example_VBA.htm"
---

# Set and Get Paths of Interface Files Example (VBA)

This example shows how to set and get the paths of interface files.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5. Run the macro.
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Sets different alias, custom icon, customization, and
'    menu file paths.
' 3. Gets different alias, custom icon, customization, and
'    menu file paths. Click OK to close each message box.
'
' NOTE: To verify, you can also click Tools > Options >
' File Locations and expand Interface. Then expand and
' examine Alias File Location, Custom Icon Location,
' Customization File, and Menu Files.
'--------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    If dsApp Is Nothing Then
         Return
    End If
```

```
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    Dim dsInterfaceFiles As DraftSight.InterfaceFiles
    If dsInterfaceFiles Is Nothing Then
        MsgBox "There are no valid interface files."
        Exit Sub
    End If
```

```
    'Set and get different file paths
    dsInterfaceFiles.AliasFilePath = "C:\Program Files\Dassault Systemes\DraftSight\Default Files\Alias"
    dsInterfaceFiles.AliasFilePath = ""
    dsInterfaceFiles.CustomizationFilePath = ""
    dsInterfaceFiles.MenuFilesPath = "C:\Program Files\Dassault Systemes\DraftSight\Default Files\StartupMenu\english"
```

```
    MsgBox "Alias file path: " & dsInterfaceFiles.AliasFilePath
    MsgBox "Custom icon path: " & dsInterfaceFiles.CustomIconPath
    MsgBox "Customization file path: " & dsInterfaceFiles.CustomizationFilePath
    MsgBox "Menu files path: " & dsInterfaceFiles.MenuFilesPath
```

```
End Sub
```
