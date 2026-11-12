---
title: "Change DimensionStyle Options of Leader Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Change_DimensionStyle_Options_of_Leader_Example_CSharp.htm"
---

# Change DimensionStyle Options of Leader Example (C#)

This example shows how to change the DimensionStyle arrow and text options of a specific Leader. The DimensionStyle arrow and text options of all other existing and new Leaders use the DimensionStyle options of the drawing.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Start debugging the project.
//
// Postconditions:
// 1.  Draws two Leaders, DSUserData and DS.
// 2.  Gets DimensionStyleUserData for DSUserData Leader.
// 3.  Gets arrow options for DSUserData Leader.
// 4.  Modifies DSUserData Leader's arrow options only.
// 5.  Zooms to fit the drawing and execution stops.
// 6.  Examine the drawing to verify that only DSUserData Leader's
//     arrow changed.
// 7.  Press F10 to step through the rest of the project
//     and examine the drawing after each call.
// 8.  Gets text options for DSUserData Leader.
// 9.  Modifies DSUserData Leader's text options only.
// 10. Inserts third Leader, DS2.
// 11. Examine the drawing to verify that DS and DS2 Leaders
//     have the same arrow and text options.
//----------------------------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace DimensionStyleUserDataTest
{
    class Program
    {

        static void Main()
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            if (null == dsApp)
            {
                return;
            }

            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Get Sketch Manager
            Model dsModel;
            SketchManager dsSketchMgr;
            dsModel = dsDoc.GetModel();
            dsSketchMgr= dsModel.GetSketchManager();

            //Insert first Leader
            double[] Coordinates = new double[] { 0, 0, 0, 4, 4, 0, 10, 4, 0 };
            double Width = 5.0;
            string myNote = "DSUserData";
            Leader dsLeader;
            dsLeader = dsSketchMgr.InsertLeader(Coordinates, Width, myNote);

            //Insert second Leader
            double[] Coordinates2 = new double[] { 8, 8, 8, 8, 8, 8, 20, 8, 8 };
            string myNote2 = "DS";
            Leader dsLeader2;
            dsLeader2 = dsSketchMgr.InsertLeader(Coordinates2, Width, myNote2);

            //Get DimensionStyleUserData for DSUserData Leader
            DimensionStyleUserData dsDimStyleUserData;
            dsDimStyleUserData = dsLeader.GetDimensionStyleUserData();

            //Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

            //Examine the drawing
            //Press F10 to step through project
            System.Diagnostics.Debugger.Break();

            //Get DimensionStyleArrowsOptions for DSUserData Leader
            DimensionStyleArrowsOptions dsArrowsOptions;
            dsArrowsOptions = dsDimStyleUserData.GetDimensionStyleArrowsOptions();

            //Set arrow size for DSUserData Leader
            dsArrowsOptions.Size = 1.0;

            //set arrow type for DSUserData Leader
            dsArrowsOptions.SetLeaderArrow(dsDimensionArrowType_e.dsDimensionArrowType_Dot, "");

            //Get DimensionStyleTextOptions for DSUserData Leader
            DimensionStyleTextOptions dsTextOptions;
            dsTextOptions = dsDimStyleUserData.GetDimensionStyleTextOptions();

            //Set text vertical position for DSUserData Leader
            dsTextOptions.VerticalPosition= dsDimensionTextVerticalPosition_e.dsDimensionTextVerticalPosition_Centered;

            //Insert third Leader
            double[] Coordinates3 = new double[] { 16, 16, 16, 16, 16, 16, 40, 16, 16 };
            string myNote3 = "DS2";
            Leader dsLeader3;
            dsLeader3 = dsSketchMgr.InsertLeader(Coordinates3, Width, myNote3);

            //Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

            //Examine the drawing to verify that DS and DS2 Leaders
            //have the same arrow and text options

        }
    }
}
```
