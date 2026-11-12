---
title: "Create and Apply DimensionStyle Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Apply_DimensionStyle_Example_VBA.htm"
---

# Create and Apply DimensionStyle Example (VBA)

This example shows how to create, activate, and apply a new DimensionStyle. This example also shows how to create arc length, jogged, rotated, radius, and diameter Dimensions for circles, arcs, and a line.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll
' 4. Open the Immediate window.
' 5. Start DraftSight and open a document.
' 6. Run the macro.
'
' Postconditions:
' 1. A new DimensionStyle named SampleDimStyle is created and
'    activated.
' 2. Arc length, jogged, rotated, radius, and diameter dimensions
'    are created for circles, arcs, and a line, using the new
'    DimensionStyle.
' 3. Examine the Immediate window and the drawing.
'------------------------------------------------------------
Option Explicit
    Sub main()
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
        'Get DimensionStyle manager
        Dim dsDimStyleManager As DraftSight.DimensionStyleManager
        Set dsDimStyleManager = dsDoc.GetDimensionStyleManager()
```

```
        'Create DimensionStyle named SampleDimStyle
        Dim createDimStyleResult As dsCreateObjectResult_e
        Dim dimStyleName As String
        dimStyleName = "SampleDimStyle"
        Dim dsDimStyle As DraftSight.DimensionStyle
        dsDimStyleManager.CreateDimensionStyle dimStyleName, dsDimStyle, createDimStyleResult
        Select Case True
            Case (dsCreateObjectResult_e.dsCreateObjectResult_Error = createDimStyleResult), dsCreateObjectResult_e.dsCreateObjectResult_AlreadyExists = createDimStyleResult, dsDimStyle Is Nothing
                MsgBox ("Failed to create " & dimStyleName & " DimensionStyle, or DimensionStyle already exists.")
                Exit Sub
        End Select
```

```
        SetDimensionStyleSettings dsDimStyle

        'Activate DimensionStyle
        dsDimStyle.Activate
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
        'Draw arc length Dimension
        DrawArcLengthDimension dsSketchMgr
```

```
        'Draw jogged Dimension for circle and arc
        DrawJoggedDimension dsSketchMgr
```

```
        'Draw rotated Dimension
        DrawRotatedDimension dsSketchMgr
```

```
        'Draw radius Dimension for circle and arc
        DrawRadialDimension dsSketchMgr
```

```
        'Draw diameter Dimension for circle and arc
        DrawDiameterDimension dsSketchMgr
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
    End Sub
```

```
    Sub SetDimensionStyleSettings(ByVal dsDimStyle As DimensionStyle)
        'Get DimensionStyle arrows options
        Dim dsArrowsDimStyleOptions As DraftSight.DimensionStyleArrowsOptions
        Set dsArrowsDimStyleOptions = dsDimStyle.GetDimensionStyleArrowsOptions()
```

```
        'Set start and end arrow types
        dsArrowsDimStyleOptions.SetStartArrow dsDimensionArrowType_e.dsDimensionArrowType_ClosedBlank, ""
        dsArrowsDimStyleOptions.SetEndArrow dsDimensionArrowType_e.dsDimensionArrowType_ClosedBlank, ""
```

```
        'Get DimensionStyle line options
        Dim dsLineDimStyleOptions As DraftSight.DimensionStyleLineOptions
        Set dsLineDimStyleOptions = dsDimStyle.GetDimensionStyleLineOptions()
```

```
        'Set Dimension line color
        Dim dsColor As DraftSight.Color
        Set dsColor = dsLineDimStyleOptions.DimensionLineColor
        dsColor.SetNamedColor dsNamedColor_e.dsNamedColor_Green
        dsLineDimStyleOptions.DimensionLineColor = dsColor
```

```
        'Set extension line color
        dsColor.SetNamedColor dsNamedColor_e.dsNamedColor_Yellow
        dsLineDimStyleOptions.ExtensionLineColor = dsColor
```

```
        'Get DimensionStyle radius and diameter Dimension options
        Dim dsRadialAndDiameterDimStyleOptions As DraftSight.DimensionStyleRadialDiameterDimensionOptions
        Set dsRadialAndDiameterDimStyleOptions = dsDimStyle.GetDimensionStyleRadialDiameterDimensionOptions()
