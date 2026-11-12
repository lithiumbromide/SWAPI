---
title: "Create PolygonMesh Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_PolygonMesh_Example_CSharp.htm"
---

# Create PolygonMesh Example (C#)

This example shows how to create a PolygonMesh.

```vb
 //-------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this example into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Start DraftSight and open a document.
 // 6. Open the Immediate window.
 // 7. Click Start Debugging.
 //
 // Postconditions:
 // 1. A PolygonMesh is created and zoomed to fit.
 // 2. All PolygonMesh parameters are printed to the Immediate
 //    window.
 //------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;
 using System.Diagnostics;

 namespace AddPolygonMesh
 {
     class Program
     {
         private static DraftSight.Interop.dsAutomation.Application dsApp;

         static void Main(string[] args)
         {
             //Connect to DraftSight application
             dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
             dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

             //Get active document
             Document dsDoc = dsApp.GetActiveDocument();
             if (null == dsDoc)
             {
                 MessageBox.Show("There are no open documents in DraftSight.");
                 return;
             }

             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get Sketch Manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //PolygonMesh parameters
             double[] coordinatesArray = new double[]
             {
                 0, 0, -4,
                 -1.53073372946036,0,-3.69551813004515,
                 -2.82842712474619,0,-2.82842712474619,
                 -3.69551813004515,0,-1.53073372946036,
                 -4, 0, 0,
                 0, 0, -4,
                 -0.76536686473018,-1.32565429614237,-3.69551813004515,
                 -1.4142135623731,-2.44948974278318,-2.82842712474619,
                 -1.84775906502257,-3.20041258076506,-1.53073372946036,
                 -2,-3.46410161513776,0,
                 0, 0, -4,
                 0.765366864730179,-1.32565429614237,-3.69551813004515,
                 1.41421356237309,-2.44948974278318,-2.82842712474619,
                 1.84775906502257,-3.20041258076506,-1.53073372946036,
                 2,-3.46410161513776,0,
                 0, 0, -4,
                 1.53073372946036,0,-3.69551813004515,
                 2.82842712474619,0,-2.82842712474619,
                 3.69551813004515,0,-1.53073372946036,
                 4, 0, 0,
                 0, 0, -4,
                 0.76536686473018,1.32565429614237,-3.69551813004515,
                 1.4142135623731,2.44948974278318,-2.82842712474619,
                 1.84775906502257,3.20041258076506,-1.53073372946036,
                 2,3.46410161513775,0,
                 0, 0, -4,
                 -0.765366864730179,1.32565429614237,-3.69551813004515,
                 -1.41421356237309,2.44948974278318,-2.82842712474619,
                 -1.84775906502257,3.20041258076506,-1.53073372946036,
                 -2,3.46410161513776, 0
             };
             int mVertexCount = 6;
             int nVertexCount = 5;

             //Add PolygonMesh
             PolygonMesh dsPolygonMesh = dsSketchMgr.InsertPolygonMesh(mVertexCount, nVertexCount, coordinatesArray);

             //Make PolygonMesh continuous from the last row to the first row
             dsPolygonMesh.MClosed =  true;

             //Zoom to fit
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

             //Print PolygonMesh properties
             PrintParameters(dsPolygonMesh);
         }

         private static void PrintParameters(PolygonMesh dsPolygonMesh)
         {
             Debug.Print(Environment.NewLine + "Polygon mesh parameters...");

             //Print common entity parameters
             Debug.Print("Handle = " + dsPolygonMesh.Handle);
             Debug.Print("Color = " + dsPolygonMesh.Color.GetNamedColor());
             Debug.Print("Erased = " + dsPolygonMesh.Erased);
             Debug.Print("Layer = " + dsPolygonMesh.Layer);
             Debug.Print("LineScale = " + dsPolygonMesh.LineScale);
             Debug.Print("LineStyle = " + dsPolygonMesh.LineStyle);
             Debug.Print("LineWeight = " + dsPolygonMesh.LineWeight);
             Debug.Print("Visible = " + dsPolygonMesh.Visible);

             double x1, y1, z1;
             double x2, y2, z2;
             dsPolygonMesh.GetBoundingBox(out x1, out y1, out z1, out x2, out y2, out z2);
             Debug.Print(string.Format("BoundingBox: ({0},{1},{2}) and ({3},{4},{5})", x1, y1, z1, x2, y2, z2));

             //Print PolygonMesh parameters
             Debug.Print("FitSmooth = " + dsPolygonMesh.FitSmooth);
             Debug.Print("NDensity = " + dsPolygonMesh.NDensity);
             Debug.Print("MDensity = " + dsPolygonMesh.MDensity);
             Debug.Print("NClosed = " + dsPolygonMesh.NClosed);
             Debug.Print("MClosed = " + dsPolygonMesh.MClosed);
             Debug.Print("MVertexCount = " + dsPolygonMesh.GetMVertexCount());
             Debug.Print("NVertexCount = " + dsPolygonMesh.GetNVertexCount());

             //Print PolygonMesh coordinates
             Debug.Print("Coordinates of polygon mesh vertices:");
             for (int vertexIndex = 0; vertexIndex < dsPolygonMesh.GetVerticesCount(); ++vertexIndex)
             {
                 double x, y, z;
                 dsPolygonMesh.GetVertexCoordinate(vertexIndex,  out x,  out y,  out z);

                 Debug.Print(string.Format("Vertex({0}): ({1},{2},{3})", vertexIndex, x, y, z));
             }
         }
     }
 }
```
