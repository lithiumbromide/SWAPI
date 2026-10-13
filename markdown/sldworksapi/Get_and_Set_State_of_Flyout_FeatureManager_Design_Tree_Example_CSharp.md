---
title: "Get and Set the State of the Flyout FeatureManager Design Tree Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_State_of_Flyout_FeatureManager_Design_Tree_Example_CSharp.htm"
---

# Get and Set the State of the Flyout FeatureManager Design Tree Example (C#)

This example shows how to to display, expand, and hide the flyout FeatureManager design tree.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a model document.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Click OK to close each of the three message boxes after examining the
//    graphics area.
// 2. Examine the Immediate window.
// ---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Windows.Forms;

namespace FlyoutFeatureTreeCSharp.csproj
{

    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        ModelDocExtension swModelDocExt;
        int status;

        public void Main()
        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = (int)swModelDocExt.FlyoutFeatureTreeVisibility;

            Debug.Print("-------Flyout state at start-------");
            if (status == (int)swFeatureTreeState_e.swFlyoutFeatureTree_Hidden)
                Debug.Print("FlyoutFeatureTree Hidden");
            if (status == (int)swFeatureTreeState_e.swFlyoutFeatureTree_ShownExpanded)
                Debug.Print("FlyoutFeatureTree Expanded");
            if (status == (int)swFeatureTreeState_e.swFlyoutFeatureTree_ShownUnExpanded)
                Debug.Print("FlyoutFeatureTree UnExpanded");

            swModelDocExt.FlyoutFeatureTreeVisibility = (int)swFeatureTreeState_e.swFlyoutFeatureTree_ShownExpanded;
            status = swModelDocExt.FlyoutFeatureTreeVisibility;
            if (status == (int)swFeatureTreeState_e.swFlyoutFeatureTree_ShownExpanded)
                MessageBox.Show("Flyout state is now swFlyoutFeatureTree_ShownExpanded.");

            swModelDocExt.FlyoutFeatureTreeVisibility = (int)swFeatureTreeState_e.swFlyoutFeatureTree_ShownUnExpanded;
            status = swModelDocExt.FlyoutFeatureTreeVisibility;
            if (status == (int)swFeatureTreeState_e.swFlyoutFeatureTree_ShownUnExpanded)
                MessageBox.Show("Flyout state is now swFlyoutFeatureTree_ShownUnExpanded.");

            swModelDocExt.FlyoutFeatureTreeVisibility = (int)swFeatureTreeState_e.swFlyoutFeatureTree_Hidden;
            status = swModelDocExt.FlyoutFeatureTreeVisibility;
            if (status == (int)swFeatureTreeState_e.swFlyoutFeatureTree_Hidden)
                MessageBox.Show("Flyout state is now swFlyoutFeatureTree_Hidden.");

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;
    }
}
```
