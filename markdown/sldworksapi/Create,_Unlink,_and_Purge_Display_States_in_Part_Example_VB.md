---
title: "Create, Unlink, and Purge Display States in Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VB.htm"
---

# Create, Unlink, and Purge Display States in Part Example (VBA)

This example shows how to create, unlink, and purge display states in a part document.

```
'---------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\multibody\multi-inter.sldprt,
'    whose Default configuration has two display states:
'    * PhotoWorks Display
'    * Display State 1
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates and unlinks Display State 2.
' 2. Attempts to purge any display states identical to
'    Display State 2.
' 3. Closes the part document without saving any changes.
' 4. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swConfig As SldWorks.Configuration
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim boolstatus As Boolean
Dim modelName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Get Default configuration and create a display state
    Set swConfig = swModel.GetConfigurationByName("Default")
    boolstatus = swConfig.CreateDisplayState("Display State 2")
    If boolstatus Then Debug.Print "Display State 2 created."
    swModel.ForceRebuild3 True
```

```
    ' If display is linked, unlink it
    Set swModelDocExt = swModel.Extension
    Debug.Print "Is Display State 2 linked? " & swModelDocExt.LinkedDisplayState
    swModelDocExt.LinkedDisplayState = False
    Debug.Print "Is Display State 2 still linked? " & swModelDocExt.LinkedDisplayState
```

```
    ' Purge any display states identical to Display State 2
    boolstatus = swModelDocExt.PurgeDisplayState
    Debug.Print "Identical display states to Display State 2 purged? " & boolstatus
    swModel.ForceRebuild3 True
```

```
    ' Close the part without saving changes
    modelName = swModel.GetTitle
    swApp.QuitDoc modelName
```

```
End Sub
```
