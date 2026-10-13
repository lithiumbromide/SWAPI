---
title: "Create Intersect Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Intersect_Feature_Example_CSharp.htm"
---

# Create Intersect Feature Example (C#)

This example shows how to create an intersect feature that includes only the internal (hollow) regions between the intersecting regions.

```
//----------------------------------------------------
// Preconditions: Verify that the specified part exists.
//
// Postconditions:
// 1. Opens the specified part.
// 2. Selects Shell1 and Plane6.
// 3. Creates Intersect1 feature.
// 4. Examine the FeatureManager design tree.
//
// NOTE: Because the part is used elsewhere, do not save
// changes.
//----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureMgr = default(FeatureManager);
            Feature swFeature = default(Feature);
            object[] bodyArray = null;
            bool[] bodyExcludeArray = null;
            object excludeArray = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            int nbrBodies = 0;
            int i = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\whatsnew\\parts\\pot.SLDPRT";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;

            //Select features for intersect feature
            status = swModelDocExt.SelectByID2("Shell1", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Plane6", "PLANE", 0, 0, 0, true, 0, null, 0);

            // Create intersect feature
            // * Do not cap planar surface openings of intersect feature
            // * Create internal regions
            bodyArray = (object[])swFeatureMgr.PreIntersect2(false, 1);
            swModel.ClearSelection2(true);

            nbrBodies = bodyArray.GetUpperBound(0);
            bodyExcludeArray = new bool[nbrBodies + 1];
            for (i = 0; i <= nbrBodies; i++)
            {
                bodyExcludeArray[i] = false;
            }
            excludeArray = bodyExcludeArray;
            swFeature = swFeatureMgr.PostIntersect(excludeArray, true, false);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
