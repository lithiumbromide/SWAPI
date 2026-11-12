---
title: "Fire Undo and Redo Pre- and Post-notifications in Part Document (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Part_Document_Example_CSharp.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Part Document (C#)

This example shows how to fire Undo and Redo pre- and post-notifications in a part document.

```vb
// --------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 //
 // Postconditions:
 // 1. Creates a circle, undoes it, redoes it, and undoes it again.
 // 2. Fires a pre- and post-notification and displays a message box
 //    before and after each Undo and Redo.
 // 3. Click OK to close each message box.
 //
 // NOTE: Because the part is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;
namespace RedoPostNotifyPartCSharp.csproj
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
            bool boolstatus = false;
            Hashtable openPart;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            // Set up event notification
            swPart = (PartDoc)swModel;
            openPart = new Hashtable();
            AttachEventHandlers();

            // Create a circle on the
            // top face of the candlestick
            swModelDocExt = swModel.Extension;
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, false, 0, null, 0);
            swSketchManager = swModel.SketchManager;
            swSketchSegment = swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.01296, -0.006347, 0.0);
            swModel.ClearSelection2(true);

            // Undo creation of circle
            // and fire an Undo pre- and post-
            // notification
            swModel.EditUndo2(1);

            // Redo creation of circle
            // and fire a Redo pre- and post-
            // notification
            swModel.EditRedo2(1);

            // Undo creation of circle again
            // to leave model document unchanged
            // and fire another Undo pre- and post-
            // notification
            swModel.EditUndo2(1);

            swModel.ClearSelection2(true);
            swModel.ForceRebuild3(true);
        }
        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }
        public void AttachSWEvents()
        {
            swPart.UndoPostNotify += this.swPart_UndoPostNotify;
            swPart.UndoPreNotify += this.swPart_UndoPreNotify;
            swPart.RedoPostNotify += this.swPart_RedoPostNotify;
            swPart.RedoPreNotify += this.swPart_RedoPreNotify;
        }
        public int swPart_UndoPostNotify()
        {
            // Show message after an Undo
            // Display message after Undo
            // NOTE: Because the message box may be displayed
            // behind an opened window, you might not see it.
            // If so, then check the Taskbar for it.
            MessageBox.Show("An Undo post-notification event has been fired.");
            return 1;
        }
        public int swPart_UndoPreNotify()
        {
            // Show message after an Undo
            // Display message after Undo
            // NOTE: Because the message box may be displayed
            // behind an opened window, you might not see it.
            // If so, then check the Taskbar for it.
            MessageBox.Show("An Undo pre-notification event has been fired.");
            return 1;
        }
        public int swPart_RedoPostNotify()
        {
            // Show message after an Undo
            // Display message after Undo
            // NOTE: Because the message box may be displayed
            // behind an opened window, you might not see it.
            // If so, then check the Taskbar for it.
            MessageBox.Show("A Redo post-notification event has been fired.");
            return 1;
        }
        public int swPart_RedoPreNotify()
        {
            // Show message after an Undo
            // Display message after Undo
            // NOTE: Because the message box may be displayed
            // behind an opened window, you might not see it.
            // If so, then check the Taskbar for it.
            MessageBox.Show("A Redo pre-notification event has been fired.");
            return 1;
        }
        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
