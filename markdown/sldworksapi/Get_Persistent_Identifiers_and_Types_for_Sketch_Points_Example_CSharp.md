---
title: "Get Persistent Identifiers and Types for Sketch Points Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Persistent_Identifiers_and_Types_for_Sketch_Points_Example_CSharp.htm"
---

# Get Persistent Identifiers and Types for Sketch Points Example (C#)

This example shows how to get the persistent identifiers and types for sketch points.

**NOTE**: SOLIDWORKS Design allocates a persistent ID for sketch points and segments, accessible by ISketchPoint::GetID. This method allows you to store the identifier and then return to the sketch entity at a later time. There are also sketch points that are not visible to the user. These are typically used internally by SOLIDWORKS Design for various purposes. Sketch points are also created from other operations; for example, creating a spline or adding a midpoint relation. Each sketch point has a read-only property, ISketchPoint::Type, that indicates how it is used in the sketch.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part or assembly.
 // 2. Select a 2D or 3D sketch.
 //
 // Postconditions:
 // 1. Gets the selected sketch's sketch-point IDs and types.
 // 2. Examine the Immediate window.
 //
 // NOTES:
 // * Both SketchPoint::ID and ISketchPoint::Type are read-only.
 // * The identifier is unique to the sketch and may be duplicated
 //   in the model. To unambiguously resolve a sketch entity, you need both
 //   the sketch and the sketch identifier.
 //---------------------------------------------------------------------------

 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;

 namespace Macro1
 {
       partial  class   SolidWorksMacro
      {
           public  void Main()
          {
               ModelDoc2 swModel;
               SelectionMgr swSelMgr;
              Feature swFeat;
               Sketch swSketch;
               object[] vSketchPtArr;
               SketchPoint swSketchPt;
               int[] vID;

              swModel = (ModelDoc2)swApp.ActiveDoc;
              swSelMgr = (SelectionMgr)swModel.SelectionManager;
              swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
              swSketch = (Sketch)swFeat.GetSpecificFeature();

               Debug.Print("File = " + swModel.GetPathName());
               Debug.Print("  " + swFeat.Name);

              vSketchPtArr = (object[])swSketch.GetSketchPoints();

               foreach (var vSketchPt   in vSketchPtArr)
              {
                  swSketchPt = (SketchPoint)vSketchPt;
                  vID = (int[])swSketchPt.GetID();
                   Debug.Print("    Pt [" + vID[0] +   ", " + vID[1] +   "]  = (" + swSketchPt.X * 1000.0 +   ", " + swSketchPt.Y * 1000.0 +  ", " + swSketchPt.Z * 1000.0 +   ") mm");
                   Debug.Print("      Type = " + swSketchPt.Type);
              }
          }

           public  SldWorks swApp;
      }

 }
```
