---
title: "Change Color Using Color Picker Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Change_Color_Using_Color_Picker_Example_CSharp.htm"
---

# Change Color Using Color Picker Example (C#)

This example shows how to change the Color of a Line using the color picker.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this code into the C# project.
// 3. Add a reference to
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Start DraftSight.
// 6. Press F5.
//
// Postconditions:
// 1. Gets the active document.
// 2. Constructs a Line.
// 3. Gets the Color of the Line.
// 4. Opens the color picker.
// 5. Select a Color in the color picker and click OK.
// 6. Sets the Color of the Line to the Color that you selected
//    in the color picker.
//----------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace ColorPickerCSharp
{
    class Program
    {
        static void Main()
        {
            DraftSight.Interop.dsAutomation.Application dsApp;
            Document dsDoc = default(Document);
            ColorPicker dsColorPicker = default(ColorPicker);
            SketchManager dsSketchMgr = default(SketchManager);
            Line dsLine = default(Line);
            Color dsColor = default(Color);
            bool OnlyColorBoxIndex = true;
            bool EnableByBlockAndLayer = true;

            //Connects to DraftSight
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            //Aborts any command currently running in DraftSight to avoid nested commands
            dsApp.AbortRunningCommand();

            //Gets active document
            dsDoc = dsApp.GetActiveDocument();

            //Gets the Sketch Manager
            dsSketchMgr = dsDoc.GetModel().GetSketchManager();

            //Constructs a Line
            double StartX = 0, StartY = 0, StartZ = 0;
            double EndX = 23.6, EndY = 12.545, EndZ = 0;
            dsLine = dsSketchMgr.InsertLine(StartX, StartY, StartZ, EndX, EndY, EndZ);

            //Gets Color of Line
            dsColor = dsLine.Color;

            //Creates an instance of the color picker
            dsColorPicker = dsApp.CreateColorPicker(OnlyColorBoxIndex, EnableByBlockAndLayer);

            //Sets Color to the color picker
            dsColorPicker.SetColor(dsColor);

            //Opens the color picker
            dsColorPicker.Execute();

            //Select a Color in the color picker
            //Click OK

            //Gets Color from color picker
            dsColor = dsColorPicker.GetColor();

            //Sets Color of the Line to Color selected in color picker
            dsLine.Color = dsColor;
        }
    }
}
```
