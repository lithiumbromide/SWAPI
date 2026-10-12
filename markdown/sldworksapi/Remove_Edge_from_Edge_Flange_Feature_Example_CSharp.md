---
title: "Remove Edge from Edge Flange Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Edge_from_Edge_Flange_Feature_Example_CSharp.htm"
---

# Remove Edge from Edge Flange Feature Example (C#)

This example shows how to remove an edge from an edge flange feature in a sheet metal part.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\SM1-remove-edges.sldprt.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Removes an edge from Edge-Flange1.
// 2. Examine the Immediate window.
//
// NOTE: Because the model is used elsewhere, do not save changes.
// ---------------------------------------------------------------------------
using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;

namespace RemoveEdgesFromEdgeFlange_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swDocument = default(ModelDoc2);
            SelectionMgr swSelectionManager = default(SelectionMgr);
            EdgeFlangeFeatureData swEdgeFlangeData = default(EdgeFlangeFeatureData);
            Feature swFeature = default(Feature);
            int lNumEdges = 0;
            Edge[] aEdgesToRemove = null;
            int lIdx = 0;
            bool bStatus = false;
            int lNumEdgesToRemove = 0;
            object[] vEdgesToRemove = null;
            object[] vEdges = null;
            swEdgeFlangeError_e nStatus = default(swEdgeFlangeError_e);
            ModelDocExtension modDocExt = default(ModelDocExtension);

            swDocument = (ModelDoc2)swApp.ActiveDoc;
            swSelectionManager = (SelectionMgr)swDocument.SelectionManager;

            modDocExt = (ModelDocExtension)swDocument.Extension;
            bStatus = modDocExt.SelectByID2("Edge-Flange1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionManager.GetSelectedObject6(1, 0);

            swEdgeFlangeData = (EdgeFlangeFeatureData)swFeature.GetDefinition();

            swEdgeFlangeData.AccessSelections(swDocument, null);

            vEdges = (object[])swEdgeFlangeData.Edges;
            lNumEdges = vEdges.GetUpperBound(0) - vEdges.GetLowerBound(0) + 1;
            Debug.Print("Number of edges in edge flange = " + swEdgeFlangeData.GetEdgeCount());

            //
            // Specify number of edges to remove
            //
            lNumEdgesToRemove = 1;

            vEdgesToRemove = null;
            aEdgesToRemove = new Edge[lNumEdgesToRemove];

            if ((lNumEdgesToRemove >= 1))
            {
                for (lIdx = 0; lIdx <= (lNumEdgesToRemove - 1); lIdx++)
                {
                    aEdgesToRemove[lIdx] = (Edge)vEdges[lIdx];
                }
                vEdgesToRemove = aEdgesToRemove;
            }

            nStatus = (swEdgeFlangeError_e)swEdgeFlangeData.RemoveEdges(vEdgesToRemove);
            Debug.Print("Edge removal error code = " + swEdgeFlangeError2String(nStatus));

            bStatus = swFeature.ModifyDefinition(swEdgeFlangeData, swDocument, null);
            Debug.Print("Status of modify definition = " + bStatus);

            swEdgeFlangeData.AccessSelections(swDocument, null);
            vEdges = null;
            vEdges = (object[])swEdgeFlangeData.Edges;
            if (((vEdges != null)))
            {
                lNumEdges = vEdges.GetUpperBound(0) - vEdges.GetLowerBound(0) + 1;
                Debug.Print("Number of edges in edge flange = " + lNumEdges);
            }
            else
            {
                Debug.Print("Number of edges in edge flange = 0");
            }

            swEdgeFlangeData.ReleaseSelectionAccess();
        }

        private string swEdgeFlangeError2String(swEdgeFlangeError_e nStatus)
        {
            string functionReturnValue = null;

            switch ((nStatus))
            {
                case 0:
                    functionReturnValue = "no error";
                    break;
                case swEdgeFlangeError_e.swEdgeFlangeError_EdgeAlreadyExists:
                    functionReturnValue = "edge already exists";
                    break;
                case swEdgeFlangeError_e.swEdgeFlangeError_EdgeNotSpecified:
                    functionReturnValue = "edge not specified";
                    break;
                case swEdgeFlangeError_e.swEdgeFlangeError_NumberOfEdgesAndSketchesNotEqual:
                    functionReturnValue = "number mismatch";
                    break;
                case swEdgeFlangeError_e.swEdgeFlangeError_SketchNotSpecified:
                    functionReturnValue = "sketch not specified";
                    break;
                default:
                    functionReturnValue = "unknown error";
                    break;
            }
            return functionReturnValue;

        }

        public SldWorks swApp;

    }

}
```
