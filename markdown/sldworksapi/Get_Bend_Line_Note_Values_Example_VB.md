---
title: "Get Bend Line Note Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bend_Line_Note_Values_Example_VB.htm"
---

# Get Bend Line Note Values Example (VBA)

This example shows how to get bend line note values.

```vb
'------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document containing views of a sheet metal
 '    flat pattern configuration with bend line notes.
 ' 2. Select a bend line note.
 '
 ' Postconditions: Prints the bend line note value to the
 ' the Immediate window.
 '-------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swNote As SldWorks.Note
Dim startMathPoint As SldWorks.MathPoint
Dim endMathPoint As SldWorks.MathPoint
Dim UpOrDown As Boolean
Dim Angle As Double
Dim Radius As Double
Dim IsBendNote As Boolean

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager

Set swNote = swSelMgr.GetSelectedObject6(1, -1)

IsBendNote = swNote.GetBendLineValues(UpOrDown, Angle, Radius, startMathPoint, endMathPoint)

Debug.Print "Up (True) or Down (False): " & UpOrDown
' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
Debug.Print "Angle: " & Angle * 57.3 & " degrees"
Debug.Print "Radius: " & Radius * 1000#; 0 & " mm"
```

```vb
End Sub
```
