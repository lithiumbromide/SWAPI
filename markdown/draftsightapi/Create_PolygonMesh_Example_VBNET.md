---
title: "Create PolygonMesh Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_PolygonMesh_Example_VBNET.htm"
---

# Create PolygonMesh Example (VB.NET)

This example shows how to create a PolygonMesh.

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
 ' 1. A PolygonMesh is created and zoomed to fit.
 ' 2. All PolygonMesh parameters are printed to the Immediate
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
             MessageBox.Show("There are no open documents in DraftSight.")
             Return
         End If

         'Get model space
         Dim dsModel As Model = dsDoc.GetModel()

         'Get Sketch Manager
         Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

         'PolygonMesh parameters
         Dim coordinatesArray As Double() = New  Double() {0, 0, -4, -1.53073372946036, 0, -3.69551813004515, _
          -2.82842712474619, 0, -2.82842712474619, -3.69551813004515, 0, -1.53073372946036, _
          -4, 0, 0, 0, 0, -4, _
          -0.76536686473018, -1.32565429614237, -3.69551813004515, -1.4142135623731, -2.44948974278318, -2.82842712474619, _
          -1.84775906502257, -3.20041258076506, -1.53073372946036, -2, -3.46410161513776, 0, _
          0, 0, -4, 0.765366864730179, -1.32565429614237, -3.69551813004515, _
          1.41421356237309, -2.44948974278318, -2.82842712474619, 1.84775906502257, -3.20041258076506, -1.53073372946036, _
          2, -3.46410161513776, 0, 0, 0, -4, _
          1.53073372946036, 0, -3.69551813004515, 2.82842712474619, 0, -2.82842712474619, _
          3.69551813004515, 0, -1.53073372946036, 4, 0, 0, _
          0, 0, -4, 0.76536686473018, 1.32565429614237, -3.69551813004515, _
          1.4142135623731, 2.44948974278318, -2.82842712474619, 1.84775906502257, 3.20041258076506, -1.53073372946036, _
          2, 3.46410161513775, 0, 0, 0, -4, _
          -0.765366864730179, 1.32565429614237, -3.69551813004515, -1.41421356237309, 2.44948974278318, -2.82842712474619, _
          -1.84775906502257, 3.20041258076506, -1.53073372946036, -2, 3.46410161513776, 0}
         Dim mVertexCount As Integer = 6
         Dim nVertexCount As Integer = 5

         'Add PolygonMesh
         Dim dsPolygonMesh As PolygonMesh = dsSketchMgr.InsertPolygonMesh(mVertexCount, nVertexCount, coordinatesArray)

         'Make PolygonMesh continuous from the last row to the first row
         dsPolygonMesh.MClosed = True

         'Zoom to fit
         dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

         'Print PolygonMesh properties
         PrintParameters(dsPolygonMesh)
     End Sub

     Sub PrintParameters(ByVal dsPolygonMesh As PolygonMesh)
         Debug.Print(Environment.NewLine   "Polygon mesh parameters...")

         'Print common entity parameters
         Debug.Print("Handle = " & Convert.ToString(dsPolygonMesh.Handle))
         Debug.Print("Color = " & dsPolygonMesh.Color.GetNamedColor())
         Debug.Print("Erased = " & Convert.ToString(dsPolygonMesh.Erased))
         Debug.Print("Layer = " & Convert.ToString(dsPolygonMesh.Layer))
         Debug.Print("LineScale = " & Convert.ToString(dsPolygonMesh.LineScale))
         Debug.Print("LineStyle = " & Convert.ToString(dsPolygonMesh.LineStyle))
         Debug.Print("LineWeight = " & Convert.ToString(dsPolygonMesh.LineWeight))
         Debug.Print("Visible = " & Convert.ToString(dsPolygonMesh.Visible))

         Dim x1 As Double, y1 As  Double, z1  As  Double
         Dim x2 As Double, y2 As  Double, z2  As  Double
         dsPolygonMesh.GetBoundingBox(x1, y1, z1, x2, y2, z2)
         Debug.Print(String.Format("BoundingBox: ({0},{1},{2}) and ({3},{4},{5})", x1, y1, z1, x2, y2, _
          z2))

         'Print PolygonMesh parameters
         Debug.Print("FitSmooth = " & Convert.ToString(dsPolygonMesh.FitSmooth))
         Debug.Print("NDensity = " & Convert.ToString(dsPolygonMesh.NDensity))
         Debug.Print("MDensity = " & Convert.ToString(dsPolygonMesh.MDensity))
         Debug.Print("NClosed = " & Convert.ToString(dsPolygonMesh.NClosed))
         Debug.Print("MClosed = " & Convert.ToString(dsPolygonMesh.MClosed))
         Debug.Print("MVertexCount = " & dsPolygonMesh.GetMVertexCount())
         Debug.Print("NVertexCount = " & dsPolygonMesh.GetNVertexCount())

         'Print PolygonMesh coordinates
         Debug.Print("Coordinates of polygon mesh vertices:")
         For vertexIndex As Integer = 0 To dsPolygonMesh.GetVerticesCount() - 1
             Dim x As  Double, y  As  Double, z  As  Double
             dsPolygonMesh.GetVertexCoordinate(vertexIndex, x, y, z)

             Debug.Print(String.Format("Vertex({0}): ({1},{2},{3})", vertexIndex, x, y, z))
         Next
     End Sub

 End Module
```
