---
title: "Create Aligned Linear and Ordinate Dimensions Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBNET.htm"
---

# Create Aligned Linear and Ordinate Dimensions Example (VB.NET)

This example shows how to create aligned linear and ordinate Dimensions for a closed PolyLine and Circles. A Leader and a geometric tolerance are also created.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
' 4. Add references to System and System.Forms.
' 5. Start DraftSight and open a document.
' 6. Click Start Debugging.
'
' Postconditions:
' 1. A closed PolyLine and four Circles are constructed.
' 2. Aligned linear and ordinate Dimensions are created.
'------------------------------------------------------------
```

```
Imports System.IO
Imports DraftSight.Interop.dsAutomation
```

```
Module Module1
```

```
    Dim dsApp As Application
```

```
    Sub Main()
        'Connect to DraftSight application
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get model space
        Dim dsModel As Model = dsDoc.GetModel()
```

```
        'Get sketch manager
        Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()
```

```
        'Construct a closed PolyLine
        Dim coordinates As Double() = New Double() {2, 2, 8, 2, 8, 8, 2, 8}
        Dim closed As Boolean = True
        Dim dsPolyline As PolyLine = dsSketchMgr.InsertPolyline2D(coordinates, closed)
```

```
        'Construct four Circles
        Dim centerX As Double = 3.5
        Dim centerY As Double = 3.5
        Dim centerZ As Double = 0.0
        Dim radius As Double = 0.7
        Dim dsFirstCircle As Circle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        centerX = 6.5
        Dim dsSecondCircle As Circle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        centerX = 6.5
        centerY = 6.5
        Dim dsThirdCircle As Circle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        centerX = 3.5
        Dim dsFourthCircle As Circle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Add aligned linear Dimensions
        Dim extLine1Point As Double() = New Double() {2, 2, 0}
        Dim extLine2Point As Double() = New Double() {8, 2, 0}
        Dim dimLinePoint As Double() = New Double() {5, 1, 0}
        Dim dimensionTextOverride As String = ""
        Dim dsFirstAlignedDim As AlignedDimension = dsSketchMgr.InsertAlignedDimension(extLine1Point, extLine2Point, dimLinePoint, dimensionTextOverride)
```

```
        extLine1Point(0) = 8
        extLine1Point(1) = 2
        extLine2Point(0) = 8
        extLine2Point(1) = 8
        dimLinePoint(0) = 9
        dimLinePoint(1) = 5
        Dim dsSecondAlignedDim As AlignedDimension = dsSketchMgr.InsertAlignedDimension(extLine1Point, extLine2Point, dimLinePoint, dimensionTextOverride)
```

```
        'Add ordinate Dimensions
        Dim measure As dsOrdinateDimensionMeasure_e = dsOrdinateDimensionMeasure_e.dsOrdinateDimensionMeasure_UseYAxis
        Dim datumPosition As Double() = New Double() {2, 2, 0}
        Dim dimPosition As Double() = New Double() {1, 2, 0}
        Dim dsFirstOrdinateDim As OrdinateDimension = dsSketchMgr.InsertOrdinateDimension(datumPosition, dimPosition, dimensionTextOverride, measure)
```

```
        datumPosition(1) = 8
        dimPosition(1) = 8
        Dim dsSecondOrdinateDim As OrdinateDimension = dsSketchMgr.InsertOrdinateDimension(datumPosition, dimPosition, dimensionTextOverride, measure)
```

```
        'Add Leader
        Dim leaderCoordinates As Double() = New Double() {6.5, 7.2, 0, 7.7, 8.6, 0}
        Dim noteWidth As Double = 1.0
        Dim noteText As String = "4X"
        Dim dsLeader As Leader = dsSketchMgr.InsertLeader(leaderCoordinates, noteWidth, noteText)
```

```
        'Add a geometric tolerance
        Dim tolerancePosition As Double() = New Double() {8.2, 8.6, 0}
        Dim textString As String = "{\Fgdt;j}%%v{\Fgdt;n}0.7{\Fgdt;m}"
        Dim dsTolerance As Tolerance = dsSketchMgr.InsertTolerance(tolerancePosition, textString)
```

```
        'Zoom to fit
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
    End Sub
```

```
End Module
```
