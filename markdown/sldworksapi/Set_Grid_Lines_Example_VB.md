---
title: "Set Grid Lines Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Grid_Lines_Example_VB.htm"
---

# Set Grid Lines Example (VBA)

This example shows how to set the number of minor grid lines between major grid lines in an active sketch.

```
'--------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Open a sketch in the part document.
' 3. If the grid is not displayed in the sketch,
'    click View > Hide/Show > Grid.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number of minor grid lines between
'    the major grid lines.
' 2. Sets the number of minor grid lines between
'    major grid lines to 15.
' 3. Gets the number of minor grid lines between
'    the major grid lines.
' 4. Examine the graphics area and Immediate window.
'--------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim bReturnValue As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Debug.Print "Current minor grid lines between major grid lines: " & swModel.GetUserPreferenceIntegerValue(swGridMinorLinesPerMajor)
    bReturnValue = swModel.SetUserPreferenceIntegerValue(swGridMinorLinesPerMajor, 15)
    Debug.Print "Modified minor grid lines between major grid lines: " & swModel.GetUserPreferenceIntegerValue(swGridMinorLinesPerMajor)
```

```
End Sub
```
