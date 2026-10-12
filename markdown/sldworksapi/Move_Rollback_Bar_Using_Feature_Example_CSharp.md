---
title: "Move Rollback Bar Using Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Rollback_Bar_Using_Feature_Example_CSharp.htm"
---

# Move Rollback Bar Using Feature Example (C#)

This example shows how to move the rollback bar above and below a selected feature in a part document.

```
//---------------------------------------
// Preconditions: Verify that the part to open exists.
// 2. Run the macro.
//
// Postconditions:
// 1. Opens the part document.
// 2. Selects the Sweep1 feature.
// 3. Moves the rollback bar to feature above the
//    Sweep1 feature; i.e., the Revolve1 feature.
// 4. Examine the graphics area to verify, then press
//    F5
// 5. Moves the rollback bar to below the Sweep1 feature.
//------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace EditRollbackPartDocCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            PartDoc swPart = default(PartDoc);
            FeatureManager swFeatureMgr = default(FeatureManager);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cstick.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swPart = (PartDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Move rollback bar to above Sweep1
            status = swModelDocExt.SelectByID2("Sweep1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swPart.EditRollback();

            System.Diagnostics.Debugger.Break();
            //Examine graphics area, then press F5
            // Move rollback bar to below Sweep1

            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            status = swFeatureMgr.EditRollback((int)swMoveRollbackBarTo_e.swMoveRollbackBarToBeforeFeature, "");

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
