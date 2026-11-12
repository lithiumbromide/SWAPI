---
title: "Expand Component in Specified FeatureManager Design Tree Pane Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Expand_Component_in_Specified_FeatureManager_Design_Tree_Pane_Example_CSharp.htm"
---

# Expand Component in Specified FeatureManager Design Tree Pane Example (C#)

This example shows how to expand a component in the specified FeatureManager design tree pane.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm.
// 2. Select speaker_frame<1> in the FeatureManager design
//    tree.
//
// Postconditions:
// 1. Expands the selected component in the top pane of the
//    FeatureManager design tree.
// 2. Examine the top pane of the FeatureManager design tree
//    and the Immediate window.
//
// NOTE: Because this assembly is used elsewhere, do not
// save changes.
//--------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssy = default(AssemblyDoc);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeat = default(Feature);
            Component2 swComp = default(Component2);
            FeatureManager swFeatMgr = default(FeatureManager);
            string featName = null;
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swComp = (Component2)swSelMgr.GetSelectedObjectsComponent4(1, -1);
            swFeat = (Feature)swAssy.FeatureByName("speaker_frame-1");
            swFeat = (Feature)swComp.FeatureByName("Cut-Extrude1");
            featName = swFeat.Name;
            swFeatMgr = (FeatureManager)swModel.FeatureManager;
            status = swFeatMgr.ExpandFeature(swComp, featName, (int)swFeatMgrPane_e.swFeatMgrPaneTop);
            Debug.Print("Selected component expanded in top pane of FeatureManager design tree? " + status);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
