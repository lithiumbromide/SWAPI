---
title: "Create Angular Dimensions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Angular_Dimensions_Example_VBA.htm"
---

# Create Angular Dimensions Example (VBA)

This example shows how to create angular Dimensions using 3 points, 2 lines, and an arc.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to:
'    install_dir\bin\dsAutomation.dll
' 4. Open the Immediate window.
' 5. Start DraftSight and open a document.
' 6. Run the macro.
'
' Postconditions:
' 1. Angular Dimensions using 3 points, 2 lines, and an arc are created.
' 2. Examine the Immediate window and the drawing.
'------------------------------------------------------------
Option Explicit
```

```
    Sub main()
```

```
        Dim dsApp As DraftSight.Application
```

```
        'Connect to the DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand

        'Get the active document
        Dim dsDoc As DraftSight.Document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get the model space
        Dim dsModel As DraftSight.Model
        Set dsModel = dsDoc.GetModel()
```

```
        'Get the sketch manager
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsSketchMgr = dsModel.GetSketchManager()
```

```
        'Add an angular Dimension using three points
        Dim dsAngular3PointDim As DraftSight.AngularDimension
        Set dsAngular3PointDim = AddAngularDimensionUsing3Points(dsSketchMgr)
```

```
        'Print the angular Dimension's properties
        PrintAngularDimProperties dsAngular3PointDim
```

```
        'Add the angular Dimension using two lines
        Dim dsAngular2LinesDim As DraftSight.AngularDimension
        Set dsAngular2LinesDim = AddAngularDimensionUsing2Lines(dsSketchMgr)
```

```
        'Print the angular Dimension's properties
        PrintAngularDimProperties dsAngular2LinesDim
```

```
        'Add an angular Dimension for the arc
        Dim dsAngularArcDim As DraftSight.AngularDimension
        Set dsAngularArcDim = AddAngularDimensionForArc(dsSketchMgr)
```

```
        'Print the angular Dimension's properties
        PrintAngularDimProperties dsAngularArcDim
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
    End Sub
```

```
    Function AddAngularDimensionForArc(ByVal dsSketchMgr As DraftSight.SketchManager) As DraftSight.AngularDimension
        'Draw an arc
        Dim centerX As Double
        centerX = 18
```

```
        Dim centerY As Double
        centerY = 2
```

```
        Dim centerZ As Double
        centerZ = 0
```

```
        Dim radius As Double
        radius = 3
```

```
        Dim startAngle As Double
        startAngle = 0#
```

```
        Dim endAngle As Double
        endAngle = 3.14159265358979 / 2
```

```
        Dim dsArc As DraftSight.CircleArc
        Set dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, radius, startAngle, endAngle)
```

```
        'Angular Dimension's position
        Dim dimPosition(2) As Double
        dimPosition(0) = 20
        dimPosition(1) = 5
        dimPosition(2) = 0
```

```
        'Text override
        Dim dimTextOverride As String
        dimTextOverride = "AngularDimArc"
```

```
        Dim dsAngularDim As DraftSight.AngularDimension
        Set dsAngularDim = dsSketchMgr.InsertAngularDimensionArc(dsArc, dimPosition, dimTextOverride)
```

```
        Debug.Print ("An angular Dimension for an arc was added.")
        Debug.Print ("")
```

```
        Set AddAngularDimensionForArc = dsAngularDim
    End Function
```

```
    Function AddAngularDimensionUsing2Lines(ByVal dsSketchMgr As DraftSight.SketchManager) As DraftSight.AngularDimension
        'Draw two lines for an angular Dimension
        Dim dsFirstLine As DraftSight.Line
        Set dsFirstLine = dsSketchMgr.InsertLine(7, 0, 0, 10, 3, 0)
```

```
        Dim dsSecondLine As DraftSight.Line
        Set dsSecondLine = dsSketchMgr.InsertLine(12, 0, 0, 15, 2, 0)

        'Angular dimension position
        Dim dimPosition(2) As Double
        dimPosition(0) = 13
        dimPosition(1) = 4
        dimPosition(2) = 0
```

```
        'No text override
        Dim dimTextOverride As String
        dimTextOverride = ""
