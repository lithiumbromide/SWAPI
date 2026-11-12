---
title: "Add Spotlight and Get Light Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Spotlight_and_Get_Light_Feature_Example_CSharp.htm"
---

# Add Spotlight and Get Light Feature Example (C#)

This example shows how to add a spotlight to a model and get its light feature.

```
//-------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Adds a spotlight.
// 3. Gets the spotlight's feature and prints its ID to
//    the Immediate window.
// 4. Examine the Immediate window, FeatureManager design tree, and
//    graphics area.
//
// NOTE: Because this assembly document is used elsewhere, do not save changes.
//---------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace LightCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            ModelView swModelView = default(ModelView);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            Light swLight = default(Light);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            int[] rect = null;

            //Open assembly
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\appearances\\usb_flash_drive1.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Add spotlight
            status = swModel.AddLightSource("SW#5", 2, "Spot1");
            status = swModel.SetLightSourcePropertyValuesVB("SW#5", 2, 0.5, 8454143, 1, -0.0999999999999991, 0.170000000000101, 1.10999999999999, 0.179999999999999, -0.0900000000001008,
            -1.02999999999999, 45, 0, 0, 0, 0.4, 0.4, 0, false);
            status = swModel.LockLightToModel(4, true);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.GraphicsRedraw(rect);

            //Get spotlight's feature ID
            swModelDocExt = swModel.Extension;
            status = swModelDocExt.SelectByID2("Spot1", "LIGHTS", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swLight = (Light)swFeature.GetSpecificFeature2();
            Debug.Print("Light ID: " + swLight.GetID());

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
