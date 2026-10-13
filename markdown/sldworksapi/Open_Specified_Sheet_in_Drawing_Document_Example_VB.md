---
title: "Open Specified Sheet in Drawing Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Specified_Sheet_in_Drawing_Document_Example_VB.htm"
---

# Open Specified Sheet in Drawing Document Example (VBA)

This example shows how to open a specific sheet when programmatically opening a drawing document.

```
'------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified sheet in the specified drawing
'    document as view-only.
' 2. Examine the drawing and Immediate window.
'
' NOTE: Because this drawing document is used
' elsewhere, do not save changes.
'------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim sName As String
Dim longstatus As Long, longwarnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Drawing document path and name
    Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw")
    sName = swDocSpecification.FileName
```

```
    ' Sheet name
    swDocSpecification.SheetName = "Sheet2"
    swDocSpecification.DocumentType = swDocDRAWING
    swDocSpecification.ReadOnly = True
    swDocSpecification.Silent = False
```

```
    ' Open the specified sheet in the specified drawing document
    Set swModel = swApp.OpenDoc7(swDocSpecification)
    longstatus = swDocSpecification.Error
    longwarnings = swDocSpecification.Warning
```

```
    Debug.Print "Name of active sheet? " & swDocSpecification.SheetName
    Debug.Print "Drawing read-only? " & swDocSpecification.ReadOnly
```

```
End Sub
```