```

```
        'Set jog angle 45 degrees (in radians)
        dsRadialAndDiameterDimStyleOptions.RadiusDimensionJogAngle = 3.14159265358979 / 4
```

```
        'Set center mark
        Dim markSize As Double
        markSize = 0.05
        dsRadialAndDiameterDimStyleOptions.SetCenterMarkDisplay dsDimensionCenterMarkDisplay_e.dsDimensionCenterMarkDisplay_AsMark, markSize
```

```
        'Get Dimension style text options
        Dim dsTextOptions As DraftSight.DimensionStyleTextOptions
        Set dsTextOptions = dsDimStyle.GetDimensionStyleTextOptions()
```

```
        'Frame Dimension text
        dsTextOptions.FrameDimensionText = True
```

```
        'Set text position
        dsTextOptions.HorizontalPosition = dsDimensionTextHorizontalPosition_e.dsDimensionTextHorizontalPosition_Centered
        dsTextOptions.VerticalPosition = dsDimensionTextVerticalPosition_e.dsDimensionTextVerticalPosition_Centered
```

```
        'Set text alignment
        dsTextOptions.Alignment = dsDimensionTextAlignment_e.dsDimensionTextAlignment_AlignWithDimensionLines
    End Sub
```

```
    Sub DrawArcLengthDimension(ByVal dsSketchMgr As DraftSight.SketchManager)
        'Add arc to drawing
        Dim centerX As Double
        centerX = -8
        Dim centerY As Double
        centerY = 1
        Dim centerZ As Double
        centerZ = 0
        Dim radius As Double
        radius = 5
        Dim startAngle As Double
        startAngle = 3.14159265358979 / 6
        Dim endAngle As Double
        endAngle = 3.14159265358979
        Dim dsArc As DraftSight.CircleArc
        Set dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, radius, startAngle, endAngle)
```

```
        'Add arc length Dimension
        Dim dimensionPosition(2) As Double
        dimensionPosition(0) = -6
        dimensionPosition(1) = 6
        dimensionPosition(2) = 0
        Dim dimensionTextOverride As String
        dimensionTextOverride = ""
        Dim dsArcLengthDim As DraftSight.ArcLengthDimension
        Set dsArcLengthDim = dsSketchMgr.InsertArcLengthDimension(dsArc, dimensionPosition, dimensionTextOverride)
```

```
        'Print information about arc length Dimension
        PrintArcLengthDimProperties dsArcLengthDim
```

```
        'Add a partial arc length Dimension
        Dim firstPoint(2) As Double
        firstPoint(0) = -4
        firstPoint(1) = 3
        firstPoint(2) = 0
        Dim secondPoint(2) As Double
        secondPoint(0) = -7
        secondPoint(1) = 6
        secondPoint(2) = 0
        dimensionPosition(0) = -6
        dimensionPosition(1) = 7
        Dim dsArcLengthPartialDim As DraftSight.ArcLengthDimension
        Set dsArcLengthPartialDim = dsSketchMgr.InsertArcLengthDimensionPartial(dsArc, firstPoint, secondPoint, dimensionPosition, dimensionTextOverride)
```

```
        'Print information about partial arc length Dimension
        PrintArcLengthDimProperties dsArcLengthDim
    End Sub
```

```
    Sub DrawJoggedDimension(ByVal dsSketchMgr As DraftSight.SketchManager)
        'Draw a circle
        Dim centerX As Double
        centerX = -7
        Dim centerY As Double
        centerY = -5
        Dim centerZ As Double
        centerZ = 0
        Dim radius As Double
        radius = 3
        Dim dsCircle As DraftSight.Circle
        Set dsCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Add jogged Dimension to circle
        Dim centerPositionOverride(2) As Double
        centerPositionOverride(0) = -12
        centerPositionOverride(1) = -8
        centerPositionOverride(2) = 0
        Dim jogLinePosition(2) As Double
        jogLinePosition(0) = -11
        jogLinePosition(1) = -8
        jogLinePosition(2) = 0
        Dim dimensionPosition(2) As Double
        dimensionPosition(0) = -10
        dimensionPosition(1) = -7.5
        dimensionPosition(2) = 0
        Dim dimensionTextOverride As String
        dimensionTextOverride = ""
        Dim dsJoggedDimForCircle As DraftSight.JoggedDimension
        Set dsJoggedDimForCircle = dsSketchMgr.InsertJoggedDimensionCircle(dsCircle, centerPositionOverride, jogLinePosition, dimensionPosition, dimensionTextOverride)
