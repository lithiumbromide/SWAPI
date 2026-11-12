---
title: "Open File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_File_Example_VB.htm"
---

# Open File Example (VBA)

This example shows how to prompt the user for the name of the file to open. This example also shows how to set up filters by file types.

```
'---------------------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions:
' 1. Displays the File to Attach dialog and lists the file
'    types specified in the filter.
' 2. Examine the Immediate window.
'----------------------------------------------------------
Option Explicit
```

```
Public swApp As SldWorks.SldWorks
Public swModel As SldWorks.ModelDoc2
```

```
Sub main()
```

```
    Dim Filter As String
    Dim fileName As String
    Dim fileConfig As String
    Dim fileDispName As String
    Dim fileDisplayState As String
    Dim fileOptions As Long
```

```
    Set swApp = Application.SldWorks
    ' The Filter string has three filters
    ' associated with it; note the use of
    ' the | character between filters
    Filter = "SOLIDWORKS Files (*.sldprt; *.sldasm; *.slddrw)|*.sldprt;*.sldasm;*.slddrw|Filter name (*.fil)|*.fil|All Files (*.*)|*.*|"
    fileName = swApp.GetOpenFileName2("File to Attach", "", Filter, fileOptions, fileConfig, fileDispName, fileDisplayState)
    Debug.Print fileName
```

```
End Sub
```
