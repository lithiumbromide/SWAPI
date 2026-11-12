---
title: "Create Polygon Face Mesh Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Polygon_Face_Mesh_Example_VBNET.htm"
---

# Create Polygon Face Mesh Example (VB.NET)

This example shows how to create a polygon face mesh.

```vb
 '-------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Open the Immediate window.
 ' 6. Start DraftSight and open a document.
 ' 7. Click Start Debugging.
 '
 ' Postconditions:
 ' 1. A polygon face mesh is created and zoomed to fit.
 ' 2. All polygon face mesh parameters are printed to the Immediate
 '    window.
 '------------------------------------------------------------

 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms
 Imports System.Diagnostics

 Module Module1

     Sub Main()

         'Connect to DraftSight application
         Dim dsApp = GetObject(, "DraftSight.Application")
         dsApp.AbortRunningCommand() '  abort any command currently running in DraftSight to avoid nested commands

         'Get active document
         Dim dsDoc As Document = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MessageBox.Show("There are no open documents in DraftSight")
             Return
         End If

         'Get model space
         Dim dsModel As Model = dsDoc.GetModel()

         'Get Sketch Manager
         Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

         'Polygon face mesh parameters
         Dim verticesCount As Integer = 8
         Dim coordinatesArray As Double() = New  Double() {2, 2, 0, 2, 6, 0, _
          6, 6, 0, 6, 2, 0, _
          2, 2, 2, 2, 6, 2, _
          6, 6, 2, 6, 2, 2}
         Dim faceVerticesCountArray As Integer() = New  Integer() {4, 4, 4, 4, 4, 4}
         Dim faceVerticesArray As Integer() = New  Integer() {1, 2, 3, 4, 5, 6, _
          7, 8, 1, 5, 8, 4, _
          2, 6, 7, 3, 3, 7, _
          8, 4, 1, 2, 6, 5}

         'Add polygon face mesh
         Dim dsPolyFaceMesh As PolyFaceMesh = dsSketchMgr.InsertPolyFaceMesh(verticesCount, coordinatesArray, faceVerticesCountArray, faceVerticesArray)
         If dsPolyFaceMesh IsNot Nothing Then
             'Zoom to fit
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

             'Print polygon face mesh parameters
             PrintParameters(dsPolyFaceMesh)
         Else
             MessageBox.Show("Polygon face mesh entity was not added to the current drawing.")
         End If
     End Sub

     Sub PrintParameters(ByVal dsPolyFaceMesh As PolyFaceMesh)
         Debug.Print(Environment.NewLine   "Polygon face mesh parameters...")

         'Print common entity parameters
         Debug.Print("Handle = " & Convert.ToString(dsPolyFaceMesh.Handle))
         Debug.Print("Color = " & dsPolyFaceMesh.Color.GetNamedColor())
         Debug.Print("Erased = " & Convert.ToString(dsPolyFaceMesh.Erased))
         Debug.Print("Layer = " & Convert.ToString(dsPolyFaceMesh.Layer))
         Debug.Print("LineScale = " & Convert.ToString(dsPolyFaceMesh.LineScale))
         Debug.Print("LineStyle = " & Convert.ToString(dsPolyFaceMesh.LineStyle))
         Debug.Print("LineWeight = " & Convert.ToString(dsPolyFaceMesh.LineWeight))
         Debug.Print("Visible = " & Convert.ToString(dsPolyFaceMesh.Visible))

         Dim x1 As Double, y1 As  Double, z1  As  Double
         Dim x2 As Double, y2 As  Double, z2  As  Double
         dsPolyFaceMesh.GetBoundingBox(x1, y1, z1, x2, y2, z2)
         Debug.Print(String.Format("BoundingBox: ({0},{1},{2}) and ({3},{4},{5})", x1, y1, z1, x2, y2, _
          z2))

         'Print polygon face mesh faces
         Debug.Print("Count of faces = " & dsPolyFaceMesh.GetFacesCount())
         For faceIndex As Integer = 0 To dsPolyFaceMesh.GetFacesCount() - 1
             Dim corner1Vertex As Integer, corner2Vertex As Integer, corner3Vertex As Integer, corner4Vertex As Integer
             dsPolyFaceMesh.GetFace(faceIndex, corner1Vertex, corner2Vertex, corner3Vertex, corner4Vertex)

             Debug.Print(String.Format("Face({0}): ({1},{2},{3},{4})", faceIndex, corner1Vertex, corner2Vertex, corner3Vertex, corner4Vertex))
         Next

         'Print polygon face mesh vertices
         Debug.Print("Count of vertices = " & dsPolyFaceMesh.GetVerticesCount())
         For vertexIndex As Integer = 0 To dsPolyFaceMesh.GetVerticesCount() - 1
             Dim x As  Double, y  As  Double, z  As  Double
             dsPolyFaceMesh.GetVertexCoordinate(vertexIndex, x, y, z)

             Debug.Print(String.Format("Vertex({0}): ({1},{2},{3})", vertexIndex, x, y, z))
         Next
     End Sub
 End Module
```