```

```
        'Print information about jogged Dimension
        PrintJoggedDimProperties dsJoggedDimForCircle
```

```
        'Draw an arc
        centerX = 2
        centerY = -6
        Dim arcRadius As Double
        arcRadius = 3
        Dim startAngle As Double
        startAngle = 0#
        Dim endAngle As Double
        endAngle = 3.14159265358979 / 3
        Dim dsArc As DraftSight.CircleArc
        Set dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, arcRadius, startAngle, endAngle)
```

```
        'Add jogged Dimension to arc
        centerPositionOverride(0) = 7
        centerPositionOverride(1) = -3
        jogLinePosition(0) = 7
        jogLinePosition(1) = -4
        dimensionPosition(0) = 5.5
        dimensionPosition(1) = -4.5
        Dim dsJoggedDimForArc As DraftSight.JoggedDimension
        Set dsJoggedDimForArc = dsSketchMgr.InsertJoggedDimensionArc(dsArc, centerPositionOverride, jogLinePosition, dimensionPosition, dimensionTextOverride)
```

```
        'Print information about jogged Dimension
        PrintJoggedDimProperties dsJoggedDimForArc
    End Sub
```

```
    Sub DrawRadialDimension(ByVal dsSketchMgr As DraftSight.SketchManager)
        'Draw a circle
        Dim centerX As Double
        centerX = 2
        Dim centerY As Double
        centerY = 2
        Dim centerZ As Double
        centerZ = 0
        Dim radius As Double
        radius = 3
        Dim dsCircle As DraftSight.Circle
        Set dsCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Draw an arc
        centerX = 10
        centerY = 2
        Dim arcRadius As Double
        arcRadius = 3
        Dim startAngle As Double
        startAngle = 0#
        Dim endAngle As Double
        endAngle = 3.14159265358979 / 3
        Dim dsArc As DraftSight.CircleArc
        Set dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, arcRadius, startAngle, endAngle)
```

```
        'Add radius Dimension to circle
        Dim dimPosition(2) As Double
        dimPosition(0) = 7
        dimPosition(1) = 6
        dimPosition(2) = 0
        Dim dimTextOverride As String
        dimTextOverride = ""
        Dim dsRadialCircleDim As DraftSight.RadialDimension
        Set dsRadialCircleDim = dsSketchMgr.InsertRadialDimensionCircle(dsCircle, dimPosition, dimTextOverride)
```

```
        'Print information about radius Dimension
        PrintRadialDimProperties dsRadialCircleDim
```

```
        'Add radius Dimension to arc
        dimPosition(0) = 16
        dimPosition(1) = 3
        Dim dsRadialArcDim As DraftSight.RadialDimension
        Set dsRadialArcDim = dsSketchMgr.InsertRadialDimensionArc(dsArc, dimPosition, dimTextOverride)
```

```
        'Print information about radius Dimension
        PrintRadialDimProperties dsRadialArcDim
    End Sub
```

```
    Sub DrawDiameterDimension(ByVal dsSketchMgr As DraftSight.SketchManager)
        'Draw a circle
        Dim centerX As Double
        centerX = 2
        Dim centerY As Double
        centerY = 2
        Dim centerZ As Double
        centerZ = 0
        Dim radius As Double
        radius = 3
        Dim dsCircle As DraftSight.Circle
        Set dsCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Draw an arc
        centerX = 10
        centerY = 2
        Dim arcRadius As Double
        arcRadius = 3
        Dim startAngle As Double
        startAngle = 0#
        Dim endAngle As Double
        endAngle = 3.14159265358979 / 3
        Dim dsArc As DraftSight.CircleArc
        Set dsArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, arcRadius, startAngle, endAngle)
```

```
        'Add diameter Dimension to circle
        Dim dimPosition(2) As Double
        dimPosition(0) = 3
        dimPosition(1) = 8
        dimPosition(2) = 0
```

```
        'No text override - empty string
        Dim dimTextOverride As String
        dimTextOverride = ""
        Dim dsDiameterCircleDim As DraftSight.DiameterDimension
        Set dsDiameterCircleDim = dsSketchMgr.InsertDiameterDimensionCircle(dsCircle, dimPosition, dimTextOverride)