```

```
        Dim dsAngularDim As DraftSight.AngularDimension
        Set dsAngularDim = dsSketchMgr.InsertAngularDimension2Line(dsFirstLine, dsSecondLine, dimPosition, dimTextOverride)
```

```
        Debug.Print ("An angular Dimension using two lines was added.")
        Debug.Print ("")
```

```
        Set AddAngularDimensionUsing2Lines = dsAngularDim
    End Function
```

```
    Function AddAngularDimensionUsing3Points(ByVal dsSketchMgr As DraftSight.SketchManager) As DraftSight.AngularDimension
        'Angular dimension parameters
        Dim centerPoint(2) As Double
        centerPoint(0) = 0
        centerPoint(1) = 0
        centerPoint(2) = 0
```

```
        Dim angleStartPoint(2) As Double
        angleStartPoint(0) = 2
        angleStartPoint(1) = 2
        angleStartPoint(2) = 0
```

```
        Dim angleEndPoint(2) As Double
        angleEndPoint(0) = 2
        angleEndPoint(1) = 4
        angleEndPoint(2) = 0
```

```
        Dim dimPosition(2) As Double
        dimPosition(0) = 5
        dimPosition(1) = 5
        dimPosition(2) = 0
```

```
        'No text override
        Dim dimTextOverride As String
        dimTextOverride = ""
```

```
        Dim dsAngularDim As DraftSight.AngularDimension
        Set dsAngularDim = dsSketchMgr.InsertAngularDimension3Point(centerPoint, angleStartPoint, angleEndPoint, dimPosition, dimTextOverride)
```

```
        Debug.Print ("An angular Dimension using three points was added.")
        Debug.Print ("")
```

```
        Set AddAngularDimensionUsing3Points = dsAngularDim
    End Function
```

```
    Sub PrintAngularDimProperties(dsAngularDim As DraftSight.AngularDimension)
        Debug.Print ("  Angular dimension parameters...")
```

```
        Debug.Print ("    Type = " & dsAngularDim.Type)
```

```
        'Get general Dimension object, which contains common Dimension properties
        Dim dsGeneralDim As DraftSight.GeneralDimension
        Set dsGeneralDim = dsAngularDim.GetGeneralDimension()
```

```
        Debug.Print ("    Dimension style = " & dsGeneralDim.DimensionStyle)
        Debug.Print ("    Handle = " & dsGeneralDim.Handle)
        Debug.Print ("    Measurement (in radians) = " & dsGeneralDim.Measurement)
        Debug.Print ("    Related = " & dsGeneralDim.Related)
        Debug.Print ("    Text override = " & dsGeneralDim.TextOverride)
        Debug.Print ("    Text rotation = " & dsGeneralDim.TextRotation)
```

```
        'Get text position
        Dim x As Double
        Dim y As Double
        dsGeneralDim.GetTextPosition x, y
        Debug.Print ("    Text position (" & x & "," & y & ")")
```

```
        'Print specific parameters for angular Dimension
        Dim z As Double
        'Get center point
        dsAngularDim.GetCenterPoint x, y, z
        Debug.Print ("    Center point (" & x & "," & y & "," & z & ")")
```

```
        'Get arc point
        dsAngularDim.GetArcPoint x, y, z
        Debug.Print ("    Arc point (" & x & "," & y & "," & z & ")")
```

```
        'Get first line's start point
        dsAngularDim.GetLine1Point x, y, z
        Debug.Print ("    Line1's start point (" & x & "," & y & "," & z & ")")
```

```
        'Get first line end point
        dsAngularDim.GetLine1EndPoint x, y, z
        Debug.Print ("    Line1's end point (" & x & "," & y & "," & z & ")")
```

```
        'Get second line start point
        dsAngularDim.GetLine2Point x, y, z
        Debug.Print ("    Line2's start point (" & x & "," & y & "," & z & ")")
```

```
        'Get second line end point
        dsAngularDim.GetLine2EndPoint x, y, z
        Debug.Print ("    Line2's end point (" & x & "," & y & "," & z & ")")
        Debug.Print ("")
    End Sub
```
