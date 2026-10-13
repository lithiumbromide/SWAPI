---
title: "Fire Notifications When Renaming Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notifications_When_Renaming_Components_Example_CSharp.htm"
---

# Fire Notifications When Renaming Components Example (C#)

This example shows how to fire notifications when you:

- are about to rename a component.
- rename a component.

```
//---------------------------------------------------
// Preconditions:
// 1. Verify that these documents exist in public_documents\samples\tutorial\api:
//    * beam_boltconnection.sldasm
//    * beam with holes.sldprt
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Open public_documents\samples\tutorial\api\beam_boltconnection.sldasm.
// 2. Fires pre-notification before appending
//    123 to each assembly component's name.
// 3. Fires notification when appending 123 to
//    each assembly component's name.
// 4. Examine the FeatureManager design tree and the
//    Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do
// not save changes.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Collections;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public AssemblyDoc swAssy;

        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            ConfigurationManager swConfigMgr = default(ConfigurationManager);
            Configuration swConfig = default(Configuration);
            Component2 swRootComp = default(Component2);
            object[] Children = null;
            Component2 swChild = default(Component2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            SelectData swSelData = default(SelectData);
            int ChildCount = 0;
            string oldName = null;
            string newName = null;
            bool bOldSetting = false;
            bool bRet = false;
            int i = 0;
            Hashtable openAssem = default(Hashtable);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;

            // Set up event
            swAssy = (AssemblyDoc)swModel;
            openAssem = new Hashtable();
            AttachEventHandlers();

            swConfigMgr = swModel.ConfigurationManager;
            swConfig = swConfigMgr.ActiveConfiguration;
            swRootComp = swConfig.GetRootComponent3(true);
            bOldSetting = swApp.GetUserPreferenceToggle((int)swUserPreferenceToggle_e.swExtRefUpdateCompNames);
            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swExtRefUpdateCompNames, false);
            Children = (object[])swRootComp.GetChildren();
            ChildCount = Children.Length;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelData = (SelectData)swSelMgr.CreateSelectData();
            for (i = 0; i <= ChildCount - 1; i++)
            {
                swChild = (Component2)Children[i];
                // Changing component name requires component to be selected
                bRet = swChild.Select4(false, swSelData, false);
                oldName = swChild.Name2;
                newName = oldName + " 123";
                swChild.Name2 = newName;
            }
            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swExtRefUpdateCompNames, bOldSetting);

        }

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {
            swAssy.PreRenameItemNotify += this.swAssy_PreRenameItemNotify;
            swAssy.RenameItemNotify += this.swAssy_RenameItemNotify;
        }

        private int swAssy_PreRenameItemNotify(int EntityType, string oldName, string newName)
        {
            Debug.Print("PRE-NOTIFICATION - about to rename component: " + oldName);
            return 0;
        }
        private int swAssy_RenameItemNotify(int EntityType, string oldName, string newName)
        {
            Debug.Print("NOTIFICATION - rename component: " + newName);
            return 0;
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
