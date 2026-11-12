---
title: "Load and Activate LineStyles Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Load_and_Activate_LineStyles_Example_CSharp.htm"
---

# Load and Activate LineStyles Example (C#)

This example shows how to load and activate LineStyles.

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
// 1. Gets the active document.
// 2. Gets the LineStyle Manager.
// 3. Loads the BATTING and ZIGAG LineStyles.
// 4. Activates and draws a Line for each LineStyle
//    loaded in Step 3.
//----------------------------------------------------------------

using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System;

static class Program
    {

        public static void Main(string[] args)
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            // Abort any command currently running in DraftSight to avoid nested commands
            dsApp.AbortRunningCommand();

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

            //Get LineStyle manager
            LineStyleManager dsLineStyleMgr = dsDoc.GetLineStyleManager();

            //Load LineStyles
            string lineStyleFilePath = System.IO.Path.Combine(
                dsApp.GetSystemFiles().GetUserDataPath(),
                "Linestyles");
            string lineStyleFile = System.IO.Path.Combine(lineStyleFilePath, "MM.LIN");
            LineStyle dsLineStyle = null;
            dsLineStyleMgr.LoadLineStyle("BATTING", lineStyleFile, out dsLineStyle);
            dsLineStyleMgr.LoadLineStyle("ZIGZAG", lineStyleFile, out dsLineStyle);

            //Get Sketch manager
            SketchManager dsSketchMgr = dsDoc.GetModel().GetSketchManager();

            //Activate BATTING LineStyle and insert Line
            dsLineStyle = dsLineStyleMgr.GetLineStyle("BATTING");
            dsLineStyle.Activate();
            dsSketchMgr.InsertLine(0, 0, 0, 100, 100, 0);

            //Activate ZIGZAG LineStyle and insert Line
            dsLineStyle = dsLineStyleMgr.GetLineStyle("ZIGZAG");
            dsLineStyle.Activate();
            dsSketchMgr.InsertLine(100, 0, 0, 200, 100, 0);
        }

    }
```
