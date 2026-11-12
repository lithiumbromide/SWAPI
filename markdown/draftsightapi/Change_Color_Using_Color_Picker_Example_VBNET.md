---
title: "Change Color Using Color Picker Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Change_Color_Using_Color_Picker_Example_VBNET.htm"
---

# Change Color Using Color Picker Example (VB.NET)

This example shows how to change the Color of a Line using the color picker.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this code into the VB.NET project.
' 3. Add a reference to
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add a reference to System.Windows.Forms.
' 5. Start DraftSight.
' 6. Press F5.
'
' Postconditions:
' 1. Gets the active document.
' 2. Constructs a Line.
' 3. Gets the Color of the Line.
' 4. Opens the color picker.
' 5. Select a Color in the color picker and click OK.
' 6. Sets the Color of the Line to the Color that you selected
'    in the color picker.
'----------------------------------------------------------------

Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()
        Dim dsApp As DraftSight.Interop.dsAutomation.Application
        Dim dsDoc As Document = Nothing
        Dim dsColorPicker As ColorPicker = Nothing
        Dim dsSketchMgr As SketchManager = Nothing
        Dim dsLine As Line = Nothing
        Dim dsColor As Color = Nothing
        Dim OnlyColorBoxIndex As Boolean = True
        Dim EnableByBlockAndLayer As Boolean = True

        'Connects to DraftSight
        dsApp = GetObject(, "DraftSight.Application")

        'Aborts any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        'Gets active document
        dsDoc = dsApp.GetActiveDocument()

        'Gets the Sketch Manager
        dsSketchMgr = dsDoc.GetModel().GetSketchManager()

        'Constructs a Line
        Dim StartX As Double = 0, StartY As Double = 0, StartZ As Double = 0
        Dim EndX As Double = 23.6, EndY As Double = 12.545, EndZ As Double = 0
        dsLine = dsSketchMgr.InsertLine(StartX, StartY, StartZ, EndX, EndY, EndZ)

        'Gets Color of Line
        dsColor = dsLine.Color

        'Creates an instance of the color picker
        dsColorPicker = dsApp.CreateColorPicker(OnlyColorBoxIndex, EnableByBlockAndLayer)

        'Sets Color to the color picker
        dsColorPicker.SetColor(dsColor)

        'Opens the color picker
        dsColorPicker.Execute()

        'Select a Color in the color picker
        'Click OK

        'Gets Color from  color picker
        dsColor = dsColorPicker.GetColor()

        'Sets Color of the Line to Color selected in color picker
        dsLine.Color = dsColor
```

```
    End Sub
```

```
End Module
```
