---
title: "Get View Bounding Box and Position Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_View_Bounding_Box_and_Position_Example_VB.htm"
---

# Get View Bounding Box and Position Example (VBA)

This example shows how to get the bounding box, geometric center, and position lock status of all drawing views in the drawing sheet.

```
'---------------------------------------------------------
' Preconditions:
' 1. Verify that the drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Gets each drawing view's:
'    * x and y coordinates of the geometric center relative
'      to the drawing sheet origin
'    * bounding box
'    * position lock status
' 3. Examine the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save
' changes.
'----------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim outline() As Double
    Dim pos() As Double
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\replaceview.slddrw"
    Set swDraw = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swView = swDraw.GetFirstView
```

```
    Do While Not swView Is Nothing
        outline = swView.GetOutline
        pos = swView.Position
        Debug.Print "View = " + swView.Name
        Debug.Print "  X and Y positions = (" & pos(0) * 1000# & ", " & pos(1) * 1000# & ") mm"
        Debug.Print "  X and Y bounding box minimums = (" & outline(0) * 1000# & ", " & outline(1) * 1000# & ") mm"
        Debug.Print "  X and Y bounding box maximums = (" & outline(2) * 1000# & ", " & outline(3) * 1000# & ") mm"
	Debug.Print "  Position locked? " & swView.PositionLocked
        Set swView = swView.GetNextView
    Loop
```

```
End Sub
```
