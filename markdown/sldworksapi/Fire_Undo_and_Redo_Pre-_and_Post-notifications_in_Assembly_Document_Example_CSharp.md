---
title: "Fire Undo and Redo Pre- and Post-notifications in Assembly Document (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_CSharp.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Assembly Document (C#)

This example shows how to fire Undo and Redo post-notifications in an assembly document.

```vb
//----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
 //
 // 1. Selects  and hides the base-plate<1> component and
 //    fires pre- and post-notifications indicating that an
 //    Undo has occurred.
 // 2. Performs a Redo and fires pre- and post-notifications.
 // 3. Performs another Undo and fires pre- and post-notifications
 //    so that the assembly document returns to its just-opened state.
 // 4. Click OK to close each message box.
 //
 // NOTE: Because the assembly is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;
namespace Macro1.csproj
{
    public partial class SolidWorksMacro
    {
        public AssemblyDoc swAssemblyDoc;
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            bool boolstatus = false;
            Hashtable openAssembly = default(Hashtable);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Event notification
            swAssemblyDoc = (AssemblyDoc)swModel;
            openAssembly = new Hashtable();
            AttachEventHandlers();

            // Select a component and hide it
            boolstatus = swModelDocExt.SelectByID2("base_plate-1@stepped_shaft", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swModel.HideComponent2();
            swModel.ClearSelection2(true);

            // Undo hiding of the component
            // and fire pre- and post-notifications
            swModel.EditUndo2(1);

            // Redo hiding of the component
            // and fire pre- and post-notifications
            swModel.EditRedo2(1);

            // Undo hiding of the component
            // so that the assembly document
            // is unchanged
            swModel.EditUndo2(1);

            // Rebuild model
            swModel.ForceRebuild3(true);
        }
        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }
        public void AttachSWEvents()
        {
            swAssemblyDoc.UndoPostNotify += this.swAssembly_UndoPostNotify;
            swAssemblyDoc.UndoPreNotify += this.swAssembly_UndoPreNotify;
            swAssemblyDoc.RedoPostNotify += this.swAssembly_RedoPostNotify;
            swAssemblyDoc.RedoPreNotify += this.swAssembly_RedoPreNotify;
        }
        public int swAssembly_UndoPostNotify()
        {
            //Display message after undo action occurs
// NOTE: Because the message box may be displayed
// behind an opened window, you might not see it.
// If so, then check the Taskbar for it.
            MessageBox.Show("An Undo post-notification event has been fired.");
            return 1;
        }
        public int swAssembly_UndoPreNotify()
        {
            //Display message after undo action occurs
// NOTE: Because the message box may be displayed
// behind an opened window, you might not see it.
// If so, then check the Taskbar for it.
            MessageBox.Show("An Undo pre-notification event has been fired.");
            return 1;
        }
        public int swAssembly_RedoPostNotify()
        {
            //Display message after undo action occurs
// NOTE: Because the message box may be displayed
// behind an opened window, you might not see it.
// If so, then check the Taskbar for it.
            MessageBox.Show("A Redo post-notification event has been fired.");
            return 1;
        }
        public int swAssembly_RedoPreNotify()
        {
            //Display message after undo action occurs
// NOTE: Because the message box may be displayed
// behind an opened window, you might not see it.
// If so, then check the Taskbar for it.
            MessageBox.Show("A Redo pre-notification event has been fired.");
            return 1;
        }
    }
}
```
