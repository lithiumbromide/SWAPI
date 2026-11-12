---
title: "Get Format of Note Text Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Format_of_Note_Text_Example_VB.htm"
---

# Get Format of Note Text Example (VBA)

This example shows how to find out whether the font style for notes is italic.

```
'---------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets whether the text format for notes
'    is italic.
' 2. Examine the Immediate window.
'---------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swTextFormat As SldWorks.TextFormat
Dim TextFormatObj As Object
Dim retval As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set TextFormatObj = swModel.GetUserPreferenceTextFormat(swDetailingNoteTextFormat)
    Set swTextFormat = TextFormatObj
    retval = swTextFormat.Italic
    Debug.Print retval
```

```
End Sub
```