```

```
        'Print information about diameter Dimension
        PrintDiameterDimProperties dsDiameterCircleDim
```

```
        'Add diameter Dimension to arc
        dimPosition(0) = 14
        dimPosition(1) = 6
        Dim dsDiameterArcDim As DraftSight.DiameterDimension
        Set dsDiameterArcDim = dsSketchMgr.InsertDiameterDimensionArc(dsArc, dimPosition, dimTextOverride)
```

```
        'Print information about diameter Dimension
        PrintDiameterDimProperties dsDiameterArcDim
    End Sub
```

```
    Sub DrawRotatedDimension(ByVal dsSketchMgr As DraftSight.SketchManager)
        'Draw line
        Dim startX As Double
        startX = 10
        Dim startY As Double
        startY = -5
        Dim startZ As Double
        startZ = 0
        Dim endX As Double
        endX = 14
        Dim endY As Double
        endY = -5
        Dim endZ As Double
        endZ = 0
        Dim dsLine As DraftSight.Line
        Set dsLine = dsSketchMgr.InsertLine(startX, startY, startZ, endX, endY, endZ)
```

```
        'Draw rotated Dimension
        Dim extLine1Point(2) As Double
        extLine1Point(0) = startX
        extLine1Point(1) = startY
        extLine1Point(2) = startZ
        Dim extLine2Point(2) As Double
        extLine2Point(0) = endX
        extLine2Point(1) = endY
        extLine2Point(2) = endZ
        Dim dimensionLinePosition(2) As Double
        dimensionLinePosition(0) = 16
        dimensionLinePosition(1) = -6
        dimensionLinePosition(2) = 0
        Dim dimTextOverride As String
        dimTextOverride = ""
```

```
        'Angle 45 degrees (in radians)
        Dim rotationAngle As Double
        rotationAngle = 3.14159265358979 / 4
        Dim dsRotatedDim As DraftSight.RotatedDimension
        Set dsRotatedDim = dsSketchMgr.InsertRotatedDimension(extLine1Point, extLine2Point, dimensionLinePosition, dimTextOverride, rotationAngle)
```

```
        'Print information about rotated Dimension
        PrintRotatedDimProperties dsRotatedDim
    End Sub
