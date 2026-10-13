---
title: "Fire Assembly Rebuild Events Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Regen_Post_Notify2_Event_Handler_Example_CSharp.htm"
---

# Fire Assembly Rebuild Events Example (C#)

This example shows how to handle pre-notification and post-notification events for an assembly, which are fired when the assembly is rebuilt.

```
// ----------------------------------------------------------------------------
// Preconditions:
//  1. Verify that the specified assembly document to open exists.
//  2. Open the Immediate window.
//
// Postconditions:
//  1. Opens the specified assembly document.
//  2. Inserts a cut-extrude assembly feature.
//  3. Pops up a dialog with the rebuild pre-notification.
//  4. Click OK to close the dialog.
//  5. Rebuilds the assembly.
//  6. Pops up a dialog with the rebuild post-notification.
//  7. Click OK to close the dialog.
//  8. Rolls back the rollback bar and pops up a dialog with the
//     rebuild post-notification.
//  9. Click OK to close the dialog.
// 10. Examine the Immediate window and FeatureManager design tree.
// 11. Click Tools > Options > System Options > Stop VSTA debugger on macro exit > OK.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
// ----------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace Macro1.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        public AssemblyDoc swAssembly;
        SketchManager swSketchManager;
        ModelDocExtension swModelDocExt;
        SketchSegment swSketchSegment;
        FeatureManager swFeatureManager;
        Feature swFeature;
        SelectionMgr swSelectionMgr;
        string fileName;
        int errors;
        int warnings;

        public void Main()
        {
            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, false);

            // Open assembly
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\smartcomponents\\stepped_shaft.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref  errors, ref warnings);

            // Insert a cut-extrude assembly feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(-0.016076, -0.532382, 0.0, 0.044465, -0.546417, 0.0);
            swModel.ClearSelection2(true);
            swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.FeatureCut3(true, false, false, 0, 0, 0.00254, 0.00254, false, false, false, false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, true, true, true, true, false, 0, 0, false);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swSelectionMgr.EnableContourSelection = false;
            swModel.ClearSelection2(true);

            // Event notification
            swAssembly = (AssemblyDoc)swModel;
            AttachEventHandlers();

            // Rebuild the model
            swModel.ForceRebuild3(true);

            // Roll back the rollback bar
            swFeatureManager.EditRollback((int)swMoveRollbackBarTo_e.swMoveRollbackBarToBeforeFeature, swFeature.Name);
        }

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {
            swAssembly.RegenNotify += this.swAssembly_RegenNotify;
            swAssembly.RegenPostNotify2 += this.swAssembly_RegenPostNotify2;
        }

        private int swAssembly_RegenNotify()
        {
            // Display message before rebuild
            System.Windows.Forms.MessageBox.Show("A rebuild pre-notification event was fired.");
            return 0;
        }

        private int swAssembly_RegenPostNotify2(object stopFeature)
        {
            // Display message after rebuild
            if ((stopFeature != null))
            {
                Feature feature = default(Feature);
                feature = (Feature)stopFeature;
                Debug.Print("The rollback bar is above " + feature.Name + " in the FeatureManager design tree.");
            }
            System.Windows.Forms.MessageBox.Show("A rebuild post-notification event was fired.");
            return 0;
        }

        public SldWorks swApp;

    }
}
```
