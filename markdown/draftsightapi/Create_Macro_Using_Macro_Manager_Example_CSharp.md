---
title: "Create Macro Using Macro Manager Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Macro_Using_Macro_Manager_Example_CSharp.htm"
---

# Create Macro Using Macro Manager Example (C#)

This example shows how to create a C# macro using the macro manager and C#.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add a reference to System.Windows.Forms.
// 5. Create C:\temp\macros, if this folder does not exist.
// 6. Start DraftSight.
// 7. Press F5.
//
// Postconditions:
// 1. Connects to DraftSight.
// 2. Gets the active document.
// 3. Gets the macro manager.
// 4. Sets the macro language, level of detail, and save path.
// 5. Starts macro recording.
// 6. Creates a Visual Studio 2008 C# project containing the
//    macro at c:\temp\macros\CircleMacroSharp and inserts
//    a Circle and Arc in the drawing.
// 7. Stops macro recording.
// 8. Open a new drawing in DraftSight.
// 9. Open c:\temp\macros\CircleMacroSharp\CircleMacroCSharp.csproj in
//    Visual Studio 2008.
//    a. Expand CircleMacroCSharp, if necessary.
//    b. Expand DSAPIMacros, if necessary.
//    c. Double-click CircleMacroCSharp located below DSAPIMacros, which
//       opens CircleMacroCSharp.cs.
//    d. Click Start Debugging.
//    e. Creates a Circle and Arc in the drawing.
//    f. Click File > Save All and save the solution.
//    g. Close File > Close Solution.
//----------------------------------------------

using System;
using DraftSight.Interop.dsAutomation;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace MacroManagerCSharp
{
    class Program
    {

        public static void Main()
        {
            DraftSight.Interop.dsAutomation.Application dsApp;

            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

            if (null == dsApp)
            {
                return;
            }

            //Abort any command currently running in DraftSight
            //to avoid nested commands
            dsApp.AbortRunningCommand();

            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }

            //Get macro manager
            MacroManager dsMacroManager = dsApp.GetMacroManager();

            //Set macro language
            dsMacroManager.Language = dsMacroLanguage_e.dsMacroLanguage_CSharp;

            //Set macro level of detail
            dsMacroManager.LevelOfDetail = dsMacroLevelOfDetail_e.dsMacroLevelOfDetail_Low;

            //Set save file path
            dsMacroManager.SavePath = "C:\\temp\\macros\\";

            //Start macro recording
            dsMacroManager.StartMacroRecording();

            //Get Sketch Manager
            SketchManager dsSketchMgr = dsDoc.GetModel().GetSketchManager();

            //Insert Circle and Arc
            Circle dsCircle = dsSketchMgr.InsertCircle(2.0, 2.0, 0.0, 4.0);

            CircleArc dsCircleArc = dsSketchMgr.InsertArc(3.0, 3.0, 0.0, 4.0, 1.0, 2.0);

            //Stop macro recoding
            dsMacroManager.StopMacroRecording("CircleMacroCSharp");
        }

    }
}
```
