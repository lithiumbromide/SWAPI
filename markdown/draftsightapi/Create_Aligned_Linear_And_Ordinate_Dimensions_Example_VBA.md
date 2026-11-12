---
title: "Create Aligned Linear and Ordinate Dimensions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBA.htm"
---

# Create Aligned Linear and Ordinate Dimensions Example (VBA)

This example shows how to create aligned linear and ordinate Dimensions for a closed PolyLine and Circles. A Leader and a geometric tolerance are also created.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to:
'    install_dir\bin\dsAutomation.dll
' 4. Start DraftSight and open a document.
' 5. Run the macro.
'
' Postconditions:
' 1. A closed PolyLine and four Circles are constructed.
' 2. Aligned linear and ordinate Dimensions are created.
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
        'Connect to DraftSight application
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
            Return
        End If
```

```
        'Get model space
        Dim dsModel As DraftSight.Model
        Set dsModel = dsDoc.GetModel()
```

```
        'Get sketch manager
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsSketchMgr = dsModel.GetSketchManager()
```

```
        'Construct a closed PolyLine
        Dim coordinates(7) As Double
        coordinates(0) = 2
        coordinates(1) = 2
        coordinates(2) = 8
        coordinates(3) = 2
        coordinates(4) = 8
        coordinates(5) = 8
        coordinates(6) = 2
        coordinates(7) = 8
        Dim closed As Boolean
        closed = True
        Dim dsPolyline As DraftSight.PolyLine
        Set dsPolyline = dsSketchMgr.InsertPolyline2D(coordinates, closed)
```

```
        'Construct four Circles
        Dim centerX As Double
        centerX = 3.5
        Dim centerY As Double
        centerY = 3.5
        Dim centerZ As Double
        centerZ = 0#
        Dim radius As Double
        radius = 0.7
        Dim dsFirstCircle As DraftSight.Circle
        Set dsFirstCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        centerX = 6.5
        Dim dsSecondCircle As DraftSight.Circle
        Set dsSecondCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        centerX = 6.5
        centerY = 6.5
        Dim dsThirdCircle As DraftSight.Circle
        Set dsThirdCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        centerX = 3.5
        Dim dsFourthCircle As DraftSight.Circle
        Set dsFourthCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Add aligned linear Dimensions
        Dim extLine1Point(2) As Double
        extLine1Point(0) = 2
        extLine1Point(1) = 2
        extLine1Point(2) = 0
        Dim extLine2Point(2) As Double
        extLine2Point(0) = 8
        extLine2Point(1) = 2
        extLine2Point(2) = 0
        Dim dimLinePoint(2) As Double
        dimLinePoint(0) = 5
        dimLinePoint(1) = 1
        dimLinePoint(2) = 0
        Dim dimensionTextOverride As String
        dimensionTextOverride = ""
        Dim dsFirstAlignedDim As DraftSight.AlignedDimension
        Set dsFirstAlignedDim = dsSketchMgr.InsertAlignedDimension(extLine1Point, extLine2Point, dimLinePoint, dimensionTextOverride)
```

```
        extLine1Point(0) = 8
        extLine1Point(1) = 2
        extLine2Point(0) = 8
        extLine2Point(1) = 8
        dimLinePoint(0) = 9
        dimLinePoint(1) = 5
        Dim dsSecondAlignedDim As DraftSight.AlignedDimension
        Set dsSecondAlignedDim = dsSketchMgr.InsertAlignedDimension(extLine1Point, extLine2Point, dimLinePoint, dimensionTextOverride)
```

```
        'Add ordinate Dimensions
        Dim measure As dsOrdinateDimensionMeasure_e
        measure = dsOrdinateDimensionMeasure_e.dsOrdinateDimensionMeasure_UseYAxis
        Dim datumPosition(2) As Double
        datumPosition(0) = 2
        datumPosition(1) = 2
        datumPosition(2) = 0
        Dim dimPosition(2) As Double
        dimPosition(0) = 1
        dimPosition(1) = 2
        dimPosition(2) = 0
        Dim dsFirstOrdinateDim As DraftSight.OrdinateDimension
        Set dsFirstOrdinateDim = dsSketchMgr.InsertOrdinateDimension(datumPosition, dimPosition, dimensionTextOverride, measure)
```

```
        datumPosition(1) = 8
        dimPosition(1) = 8
        Dim dsSecondOrdinateDim As DraftSight.OrdinateDimension
        Set dsSecondOrdinateDim = dsSketchMgr.InsertOrdinateDimension(datumPosition, dimPosition, dimensionTextOverride, measure)
```

```
        'Add Leader
        Dim leaderCoordinates(5) As Double
        leaderCoordinates(0) = 6.5
        leaderCoordinates(1) = 7.2
        leaderCoordinates(2) = 0
        leaderCoordinates(3) = 7.7
        leaderCoordinates(4) = 8.6
        leaderCoordinates(5) = 0
        Dim noteWidth As Double
        noteWidth = 1#
        Dim noteText As String
        noteText = "4X"
        Dim dsLeader As DraftSight.Leader
        Set dsLeader = dsSketchMgr.InsertLeader(leaderCoordinates, noteWidth, noteText)
```

```
        'Add a geometric tolerance
        Dim tolerancePosition(2) As Double
        tolerancePosition(0) = 8.2
        tolerancePosition(1) = 8.6
        tolerancePosition(2) = 0
        Dim textString As String
        textString = "{\Fgdt;j}%%v{\Fgdt;n}0.7{\Fgdt;m}"
        Dim dsTolerance As DraftSight.Tolerance
        Set dsTolerance = dsSketchMgr.InsertTolerance(tolerancePosition, textString)
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
    End Sub
```
