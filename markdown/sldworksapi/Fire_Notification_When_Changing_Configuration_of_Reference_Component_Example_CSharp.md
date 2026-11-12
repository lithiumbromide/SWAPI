---
title: "Fire Notification When Changing Configuration of Reference Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Changing_Configuration_of_Reference_Component_Example_CSharp.htm"
---

# Fire Notification When Changing Configuration of Reference Component Example (C#)

This example shows how to fire an event when changing the configuration of a reference component in an assembly.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document that contains at least one
//    subassembly (i.e., reference component) that has
//    multiple configurations.
// 2. Make sure that the Tools > Options > Stop VSTA debugger on macro exit
//    checkbox is not selected.
// 3. Run this macro (press F5).
// 4. Right-click a subassembly and select Configure Component.
// 5. In the Configuration column on the Modify Configurations
//    dialog, select a different configuration and click OK.
//
// Postconditions:
// 1. Displays a message box informing you that the component's
//    configuration is being changed. Check the taskbar for the
//    message box.
// 2. Click OK to close the message box and
//    the Modify Configurations dialog.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Windows.Forms;
using System.Collections;

namespace CompConfigChangeNotifyAssemblyDocCSharp.csproj
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
            swAssem.ComponentConfigurationChangeNotify += this.swAssem_ComponentConfigurationChangeNotify;
        }

        public int swAssem_ComponentConfigurationChangeNotify(string componentName, string oldConfigurationName, string newConfigurationName)
        //Send message when user is changing the configuration of a reference component
        {
            MessageBox.Show("A component's configuration is being changed." + " Component name: " + componentName + ", old configuration name: " + oldConfigurationName + ", and new configuration name: " + newConfigurationName);
            return 1;
        }

    }
}
```
