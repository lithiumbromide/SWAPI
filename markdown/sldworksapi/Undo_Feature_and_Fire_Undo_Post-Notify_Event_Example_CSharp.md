---
title: "Undo Feature and Fire Undo Post-Notify Event Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm"
---

# Undo Feature and Fire Undo Post-Notify Event Example (C#)

This example shows how to fire an undo post-notification in a part.

```vb
 //-----------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 //
 // Postconditions:
 // 1. Creates a cut-extrude feature on the top face of the
 //    candlestick.
 // 2. Undoes the cut-extrude feature and fires an undo post-notification.
 // 3. Click OK to close the message box.
 // 4. Deletes the cut-extrude sketch and all absorbed features.
 //
 // NOTE: Because the part is used elsewhere, do not save changes.
 //-----------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;
namespace UndoPostNotifyCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public PartDoc swPart;
        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            SketchManager swSketchManager;
            SketchSegment swSketchSegment;
            FeatureManager swFeatureManager;
            Feature swFeature;
            bool boolstatus = false;

            Hashtable openPart;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            // Set up event notification
            swPart = (PartDoc)swModel;
            openPart = new Hashtable();
            AttachEventHandlers();

            // Create a cut-extrude feature on the
            // top face of the candlestick
            swModelDocExt = swModel.Extension;
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, false, 0, null, 0);
            swSketchManager = swModel.SketchManager;
            swSketchSegment = swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.01296, -0.006347, 0.0);
            swModel.ClearSelection2(true);
            boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            swFeatureManager = swModel.FeatureManager;
            swFeature = swFeatureManager.FeatureCut(true, false, false, 0, 0, 0.01, 0.01, false, false, false,
            false, 0.01745329251994, 0.01745329251994, false, false, false, false, false, true, true
            );
            swModel.ClearSelection2(true);

            // Undo the cut-extrude feature
            swModel.EditUndo2(1);

            // Fire undo notification

            // Select the circle and delete it
            boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            boolstatus = swModelDocExt.DeleteSelection2((int)swDeleteSelectionOptions_e.swDelete_Absorbed);

            swModel.ForceRebuild3(true);
        }

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {
            swPart.UndoPostNotify += this.swPart_UndoPostNotify;
        }

        public int swPart_UndoPostNotify()
        {
            //Show message after undo action occurs
           // NOTE: Because the message box might be displayed
           // behind an opened window, you might not see it.
           // If so, then check the Taskbar.
            MessageBox.Show("An undo post-notification event has been fired.");
            return 1;
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
