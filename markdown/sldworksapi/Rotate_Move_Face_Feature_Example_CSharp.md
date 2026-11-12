---
title: "Rotate Move Face Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Move_Face_Feature_Example_CSharp.htm"
---

# Rotate Move Face Feature Example (C#)

This example shows how to rotate (draft) a Move Face feature by changing the XYZ origin and rotation angles.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document that contains a Move Face feature named Move Face1.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Rotates (drafts) the Move Face feature.
 // 2. Examine the Immediate window.
 //----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace RotateMoveFaceFeature_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeat = default(Feature);
            MoveFaceFeatureData swMoveFaceFeatData = default(MoveFaceFeatureData);
            double[] varPara = null;
            double[] newPara = new double[6];
            double[] newVarPara = null;
            bool boolstatus = false;
            double PI = 0;
            long i = 0;
            // Set PI
            PI = 4 * System.Math.Atan(1);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModelDocExt = swModel.Extension;
            // Select, get, and access Move Face feature
            boolstatus = swModelDocExt.SelectByID2("Move Face1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swMoveFaceFeatData = (MoveFaceFeatureData)swFeat.GetDefinition();
            swMoveFaceFeatData.AccessSelections(swModel, null);
            // Get current XYZ origin and rotation angles of Move Face feature
            Debug.Print("Before rotating Move Face feature...");
             // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
            Debug.Print(" Draft angle of Move Face feature: " + swMoveFaceFeatData.Angle * 57.3 + " degrees");
            Debug.Print(" XYZ origin (first 3) and rotation angles (last 3)");
            varPara = (double[])swMoveFaceFeatData.TriadRotationParameters;
            for (i = varPara.GetLowerBound(0); i <= varPara.GetUpperBound(0); i++)
            {
                Debug.Print(" " + (varPara[i]));
            }
            // New XYZ location and rotation angle values
            newPara[0] = 0.0;
            newPara[1] = 0.0;
            newPara[2] = 0.0;
            newPara[3] = 2 * PI / 180;
            // Convert radians to degrees
            newPara[4] = 2 * PI / 180;
            // Convert radians to degrees
            newPara[5] = 0.0;
            newVarPara = newPara;
            // Rotate the Move Face feature
            swMoveFaceFeatData.TriadRotationParameters = newVarPara;
            Debug.Print(" ");
            Debug.Print("After rotating Move Face feature...");
            Debug.Print(" Draft angle of Move Face feature: " + swMoveFaceFeatData.Angle * 57.3 + " degrees");
            Debug.Print(" XYZ origin (first 3) and rotation angles (last 3)");
            newVarPara = (double[])swMoveFaceFeatData.TriadRotationParameters;
            for (i = newVarPara.GetLowerBound(0); i <= newVarPara.GetUpperBound(0); i++)
            {
                Debug.Print(" " + (newVarPara[i]));
            }
            // Modify the Move Face feature
            swFeat.ModifyDefinition(swMoveFaceFeatData, swModel, null);
        }

        public SldWorks swApp;
    }
}
```
