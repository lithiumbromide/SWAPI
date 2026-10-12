---
title: "Fire Notification When Component Referenced Display State Changes Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Component_Referenced_Display_State_Changes_Example_CSharp.htm"
---

# Fire Notification When Component Referenced Display State Changes Example (C#)

This example shows how to fire a notification when a component's referenced display state is changed in an assembly.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document that has
//    a component with multiple referenced
//    display states.
// 2. Make sure that Tools > Options > Stop VSTA
//    debugger on macro exit is not selected.
// 3. Run this macro (press F5).
// 4. Change the referenced display state of
//    a component (right-click the component, click the
//    Component Properties button, select a different
//    referenced display state, and click OK).
//
// Postconditions:
// 1. Displays a message box informing you that the referenced
//    display state of a component has changed. Check the
//    taskbar for the message box.
// 2. Click OK to close the message box.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;

namespace Macro1.csproj
{
    public partial class SolidWorksMacro
    {
        public AssemblyDoc swAssem;
        public void Main()
        {
            ModelDoc2 swModel;
            Hashtable openAssem;
            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Set up events
            swAssem = (AssemblyDoc)swModel;
            openAssem = new Hashtable();
            AttachEventHandlers();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {
            swAssem.ComponentReferredDisplayStateChangeNotify += this.swAssem_ComponentReferredDisplayStateChangeNotify;
        }

        public int swAssem_ComponentReferredDisplayStateChangeNotify(object componentModel, string compName, int oldDSId, string oldDSName, int newDSId, string newDSName)
        //Send message when user changes referenced display state of a component
        {
            MessageBox.Show("A component's referenced display state has changed.");
            return 1;
        }

    }
}
```
