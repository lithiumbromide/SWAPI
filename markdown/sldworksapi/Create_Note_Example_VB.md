---
title: "Create Note Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Note_Example_VB.htm"
---

# Create Note Example (VBA)

This example shows how to compose a two-line note and insert the note on the current drawing sheet.

```
'---------------------------------------------
' Preconditions: Open a drawing.
'
' Postconditions:
' 1. Verifies that a drawing is open.
' 2. Composes and inserts a note on the
'    drawing sheet.
' 3. Examine the graphics area.
'---------------------------------------------
Option Explicit
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim str As String
```

```
    ' Constant enumerators
    Const swDocPART = 1
    Const swDocASSEMBLY = 2
    Const swDocDRAWING = 3
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then
        ' If no model currently loaded, then exit
        Exit Sub
    End If
```

```
    ' Determine the document type
    ' If the document is not a drawing, then send a message to the user
    If (swModel.GetType <> swDocDRAWING) Then
        swApp.SendMsgToUser ("Macro only used for drawings")
        Exit Sub
    End If
```

```
    ' Compose text string with carriage return
    str = "Fred and " + Chr(10) + "Ethel"
```

```
    ' Insert note at (.09,.08) on the sheet
    swModel.CreateText str, 0.09, 0.08, 0, 0.01, 0
```

```
End Sub
```
