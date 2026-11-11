---
title: "Create Polygon Face Mesh Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Polygon_Face_Mesh_Example_VBA.htm"
---

# Create Polygon Face Mesh Example (VBA)

This example shows how to create a polygon face mesh.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Open the Immediate window.
' 5. Start DraftSight and open a drawing document.
' 6. Run the macro.
'
' Postconditions:
' 1. A polygon face mesh is created and zoomed to fit.
' 2. All polygon mesh face parameters are printed to the Immediate
'    window.
'------------------------------------------------------------
```

```
Option Explicit
```

```
    Sub Main()
```

```
        'Connect to DraftSight application
        Dim dsApp As DraftSight.Application
        Set dsApp = GetObject(, "DraftSight.Application")
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Get active document
	Dim dsDoc As DraftSight.Document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            End
        End If
```

```
        'Get model space
        Dim dsModel As DraftSight.Model
        Set dsModel = dsDoc.GetModel()
```

```
        'Get Sketch Manager
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsSketchMgr = dsModel.GetSketchManager()
```

```
        'Polygon face mesh parameters
        Dim verticesCount As Integer
        verticesCount = 8
```

```
        Dim coordinatesArray() As Variant
        coordinatesArray = Array(2#, 2#, 0#, 2#, 6#, 0#, _
        6#, 6#, 0#, 6#, 2#, 0#, 2#, 2#, _
        2#, 2#, 6#, 2#, 6#, 6#, 2#, 6#, 2#, 2#)
```

```
        Dim faceVerticesCountArray() As Variant
        faceVerticesCountArray = Array(4, 4, 4, 4, 4, 4)
```

```
        Dim faceVerticesArray() As Variant
        faceVerticesArray = Array(1, 2, 3, 4, 5, 6, 7, 8, _
        1, 5, 8, 4, 2, 6, 7, 3, 3, 7, 8, _
        4, 1, 2, 6, 5)
```

```
        Dim coordinatesDoubleArray() As Double
        Dim i As Long
        Dim arraySize As Long
        arraySize = UBound(coordinatesArray)
        ReDim coordinatesDoubleArray(arraySize)
        For i = 0 To arraySize
            coordinatesDoubleArray(i) = coordinatesArray(i)
        Next i
```

```
        Dim faceVerticesCountLongArray() As Long
        arraySize = UBound(faceVerticesCountArray)
        ReDim faceVerticesCountLongArray(arraySize)
        For i = 0 To arraySize
            faceVerticesCountLongArray(i) = faceVerticesCountArray(i)
        Next i
```

```
        Dim faceVerticesLongArray() As Long
        arraySize = UBound(faceVerticesArray)
        ReDim faceVerticesLongArray(arraySize)
        For i = 0 To arraySize
            faceVerticesLongArray(i) = faceVerticesArray(i)
        Next i
```

```
        'Add polygon face mesh
        Dim dsPolyFaceMesh As DraftSight.PolyFaceMesh
        Set dsPolyFaceMesh = dsSketchMgr.InsertPolyFaceMesh(verticesCount, coordinatesDoubleArray, faceVerticesCountLongArray, faceVerticesLongArray)
```

```
        If Not dsPolyFaceMesh Is Nothing Then
            'Zoom to fit
            dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
            'Print Polygon face mesh properties
            PrintParameters dsPolyFaceMesh
        Else
            MsgBox ("Polygon face mesh entity was not added to the current drawing.")
        End If
```

```
    End Sub
```

```
    Sub PrintParameters(ByVal dsPolyFaceMesh As DraftSight.PolyFaceMesh)
        Debug.Print ("Polygon face mesh parameters...")
```

```
        'Print common entity parameters
        Debug.Print ("Handle = " & dsPolyFaceMesh.Handle)
        Debug.Print ("Color = " & dsPolyFaceMesh.Color.GetNamedColor())
        Debug.Print ("Erased = " & dsPolyFaceMesh.Erased)
        Debug.Print ("Layer = " & dsPolyFaceMesh.Layer)
        Debug.Print ("LineScale = " & dsPolyFaceMesh.LineScale)
        Debug.Print ("LineStyle = " & dsPolyFaceMesh.LineStyle)
        Debug.Print ("LineWeight = " & dsPolyFaceMesh.LineWeight)
        Debug.Print ("Visible = " & dsPolyFaceMesh.Visible)
```

```
        Dim x1 As Double, y1 As Double, z1 As Double
        Dim x2 As Double, y2 As Double, z2 As Double
        dsPolyFaceMesh.GetBoundingBox x1, y1, z1, x2, y2, z2
        Debug.Print ("BoundingBox: " & x1 & ", " & y1 & ", " & z1 & ", " & x2 & ", " & y2 & ", " & z2)
```

```
        'Print polygon face mesh faces
        Dim countFaces As Long
        countFaces = dsPolyFaceMesh.GetFacesCount
        Debug.Print ("Count of faces = " & countFaces)
        Dim faceIndex As Long
            For faceIndex = 0 To dsPolyFaceMesh.GetFacesCount() - 1
            Dim corner1Vertex As Long, corner2Vertex As Long, corner3Vertex As Long, corner4Vertex As Long
            dsPolyFaceMesh.GetFace faceIndex, corner1Vertex, corner2Vertex, corner3Vertex, corner4Vertex
            Debug.Print ("Face(0) : (1),(2),(3),(4) " & faceIndex & " : " & corner1Vertex & ", " & corner2Vertex & ", " & corner3Vertex & ", " & corner4Vertex)
```

```
        Next
```

```
        'Print polygon face mesh vertices
        Dim countVertices As Long
        countVertices = dsPolyFaceMesh.GetVerticesCount
        Debug.Print ("Count of vertices = " & countVertices)
        Dim vertexIndex As Long
        For vertexIndex = 0 To dsPolyFaceMesh.GetVerticesCount() - 1
            Dim x As Double, y As Double, z As Double
            dsPolyFaceMesh.GetVertexCoordinate vertexIndex, x, y, z
            Debug.Print ("Vertex (0) : (1),(2),(3) " & vertexIndex & " : " & x & ", " & y & ", " & z)
        Next
```

```
    End Sub
```
