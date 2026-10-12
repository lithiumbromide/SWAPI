---
title: "Convert Curves into 3D Sketches Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Curves_into_3D_Sketches_Example_CSharp.htm"
---

# Convert Curves into 3D Sketches Example (C#)

This example:

- Shows how to convert curves (edges) into 3D sketches.
- Uses IModelDoc2::SketchConvertIsoCurves to extract ISO-parametric (UV) curves from a face or surface. Specifically, this code shows how to extract the curves containing a vertex.

```
//----------------------------------------------------
// Preconditions:
// 1. Open a part or fully resolved assembly.
// 2. Select a face.
// 3. Press the Ctrl key and select a vertex.
//
// Postconditions:
// 1. Generates two 3D sketches:
//    * First 3D sketch is edge of face in V direction
//      from the selected vertex.
//    * Second 3D sketch is edge of face in U direction
//      from the selected vertex.
// 2. Examine the graphics area and FeatureManager design
//    tree.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
```

```
		ModelDoc2 swModel = default(ModelDoc2);
		SelectionMgr swSelMgr = default(SelectionMgr);
		SelectData swSelData = default(SelectData);
		Face2 swFace = default(Face2);
		Vertex swVertex = default(Vertex);
		Entity swFaceEnt = default(Entity);
		Entity swVertexEnt = default(Entity);
		bool bRet = false;

		swModel = swApp.ActiveDoc;

		swSelMgr = swModel.SelectionManager;
		swSelData = swSelMgr.CreateSelectData;
		swFace = swSelMgr.GetSelectedObject6(1, -1);
		swVertex = swSelMgr.GetSelectedObject6(2, -1);

		swFaceEnt = swFace;
		swVertexEnt = swVertex;

		swModel.ClearSelection2(true);

		bRet = swFaceEnt.Select4(true, swSelData);
		bRet = swVertexEnt.Select4(true, swSelData);

		swModel.SketchConvertIsoCurves(100.0, false, true, true);
		swModel.SketchConvertIsoCurves(100.0, true, true, true);
```

```
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
