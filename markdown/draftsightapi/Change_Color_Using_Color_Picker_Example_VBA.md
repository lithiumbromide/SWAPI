---
title: "Change Color Using Color Picker Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Change_Color_Using_Color_Picker_Example_VBA.htm"
---

# Change Color Using Color Picker Example (VBA)

This example shows how to change the Color of a Line using the color picker.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this code into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5. Press F5.
'
' Postconditions:
' 1. Gets the active document.
' 2. Constructs a Line.
' 3. Gets the Color of the Line.
' 4. Opens the color picker.
' 5. Select a Color in the color picker and click OK.
' 6. Sets the Color of the Line to the Color that you selected
'    in the color picker.
'--------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
        Dim dsApp As DraftSight.Application
        Dim dsDoc As DraftSight.Document
        Dim dsColorPicker As DraftSight.ColorPicker
        Dim dsSketchMgr As DraftSight.SketchManager
        Dim dsLine As DraftSight.Line
        Dim dsColor As DraftSight.Color
        Dim OnlyColorBoxIndex As Boolean
        Dim EnableByBlockAndLayer As Boolean
```

```
        'Connects to DraftSight
        Set dsApp = GetObject(, "DraftSight.Application")
```

```
        'Aborts any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Gets active document
        Set dsDoc = dsApp.GetActiveDocument
```

```
        'Gets the Sketch Manager
        Set dsSketchMgr = dsDoc.GetModel.GetSketchManager
```

```
        'Constructs a Line
        Dim StartX As Double
        Dim StartY As Double
        Dim StartZ As Double
        Dim EndX As Double
        Dim EndY As Double
        Dim EndZ As Double
```

```
        StartX = 0
        StartY = 0
        StartZ = 0
        EndX = 23.6
        EndY = 12.545
        EndZ = 0
```

```
        Set dsLine = dsSketchMgr.InsertLine(StartX, StartY, StartZ, EndX, EndY, EndZ)
```

```
        'Gets Color of Line
        Set dsColor = dsLine.Color
```

```
        'Creates an instance of the color picker
        Set dsColorPicker = dsApp.CreateColorPicker(OnlyColorBoxIndex, EnableByBlockAndLayer)
```

```
        'Sets Color to the color picker
        dsColorPicker.SetColor dsColor
```

```
        'Opens the color picker
        dsColorPicker.Execute
```

```
        'Select a Color in the color picker
        'Click OK
```

```
        'Gets Color from  color picker
        Set dsColor = dsColorPicker.GetColor
```

```
        'Sets Color of the Line to Color selected in color picker
        dsLine.Color = dsColor
```

```
End Sub
```
