---
title: "Get Chamfer Distances Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Chamfer_Distances_Example_CSharp.htm"
---

# Get Chamfer Distances Example (C#)

This example shows how to get the distances associated with the selected chamfer.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document with at least one chamfer feature.
 // 2. Select the chamfer feature.
 // 3. Open the Immediate window.
 //
 // Postconditions: Examine the Immediate window for the
 // chamfer data.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace GetFaceEdgeCount_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
             const double DegPerRad = 57.3;
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             ChamferFeatureData2 swChamfer = default(ChamferFeatureData2);
             Vertex swVertex = default(Vertex);
             object[] vEdgeArr = null;
             object vEdge = null;
             Edge swEdge = default(Edge);
             object[] vFaceArr = null;
             object vFace = null;
             Face2 swFace = default(Face2);
             object[] vLoopArr = null;
             object vLoop = null;
             Loop2 swLoop = default(Loop2);
             object vLoopEdge = null;
             object[] vLoopEdgeArr = null;
             Edge swLoopEdge = default(Edge);
             Entity swEnt = default(Entity);
             SelectData swSelData = default(SelectData);
             int i = 0;
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swSelData = (SelectData)swSelMgr.CreateSelectData();
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swChamfer = (ChamferFeatureData2)swFeat.GetDefinition();

             // Get chamfer information
             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  " + swFeat.Name);
             Debug.Print("    EdgeChamferAngle          = " + swChamfer.EdgeChamferAngle * DegPerRad + " degrees");
             Debug.Print("    EqualDistance             = " + swChamfer.EqualDistance);
             Debug.Print("    EdgeChamferDistance(0)    = " + swChamfer.GetEdgeChamferDistance(0) * 1000.0 + " mm");
             Debug.Print("    EdgeChamferDistance(1)    = " + swChamfer.GetEdgeChamferDistance(1) * 1000.0 + " mm");
             Debug.Print("    VertexChamferDistance(0)  = " + swChamfer.GetVertexChamferDistance(0) * 1000.0 + " mm");
             Debug.Print("    VertexChamferDistance(1)  = " + swChamfer.GetVertexChamferDistance(1) * 1000.0 + " mm");
             Debug.Print("    VertexChamferDistance(2)  = " + swChamfer.GetVertexChamferDistance(2) * 1000.0 + " mm");
             Debug.Print("    KeepFeatures              = " + swChamfer.KeepFeatures);
             Debug.Print("    Number of chamfered faces = " + swChamfer.GetFaceCount());
              Debug.Print("    Number of chamfered edges = " + swChamfer.GetEdgeCount());
             Debug.Print("    Type                      = " + swChamfer.Type);
             // ChamferFeatureData2::Type
             //   1 = Angle-Distance
             //   2 = Distance-Distance
             //   3 = Vertex

             // Roll back to get access to geometric entities
             bRet = swChamfer.AccessSelections(swModel, null);
             Debug.Assert(bRet);

             swVertex = (Vertex)swChamfer.Vertex;

             vEdgeArr = (object[])swChamfer.Edges;
             vFaceArr = (object[])swChamfer.Faces;
             vLoopArr = (object[])swChamfer.Loops;

             if ((swVertex != null))
             {
                 swModel.ClearSelection2(true);
                 swEnt = (Entity)swVertex;
                 bRet = swEnt.Select4(true, swSelData);
                 Debug.Assert(bRet);
             }

             if ((vEdgeArr != null))
             {
                 swModel.ClearSelection2(true);
                 i = 0;
                 bRet = false;
                 foreach (object vEdge_loopVariable in vEdgeArr)
                 {
                     vEdge = vEdge_loopVariable;
                     swEdge = (Edge)vEdge;
                     swEnt = (Entity)swEdge;

                     bRet = swEnt.Select4(true, swSelData);
                     Debug.Assert(bRet);

                     Debug.Print("    EdgeFlip(" + i + ")              = " + swChamfer.GetIsFlipped(swEdge));

                     i = i + 1;
                 }

             }

             if ((vFaceArr != null))
             {
                 swModel.ClearSelection2(true);
                 i = 0;
                 bRet = false;

                 foreach (object vFace_loopVariable in vFaceArr)
                 {
                     vFace = vFace_loopVariable;
                     swFace = (Face2)vFace;
                     swEnt = (Entity)swFace;

                     bRet = swEnt.Select4(true, swSelData);
                     Debug.Assert(bRet);

                     Debug.Print("    FaceFlip(" + i + ")              = " + swChamfer.GetIsFlipped(swFace));

                     i = i + 1;
                 }

             }

             if ((vLoopArr != null))
             {
                 swModel.ClearSelection2(true);
                 i = 0;
                 bRet = false;

                 foreach (object vLoop_loopVariable in vLoopArr)
                 {
                     vLoop = vLoop_loopVariable;
                     swLoop = (Loop2)vLoop;

                     // Cannot select loop-through-entity interface because loop
                     // is topology; instead, get edges (geometry) and select through
                     // entity from edge

                     vLoopEdgeArr = (object[])swLoop.GetEdges();

                     foreach (object vLoopEdge_loopVariable in vLoopEdgeArr)
                     {
                         vLoopEdge = vLoopEdge_loopVariable;
                         swLoopEdge = (Edge)vLoopEdge;
                         swEnt = (Entity)swLoopEdge;

                         bRet = swEnt.Select4(true, swSelData);
                         Debug.Assert(bRet);
                     }

                     Debug.Print("    LoopFlip(" + i + ")              = " + swChamfer.GetIsFlipped(swLoop));
                     i = i + 1;
                 }

             }

             //Cancel changes
             swChamfer.ReleaseSelectionAccess();

         }

         public SldWorks swApp;

     }
 }
```
