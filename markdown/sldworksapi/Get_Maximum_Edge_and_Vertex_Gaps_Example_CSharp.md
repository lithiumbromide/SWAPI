---
title: "Get Maximum Edge and Vertex Gaps Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Maximum_Edge_and_Vertex_Gaps_Example_CSharp.htm"
---

# Get Maximum Edge and Vertex Gaps Example (C#)

This example returns the same data returned by the Tools > Check dialog box when the check boxes, Maximum edge gap and Maximum vertex gap, are selected.

This example shows how to iterate over each edge and vertex in a part to obtain:

* Whether an edge or vertex is:

* tolerant (distance to neighbor is greater than 5.0E-9 mm).

* exact (distance to neighbor is less than or equal to 5.0E-9 mm).

* Gap size (or tolerance) in mm of each edge or vertex.

* Maximum edge and vertex gaps (or tolerances) in mm for the part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\assemblymates\head.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window for tolerance data for all edges
 // and vertexes.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 //----------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace GetMaximumEdgeandVertexGaps_CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            PartDoc swPart = default(PartDoc);
            object[] vBodyArr = null;
            Body2 swBody = default(Body2);
            object[] vEdgeArr = null;
            Edge swEdge = default(Edge);
            object[] vVertexArr = null;
            Vertex swVertex = default(Vertex);
            FaultEntity swFaultEnt = default(FaultEntity);
            bool bRet = false;
            double tol = 0.0;
            Entity swTanEnt = default(Entity);

             swModel = (ModelDoc2)swApp.ActiveDoc;
            swPart = (PartDoc)swModel;
            Debug.Print("File = " + swModel.GetPathName());
            vBodyArr = (Object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, true);
            foreach ( Object vBody in vBodyArr)
            {
                swBody = (Body2)vBody;
                Debug.Print(" Body[" + swBody.GetType() + "] --> " + swBody.GetSelectionId());
                vEdgeArr = (Object[])swBody.GetEdges();
                vVertexArr = (Object[])swBody.GetVertices();
                double maxEdgeGap = 0;
                maxEdgeGap = 0.0;
                foreach (Object vEdge in vEdgeArr)
                {
                    // Find maximum edge gap
                    swEdge = (Edge)vEdge;
                    bRet = swEdge.IsTolerant(out tol);
                    if (maxEdgeGap < tol)
                    {
                        maxEdgeGap = tol;
                    }
                    if ((!(bRet == false)))
                    {
                        Debug.Print("Edge is tolerant: ");
                        Debug.Print(" Tolerance = " + tol);
                        swTanEnt = (Entity)swEdge;
                        bRet = swTanEnt.Select4(true, null);
                    }
                    else
                    {
                        Debug.Print("Edge is exact: Tolerance = " + tol);
                    }
                    swFaultEnt = swEdge.Check;
                }
                Debug.Print("");
                Debug.Print("Maximum edge gap is " + maxEdgeGap);
                Debug.Print("");
                double maxVertexGap = 0;
                maxVertexGap = 0.0;
                foreach (Object vVertex in vVertexArr)
                {
                    // Find maximum vertex gap
                    swVertex = (Vertex)vVertex;
                    bRet = swVertex.IsTolerant(out tol);
                    if (maxVertexGap < tol)
                    {
                        maxVertexGap = tol;
                    }
                    if ((!(bRet == false)))
                    {
                        Debug.Print("Vertex is tolerant: ");
                        Debug.Print(" Tolerance = " + tol);
                        swTanEnt = (Entity)swVertex;
                        bRet = swTanEnt.Select4(true, null);
                    }
                    else
                    {
                        Debug.Print("Vertex is exact: Tolerance = " + tol);
                    }
                }
                Debug.Print("");
                Debug.Print("Maximum vertex gap is " + maxVertexGap);
                Debug.Print("");
            }
        }
        public SldWorks swApp;
    }
}
```
