---
title: "Selective Open Post-Notify Event Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Selective_Open_Post_Notify_Event_Example_CSharp.htm"
---

# Selective Open Post-Notify Event Example (C#)

This example shows how to handle the post-notification event that fires when components are selected for Quick View/Selective Open.

```
//------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly to open
//    exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. If the Large Design Review dialog displays,
//    then click OK to close it.
// 2. When prompted, select the components to open
//    and click Open Selected.
// 3. Click OK to close the message box.
// 4. If prompted to rebuild, then click Rebuild.
// 5. After reading the next message box displayed,
//    click OK to close it.
// 6. Displays only the selected components.
// 7. Inspect the Immediate Window and graphics area.
//
// NOTE: Because the assembly is used elsewhere, do not save
// changes.
//--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
```

```vb
using SolidWorks.Interop.swconst;
using System;
namespace SelectiveOpenPostNotify_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public AssemblyDoc swAssembly;
        public void Main()
        {
            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, false);
            ModelDoc2 swModel = default(ModelDoc2);
            DocumentSpecification swDocSpecification = default(DocumentSpecification);
            swDocSpecification = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bowl and chute.sldasm");
            swDocSpecification.InteractiveComponentSelection = true;
            swDocSpecification.DocumentType = (int)swDocumentTypes_e.swDocASSEMBLY;
            swModel = swApp.OpenDoc7(swDocSpecification);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssembly = (AssemblyDoc)swModel;
            // Set up event
            AttachEventHandlers();
        }
        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }
        public void AttachSWEvents()
        {
            swAssembly.SelectiveOpenPostNotify += this.swAssembly_SelectiveOpenPostNotify;
        }
        public int swAssembly_SelectiveOpenPostNotify(string NewAddedDisplayStateName, ref object SelectedComponentNames)
        {
            System.Windows.Forms.MessageBox.Show("A post-notification event has been fired for the selective open.");
            System.Diagnostics.Debug.Print("New display state name: " + NewAddedDisplayStateName);
            System.Diagnostics.Debug.Print("Selected component names:");
            long i = 0;
            String[] selected;
            selected = (String[])SelectedComponentNames;
            for (i = 0; i <= selected.GetUpperBound(0); i++)
            {
                System.Diagnostics.Debug.Print(" " + selected[i]);
            }
            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, true);
            return 0;
        }
        public SldWorks swApp;
    }
}
```
