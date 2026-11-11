---
title: "Create Polygon Face Mesh Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Polygon_Face_Mesh_Example_CSharp.htm"
---

# Create Polygon Face Mesh Example (C#)

This example shows how to create a polygon face mesh.

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
 // 1. A Polygon face mesh is created and zoomed to fit.
 // 2. All Polygon face mesh parameters are printed to the Immediate
 //    window.
 //------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;
 using System.Diagnostics;

 namespace AddPolyfaceMesh
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
                 MessageBox.Show("There are no opened documents in DraftSight");
                 return;
             }

             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get Sketch Manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //Polygon face mesh parameters
             int verticesCount = 8;
             double[] coordinatesArray = new double[]
             {
                 2, 2, 0,
                 2, 6, 0,
                 6, 6, 0,
                 6, 2, 0,
                 2, 2, 2,
                 2, 6, 2,
                 6, 6, 2,
                 6, 2, 2
             };
             int[] faceVerticesCountArray = new int[] { 4, 4, 4, 4, 4, 4 };
             int[] faceVerticesArray = new int[]
             {
                 1, 2, 3, 4,
                 5, 6, 7, 8,
                 1, 5, 8, 4,
                 2, 6, 7, 3,
                 3, 7, 8, 4,
                 1, 2, 6, 5
             };

             //Add polygon face mesh
             PolyFaceMesh dsPolyFaceMesh = dsSketchMgr.InsertPolyFaceMesh(verticesCount, coordinatesArray, faceVerticesCountArray, faceVerticesArray);
             if (null != dsPolyFaceMesh)
             {
                 //Zoom to fit
                 dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

                 //Print polygon face mesh parameters
                 PrintParameters(dsPolyFaceMesh);
             }
             else
             {
                 MessageBox.Show("Polygon face mesh entity was not added to the current drawing.");
             }
         }

         private static void PrintParameters(PolyFaceMesh dsPolyFaceMesh)
         {
             Debug.Print(Environment.NewLine + "Polygon face mesh parameters...");

             //Print common entity parameters
             Debug.Print("Handle = " + dsPolyFaceMesh.Handle);
             Debug.Print("Color = " + dsPolyFaceMesh.Color.GetNamedColor());
             Debug.Print("Erased = " + dsPolyFaceMesh.Erased);
             Debug.Print("Layer = " + dsPolyFaceMesh.Layer);
             Debug.Print("LineScale = " + dsPolyFaceMesh.LineScale);
             Debug.Print("LineStyle = " + dsPolyFaceMesh.LineStyle);
             Debug.Print("LineWeight = " + dsPolyFaceMesh.LineWeight);
             Debug.Print("Visible = " + dsPolyFaceMesh.Visible);

             double x1, y1, z1;
             double x2, y2, z2;
             dsPolyFaceMesh.GetBoundingBox(out x1, out y1, out z1, out x2, out y2, out z2);
             Debug.Print(string.Format("BoundingBox: ({0},{1},{2}) and ({3},{4},{5})", x1, y1, z1, x2, y2, z2));

             //Print polygon face mesh faces
             Debug.Print("Count of faces = " + dsPolyFaceMesh.GetFacesCount());
             for (int faceIndex = 0; faceIndex < dsPolyFaceMesh.GetFacesCount(); ++faceIndex)
             {
                 int corner1Vertex, corner2Vertex, corner3Vertex, corner4Vertex;
                 dsPolyFaceMesh.GetFace(faceIndex,  out corner1Vertex, out corner2Vertex, out corner3Vertex, out corner4Vertex);

                 Debug.Print(string.Format("Face({0}): ({1},{2},{3},{4})", faceIndex, corner1Vertex, corner2Vertex, corner3Vertex, corner4Vertex));
             }

             //Print polygon face mesh vertices
             Debug.Print("Count of vertices = " + dsPolyFaceMesh.GetVerticesCount());
             for (int vertexIndex = 0; vertexIndex < dsPolyFaceMesh.GetVerticesCount(); ++vertexIndex)
             {
                 double x, y, z;
                 dsPolyFaceMesh.GetVertexCoordinate(vertexIndex, out x, out y, out z);

                 Debug.Print(string.Format("Vertex({0}): ({1},{2},{3})", vertexIndex, x, y, z));
             }
         }
     }
 }
```
