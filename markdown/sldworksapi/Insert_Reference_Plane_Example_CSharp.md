---
title: "Insert Reference Plane Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Reference_Plane_Example_CSharp.htm"
---

# Insert Reference Plane Example (C#)

This example shows how to create a constraint-based angle reference plane.

```
//-----------------------------------------------------------
// 1. Verify that the specified part exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a constraint-based reference plane.
// 2. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not
// save changes.
//-----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
```

```vb
namespace InsertRefPlaneFeatureManagerCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            RefPlane swRefPlane = default(RefPlane);
            SelectionMgr swSelMgr = default(SelectionMgr);
            RefPlaneFeatureData swRefPlaneFeatureData = default(RefPlaneFeatureData);
            int fileerror = 0;
            int filewarning = 0;
            bool boolstatus = false;
            int planeType = 0;

            swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\plate.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref fileerror, ref filewarning);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            // Create a constraint-based reference plane
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.028424218552, 0.07057725774359, 0, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.05976462601598, 0.0718389621656, 0.0001242036435087, true, 1, null, 0);
            swRefPlane = (RefPlane)swFeatureManager.InsertRefPlane(16, 0.7853981633975, 4, 0, 0, 0);

            // Get type of the just-created reference plane
            boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swRefPlaneFeatureData = (RefPlaneFeatureData)swFeature.GetDefinition();

            planeType = swRefPlaneFeatureData.Type2;
            Debug.Print("Type of reference plane using IRefPlaneFeatureData::Type2: ");
            switch (planeType)
            {
                case 0:
                    Debug.Print(" Invalid");
                    break;
                case 1:
                    Debug.Print(" Undefined");
                    break;
                case 2:
                    Debug.Print(" Line Point");
                    break;
                case 3:
                    Debug.Print(" Three Points");
                    break;
                case 4:
                    Debug.Print(" Line Line");
                    break;
                case 5:
                    Debug.Print(" Distance");
                    break;
                case 6:
                    Debug.Print(" Parallel");
                    break;
                case 7:
                    Debug.Print(" Angle");
                    break;
                case 8:
                    Debug.Print(" Normal");
                    break;
                case 9:
                    Debug.Print(" On Surface");
                    break;
                case 10:
                    Debug.Print(" Standard");
                    break;
                case 11:
                    Debug.Print(" Constraint-based");
                    break;
            }
            Debug.Print("");

            planeType = swRefPlaneFeatureData.Type;
            Debug.Print("Type of reference plane using IRefPlaneFeatureData::Type: ");
            switch (planeType)
            {
                case 0:
                    Debug.Print(" Invalid");
                    break;
                case 1:
                    Debug.Print(" Undefined");
                    break;
                case 2:
                    Debug.Print(" Line Point");
                    break;
                case 3:
                    Debug.Print(" Three Points");
                    break;
                case 4:
                    Debug.Print(" Line Line");
                    break;
                case 5:
                    Debug.Print(" Distance");
                    break;
                case 6:
                    Debug.Print(" Parallel");
                    break;
                case 7:
                    Debug.Print(" Angle");
                    break;
                case 8:
                    Debug.Print(" Normal");
                    break;
                case 9:
                    Debug.Print(" On Surface");
                    break;
                case 10:
                    Debug.Print(" Standard");
                    break;
                case 11:
                    Debug.Print(" Constraint-based");
                    break;
            }
            Debug.Print("");

            swModel.ClearSelection2(true);
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
