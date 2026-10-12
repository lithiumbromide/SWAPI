---
title: "Insert Cosmetic Weld Bead Using Geometric Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_CSharp.htm"
---

# Insert Cosmetic Weld Bead Using Geometric Entities Example (C#)

This example shows how to insert a cosmetic weld bead using geometric entities.

```
//----------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a cosmetic weld bead using the
//    selected geometric entities (i.e., faces).
// 2. To verify, examine the graphics area and
//    expand the Weld Folder and its subfolder
//    in the FeatureManager design tree.
// 3. Examine the Immediate window.
//
// NOTE: Because the part document is used elsewhere,
// do not save any changes to it.
//-----------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace InsertCosmeticWeldBead2CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Feature swFeature = default(Feature);
            SelectionMgr swSelMgr = default(SelectionMgr);
            FeatureManager swFeatureMgr = default(FeatureManager);
            CosmeticWeldBeadFeatureData swCosmeticWeldBeadFeatureData = default(CosmeticWeldBeadFeatureData);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            int entityType = 0;

            //Open model document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\driveworksxpress\\leg.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select the faces
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            //From face
            status = swModelDocExt.SelectByID2("", "FACE", 0.447611268878973, 0.185506718400291, 0.00676112086262037, true, 4, null, 0);
            //To face
            status = swModelDocExt.SelectByID2("", "FACE", 0.567647499089958, 0.0888999999998532, 0.00208831790428121, true, 8, null, 0);

            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            Face2[] weldFromFace = new Face2[1];
            object[] weldFromArray = new object[1];
            weldFromFace[0] = (Face2)swSelMgr.GetSelectedObject6(1, 4);
            weldFromArray = (object[])weldFromFace;

            Face2[] weldToFace = new Face2[1];
            object[] weldToArray = new object[1];
            weldToFace[0] = (Face2)swSelMgr.GetSelectedObject6(1, 8);
            weldToArray = (object[])weldToFace;

            //Create cosmetic weld bead using the selected faces
            object[] weldObjs = new object[2];
            swFeatureMgr = swModel.FeatureManager;
            weldObjs = (object[])swFeatureMgr.InsertCosmeticWeldBead2(0, weldFromArray, weldToArray, 15 / 1000);

            //Get the weld-from and weld-to entities and their types
            status = swModelDocExt.SelectByID2("Weld Bead1", "COSMETIC_WELD", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swCosmeticWeldBeadFeatureData = (CosmeticWeldBeadFeatureData)swFeature.GetDefinition();
            swCosmeticWeldBeadFeatureData.AccessSelections(swModel, null);
            Debug.Print(swFeature.Name);
            weldObjs = (object[])swCosmeticWeldBeadFeatureData.GetEntitiesWeldFrom(out entityType);
            Debug.Print("  Weld-from type: " + entityType);
            weldObjs = (object[])swCosmeticWeldBeadFeatureData.GetEntitiesWeldTo(out entityType);
            Debug.Print("  Weld-to type:   " + entityType);
            swCosmeticWeldBeadFeatureData.ReleaseSelectionAccess();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
