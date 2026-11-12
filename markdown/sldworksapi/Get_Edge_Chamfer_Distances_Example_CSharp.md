---
title: "Get Edge Chamfer Distances Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Chamfer_Distances_Example_CSharp.htm"
---

# Get Edge Chamfer Distances Example (C#)

This example shows how to get the distances of the edges and vertices for the chamfer feature.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the part document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Creates a chamfer feature.
// 3. Examine the Immediate window for the chamfer data.
//
// NOTE: Because this part document is used elsewhere, do not
// save any changes.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace IChamferFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            //1 radian = 180º/p = 57.295779513º or approximately 57.3º
            const double DegPerRad = 57.3;
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Feature swFeat = default(Feature);
            FeatureManager swFeatMgr = default(FeatureManager);
            SelectionMgr swSelMgr = default(SelectionMgr);
            ChamferFeatureData2 swChamfer = default(ChamferFeatureData2);
            object[] vEdgeArr;
            object vEdge = null;
            Edge swEdge = default(Edge);
            Entity swEnt = default(Entity);
            SelectData swSelData = default(SelectData);
            int i = 0;
            bool bRet = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block20.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Create and select chamfer feature
            bRet = swModelDocExt.SelectByID2("", "EDGE", -0.0621980171204655, 0.0394066118978458, -0.000546079442074188, true, 0, null, 0);
            bRet = swModelDocExt.SelectByID2("", "EDGE", -0.0381606508724985, 0.0396345009388028, 0.0493384681956286, true, 0, null, 1);
            swFeatMgr = (FeatureManager)swModel.FeatureManager;
            swFeat = (Feature)swFeatMgr.InsertFeatureChamfer(4, 1, 0.00254, 0.78539816339745, 0, 0, 0, 0);
            bRet = swModelDocExt.SelectByID2("Chamfer1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelData = (SelectData)swSelMgr.CreateSelectData();
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swChamfer = (ChamferFeatureData2)swFeat.GetDefinition();

            //Get chamfer information
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
            Debug.Print("    GetFaceCount              = " + swChamfer.GetFaceCount());
            Debug.Print("    GetEdgeCount              = " + swChamfer.GetEdgeCount());
            Debug.Print("    Type                      = " + swChamfer.Type);
            // ChamferFeatureData2::Type
            //   1 = Angle-Distance
            //   2 = Distance-Distance
            //   3 = Vertex
            //Roll back to get access to geometric entities
            bRet = swChamfer.AccessSelections(swModel, null);
            Debug.Assert(bRet);
            vEdgeArr = (object[])swChamfer.Edges;

            if ((vEdgeArr != null))
            {
                swModel.ClearSelection2(true);
                i = 0;
                bRet = false;
                foreach (object vEdge_loopVariable in vEdgeArr)
                {
                    vEdge = (object)vEdge_loopVariable;
                    swEdge = (Edge)vEdge;
                    swEnt = (Entity)swEdge;
                    bRet = swEnt.Select4(true, swSelData);
                    Debug.Assert(bRet);
                    Debug.Print("    EdgeFlip(" + i + ")              = " + swChamfer.GetIsFlipped(swEdge));
                    i = i + 1;
                }
            }

            //Roll forward
            swChamfer.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
