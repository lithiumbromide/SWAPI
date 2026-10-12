---
title: "Create Imported Solid Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Imported_Solid_Body_Example_CSharp.htm"
---

# Create Imported Solid Body Example (C#)

This example shows how to create an imported solid body in the shape of a pyramid.

```
//-----------------------------------------------
// Preconditions:  Verify that the specified part
// document template exists.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Creates a pyramid-shaped, imported, solid body.
//------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace MacroCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            PartDoc swPart = default(PartDoc);
            Body2 swBody = default(Body2);
            double[] nPt = null;
            object vPt = null;
            bool bRet = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2015\\templates\\part.prtdot", 0, 0, 0);
            swPart = (PartDoc)swModel;
            swBody = (Body2)swPart.CreateNewBody();
            // Front
            nPt = new double[9];
            nPt[0] = 0.0;
            nPt[1] = 0.0;
            nPt[2] = 1.0;
            nPt[3] = -1.0;
            nPt[4] = -1.0;
            nPt[5] = 0.0;
            nPt[6] = 1.0;
            nPt[7] = -1.0;
            nPt[8] = 0.0;
            vPt = nPt;
            bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), null);
            // Left
            nPt = new double[9];
            nPt[0] = 0.0;
            nPt[1] = 0.0;
            nPt[2] = 1.0;
            nPt[3] = -1.0;
            nPt[4] = -1.0;
            nPt[5] = 0.0;
            nPt[6] = -1.0;
            nPt[7] = 1.0;
            nPt[8] = 0.0;
            vPt = nPt;
            bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), null);
            // Back
            nPt = new double[9];
            nPt[0] = 0.0;
            nPt[1] = 0.0;
            nPt[2] = 1.0;
            nPt[3] = -1.0;
            nPt[4] = 1.0;
            nPt[5] = 0.0;
            nPt[6] = 1.0;
            nPt[7] = 1.0;
            nPt[8] = 0.0;
            vPt = nPt;
            bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), null);
            // Right
            nPt = new double[9];
            nPt[0] = 0.0;
            nPt[1] = 0.0;
            nPt[2] = 1.0;
            nPt[3] = 1.0;
            nPt[4] = 1.0;
            nPt[5] = 0.0;
            nPt[6] = 1.0;
            nPt[7] = -1.0;
            nPt[8] = 0.0;
            vPt = nPt;
            bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), null);
            // Bottom
            nPt = new double[12];
            nPt[0] = -1.0;
            nPt[1] = -1.0;
            nPt[2] = 0.0;
            nPt[3] = -1.0;
            nPt[4] = 1.0;
            nPt[5] = 0.0;
            nPt[6] = 1.0;
            nPt[7] = 1.0;
            nPt[8] = 0.0;
            nPt[9] = 1.0;
            nPt[10] = -1.0;
            nPt[11] = 0.0;
            vPt = nPt;
            bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), null);

            bRet = swBody.CreateBodyFromSurfaces();

            swModel.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
