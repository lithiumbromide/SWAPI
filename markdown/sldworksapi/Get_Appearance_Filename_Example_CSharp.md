---
title: "Get Appearance File Name Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Appearance_Filename_Example_CSharp.htm"
---

# Get Appearance File Name Example (C#)

This example shows how to get the file name of the first appearance applied to a model.

```
//----------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified model document exists.
// 2. Verify that the specified materials file exists.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified model document.
// 2. Applies the specified appearance to the selected face.
// 3. Gets the material IDs.
// 4. Gets the file name of the first appearance applied to the model.
// 5. Examine the graphics area and the Immediate window.
//
// NOTE: Because the model is used elsewhere, do not save changes.
//----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace FileNameCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Face2 swFace = default(Face2);
            Configuration swConfiguration = default(Configuration);
            RenderMaterial swRenderMaterial = default(RenderMaterial);
            int nbrRenderMaterials = 0;
            string fileName = null;
            int warnings = 0;
            int errors = 0;
            bool status = false;
            string materialName = null;
            string[] displayStateNames = null;
            int materialID1 = 0;
            int materialID2 = 0;

            //Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cover_plate.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Create material for the appearance
            materialName = "C:\\Program Files\\SolidWorks Corp\\SolidWorks\\data\\graphics\\Materials\\plastic\\low gloss\\blue low gloss plastic.p2m";
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swRenderMaterial = (RenderMaterial)swModelDocExt.CreateRenderMaterial(materialName);

            //Verify that RealView Graphics is set
            Debug.Print("RealView Graphics set? " + swModelDocExt.ViewDisplayRealView);

            //Select a face and add an appearance
            status = swModelDocExt.SelectByID2("", "FACE", 0.0417924256550464, 0.0796803314056547, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFace = (Face2)swSelectionMgr.GetSelectedObject6(1, -1);
            status = swRenderMaterial.AddEntity(swFace);
            Debug.Print("Appearance added to selected face? " + status);

            swModel.ClearSelection2(true);

            //Get the names of display states
            //Add the appearance to all display states
            swConfiguration = (Configuration)swModel.GetActiveConfiguration();
            displayStateNames = (string[])swConfiguration.GetDisplayStates();
            status = swModelDocExt.AddDisplayStateSpecificRenderMaterial(swRenderMaterial, (int)swDisplayStateOpts_e.swAllDisplayState, displayStateNames, out materialID1, out materialID2);
            Debug.Print("Material IDs returned by IModelDocExtension::AddDisplayStateSpecificRenderMaterial: ");
            Debug.Print("  ID1: " + materialID1);
            Debug.Print("  ID2: " + materialID2);

            //Get the number of appearances
            nbrRenderMaterials = swModelDocExt.GetRenderMaterialsCount2((int)swDisplayStateOpts_e.swAllDisplayState, displayStateNames);

            //If one or more appearances are applied to the model,
            //then get the file name of the first appearance applied
            if (nbrRenderMaterials > 0)
            {
                swRenderMaterial.GetMaterialIds(out materialID1, out materialID2);
                Debug.Print("Material IDs returned by IModelDocExtension::GetMaterialIds: ");
                Debug.Print("  ID1: " + materialID1);
                Debug.Print("  ID2: " + materialID2);
                Debug.Print("First appearance's file name: " + swRenderMaterial.FileName);
            }
            else
            {
                Debug.Print("No appearances applied to this model.");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