```

```
    Sub PrintArcLengthDimProperties(ByVal dsArcLengthDim As ArcLengthDimension)
        Debug.Print ("  Arc length Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As DraftSight.GeneralDimension
        Set dsGeneralDim = dsArcLengthDim.GetGeneralDimension()
        PrintGeneralDimProperties dsGeneralDim
```

```
        'Print specific parameters for arc length Dimension
        Debug.Print ("    ArcSymbolType = " & dsArcLengthDim.ArcSymbolType)
        Debug.Print ("    HasLeader = " & dsArcLengthDim.HasLeader)
        Debug.Print ("    IsPartial = " & dsArcLengthDim.IsPartial)
        Dim x As Double, y As Double, z As Double
```

```
        'Get center point
        dsArcLengthDim.GetCenterPoint x, y, z
        Debug.Print ("    Center point (" & x & "," & y & "," & z & ")")
```

```
        'Get arc point
        dsArcLengthDim.GetArcPoint x, y, z
        Debug.Print ("    Arc point (" & x & "," & y & "," & z & ")")
```

```
        'Get extension line 1 point
        dsArcLengthDim.GetExtensionLine1Point x, y, z
        Debug.Print ("    Extension line 1 point (" & x & "," & y & "," & z & ")")
```

```
        'Get extension line 2 point
        dsArcLengthDim.GetExtensionLine2Point x, y, z
        Debug.Print ("    Extension line 2 point (" & x & "," & y & "," & z & ")")
    End Sub
```

```
    Sub PrintRadialDimProperties(ByVal dsRadialDim As RadialDimension)
        Debug.Print ("  Radius Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As DraftSight.GeneralDimension
        Set dsGeneralDim = dsRadialDim.GetGeneralDimension()
        PrintGeneralDimProperties dsGeneralDim
```

```
        'Print specific parameters for radius Dimension
        Dim x As Double, y As Double, z As Double
```

```
        'Get center point
        dsRadialDim.GetCenterPoint x, y, z
        Debug.Print ("    Center point (" & x & "," & y & "," & z & ")")
```

```
        'Get defining point
        dsRadialDim.GetDefiningPoint x, y, z
        Debug.Print ("    Defining point (" & x & "," & y & "," & z & ")")
```

```
        'Print leader length value
        Debug.Print ("    Leader length = " & dsRadialDim.LeaderLength)
    End Sub
```

```
    Sub PrintDiameterDimProperties(ByVal dsDiameterDim As DiameterDimension)
        Debug.Print ("  Diameter Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As DraftSight.GeneralDimension
        Set dsGeneralDim = dsDiameterDim.GetGeneralDimension()
        PrintGeneralDimProperties dsGeneralDim
```

```
        'Print specific parameters for diameter Dimension
        Dim x As Double, y As Double, z As Double

        'Get defining point
        dsDiameterDim.GetDefiningPoint x, y, z
        Debug.Print ("    Defining point (" & x & "," & y & "," & z & ")")
```

```
        'Get far defining point
        dsDiameterDim.GetFarDefiningPoint x, y, z
        Debug.Print ("    Far defining point (" & x & "," & y & "," & z & ")")

        'Print leader length value
        Debug.Print ("    Leader length = " & dsDiameterDim.LeaderLength)
    End Sub
```

```
    Sub PrintJoggedDimProperties(ByVal dsJoggedDim As JoggedDimension)
        Debug.Print ("  Jogged Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As DraftSight.GeneralDimension
        Set dsGeneralDim = dsJoggedDim.GetGeneralDimension()
        PrintGeneralDimProperties dsGeneralDim
```

```
        'Print specific parameters for jogged Dimension
        Debug.Print ("    Jog angle = " & dsJoggedDim.JogAngle)
        Dim x As Double, y As Double, z As Double
```

```
        'Get center point
        dsJoggedDim.GetCenterPoint x, y, z
        Debug.Print ("    Center point (" & x & "," & y & "," & z & ")")

        'Get chord point
        dsJoggedDim.GetChordPoint x, y, z
        Debug.Print ("    Chord point (" & x & "," & y & "," & z & ")")

        'Get jog point
        dsJoggedDim.GetJogPoint x, y, z
        Debug.Print ("    Jog point (" & x & "," & y & "," & z & ")")

        'Get override center point
        dsJoggedDim.GetOverrideCenterPoint x, y, z
        Debug.Print ("    Override center point (" & x & "," & y & "," & z & ")")
    End Sub
```

```
    Sub PrintRotatedDimProperties(ByVal dsRotatedDim As RotatedDimension)
        Debug.Print ("  Rotated Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As DraftSight.GeneralDimension
        Set dsGeneralDim = dsRotatedDim.GetGeneralDimension()
        PrintGeneralDimProperties dsGeneralDim
```

```
        'Print specific parameters for rotated Dimension
        Debug.Print ("    Rotation angle = " & dsRotatedDim.Rotation)
        Dim x As Double, y As Double, z As Double
```

```
        'Get Dimension line point
        dsRotatedDim.GetDimensionLinePoint x, y, z
        Debug.Print ("    Dimension line point (" & x & "," & y & "," & z & ")")
```

```
        'Get extension line 1 point
        dsRotatedDim.GetExtensionLine1Point x, y, z
        Debug.Print ("    Extension line 1 point (" & x & "," & y & "," & z & ")")
```

```
        'Get extension line 2 point
        dsRotatedDim.GetExtensionLine2Point x, y, z
        Debug.Print ("    Extension line 2 point (" & x & "," & y & "," & z & ")")
    End Sub
```

```
    Sub PrintGeneralDimProperties(ByVal dsGeneralDim As GeneralDimension)
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Debug.Print ("    Dimension style = " & dsGeneralDim.DimensionStyle)
        Debug.Print ("    Handle = " & dsGeneralDim.Handle)
        Debug.Print ("    Measurement = " & dsGeneralDim.Measurement)
        Debug.Print ("    Related = " & dsGeneralDim.Related)
        Debug.Print ("    Text override = " & dsGeneralDim.TextOverride)
        Debug.Print ("    TextRotation = " & dsGeneralDim.TextRotation)

        'Get text position
        Dim x As Double, y As Double
        dsGeneralDim.GetTextPosition x, y
        Debug.Print ("    Text position (" & x & "," & y & ")")
    End Sub
```
