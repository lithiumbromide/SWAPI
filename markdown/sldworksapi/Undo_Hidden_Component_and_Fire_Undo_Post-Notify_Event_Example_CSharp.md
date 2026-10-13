---
title: "Undo Hidden Component and Fire Undo Post-Notify Event Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm"
---

# Undo Hidden Component and Fire Undo Post-Notify Event Example (C#)

This example shows how to fire an undo post-notification in an assembly document.

```
//--------------------------------------------------------------------------
// Preconditions: Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
//
// Postconditions:
// 1. Selects and hides the base-plate<1> component.
// 2. Undoes the hiding of the base-plate<1> component.
// 3. Fires a post-notification indicating that an undo action occurred.
// 4. Click OK to close the message box.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
```

```vb
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
            swModel.EditUndo2(1);

            // Fire undo post-notiifcation

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
        }

        public int swAssembly_UndoPostNotify()
        {
            //Display message after undo action occurs
            MessageBox.Show("An undo post-notification event has been fired.");
            return 1;
        }
    }

}
```
