---
title: "Create PolygonMesh Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_PolygonMesh_Example_VBA.htm"
---

# Create PolygonMesh Example (VBA)

This example shows how to create a PolygonMesh.

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
' 1. A PolygonMesh is created and zoomed to fit.
' 2. All PolygonMesh parameters are printed to the Immediate
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
        'PolygonMesh parameters
        Dim coordinatesArray() As Variant
        coordinatesArray = Array(0#, 0#, -4#, -1.53073372946036, 0#, -3.69551813004515, _
         -2.82842712474619, 0#, -2.82842712474619, -3.69551813004515, 0#, -1.53073372946036, _
         -4#, 0#, 0#, 0#, 0#, -4#, _
         -0.76536686473018, -1.32565429614237, -3.69551813004515, -1.4142135623731, -2.44948974278318, -2.82842712474619, _
         -1.84775906502257, -3.20041258076506, -1.53073372946036, -2#, -3.46410161513776, 0#, _
         0#, 0#, -4#, 0.765366864730179, -1.32565429614237, -3.69551813004515, _
         1.41421356237309, -2.44948974278318, -2.82842712474619, 1.84775906502257, -3.20041258076506, -1.53073372946036, _
         2#, -3.46410161513776, 0#, 0#, 0#, -4#, _
         1.53073372946036, 0#, -3.69551813004515, 2.82842712474619, 0#, -2.82842712474619, _
         3.69551813004515, 0#, -1.53073372946036, 4#, 0#, 0#, _
         0#, 0#, -4#, 0.76536686473018, 1.32565429614237, -3.69551813004515, _
         1.4142135623731, 2.44948974278318, -2.82842712474619, 1.84775906502257, 3.20041258076506, -1.53073372946036, _
         2#, 3.46410161513775, 0#, 0#, 0#, -4#, _
         -0.765366864730179, 1.32565429614237, -3.69551813004515, -1.41421356237309, 2.44948974278318, -2.82842712474619, _
         -1.84775906502257, 3.20041258076506, -1.53073372946036, -2#, 3.46410161513776, 0#)

        Dim mVertexCount As Long
        mVertexCount = 6
```

```
        Dim nVertexCount As Long
        nVertexCount = 5
```

```
        Dim coordinatesDoubleArray() As Double
	Dim nbrArrayElements As Long
        nbrArrayElements = (mVertexCount * nVertexCount) * 3
        ReDim coordinatesDoubleArray(nbrArrayElements - 1)
```

```
        Dim i As Long
        For i = 0 To (nbrArrayElements - 1)
            coordinatesDoubleArray(i) = coordinatesArray(i)
        Next i
```

```
        'Add PolygonMesh
        Dim dsPolygonMesh As DraftSight.PolygonMesh
        Set dsPolygonMesh = dsSketchMgr.InsertPolygonMesh(mVertexCount, nVertexCount, coordinatesDoubleArray)
```

```
        'Make PolygonMesh continuous from the last row to the first row
        dsPolygonMesh.MClosed = True
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
        'Print PolygonMesh properties
        PrintParameters dsPolygonMesh
    End Sub
```

```
    Sub PrintParameters(ByVal dsPolygonMesh As DraftSight.PolygonMesh)
        Debug.Print ("Polygon mesh parameters...")
```

```
        'Print common entity parameters
        Debug.Print ("Handle = " & dsPolygonMesh.Handle)
        Debug.Print ("Color = " & dsPolygonMesh.Color.GetNamedColor())
        Debug.Print ("Erased = " & dsPolygonMesh.Erased)
        Debug.Print ("Layer = " & dsPolygonMesh.Layer)
        Debug.Print ("LineScale = " & dsPolygonMesh.LineScale)
        Debug.Print ("LineStyle = " & dsPolygonMesh.LineStyle)
        Debug.Print ("LineWeight = " & dsPolygonMesh.LineWeight)
        Debug.Print ("Visible = " & dsPolygonMesh.Visible)
```

```
        Dim x1 As Double, y1 As Double, z1 As Double
        Dim x2 As Double, y2 As Double, z2 As Double
        dsPolygonMesh.GetBoundingBox x1, y1, z1, x2, y2, z2
        Debug.Print ("BoundingBox: " & x1 & ", " & y1 & ", " & z1 & ", " & x2 & ", " & y2 & ", " & z2)
```

```
        'Print PolygonMesh parameters
        Debug.Print ("FitSmooth = " & dsPolygonMesh.FitSmooth)
        Debug.Print ("NDensity = " & dsPolygonMesh.NDensity)
        Debug.Print ("MDensity = " & dsPolygonMesh.MDensity)
        Debug.Print ("NClosed = " & dsPolygonMesh.NClosed)
        Debug.Print ("MClosed = " & dsPolygonMesh.MClosed)
        Debug.Print ("MVertexCount = " & dsPolygonMesh.GetMVertexCount())
        Debug.Print ("NVertexCount = " & dsPolygonMesh.GetNVertexCount())
```

```
        'Print PolygonMesh coordinates
        Debug.Print ("Coordinates of polygon mesh vertices:")
        Dim vertexIndex As Long
        For vertexIndex = 0 To dsPolygonMesh.GetVerticesCount() - 1
            Dim x As Double, y As Double, z As Double
            dsPolygonMesh.GetVertexCoordinate vertexIndex, x, y, z
```

```
            Debug.Print ("Vertex " & vertexIndex & ": (1),(2),(3): " & x & ", " & y & ", " & z)
            Next
    End Sub
```
