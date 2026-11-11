---
title: "Create and Apply DimensionStyle Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Apply_DimensionStyle_Example_VBNET.htm"
---

# Create and Apply DimensionStyle Example (VB.NET)

This example shows how to create, activate, and apply a new DimensionStyle. This example also shows how to create arc length, jogged, rotated, radius, and diameter Dimensions for circles, arcs, and a line.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this project into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
' 4. Set a breakpoint at:
'    dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
' 5. Start DraftSight and open a document.
' 6. Click Start Debugging.
'
' Postconditions:
' 1. A new DimensionStyle named SampleDimStyle is created and
'    activated.
' 2. Arc length, jogged, rotated, radius, and diameter dimensions
'    are created for circles, arcs, and a line, using the new
'    DimensionStyle.
' 3. Examine the Output or Immediate window.
' 4. Click Continue.
' 5. Examine the drawing.
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
    Dim dsApp As DraftSight.Interop.dsAutomation.Application
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
        'Get DimensionStyle manager
        Dim dsDimStyleManager As DimensionStyleManager = dsDoc.GetDimensionStyleManager()
```

```
        'Create DimensionStyle named SampleDimStyle
        Dim createDimStyleResult As dsCreateObjectResult_e
        Dim dimStyleName As String = "SampleDimStyle"
        Dim dsDimStyle As DimensionStyle = Nothing
        dsDimStyleManager.CreateDimensionStyle(dimStyleName, dsDimStyle, createDimStyleResult)
        If dsCreateObjectResult_e.dsCreateObjectResult_Error = createDimStyleResult OrElse dsCreateObjectResult_e.dsCreateObjectResult_AlreadyExists = createDimStyleResult OrElse dsDimStyle Is Nothing Then
            MsgBox("Failed to create " & dimStyleName & " DimensionStyle, or DimensionStyle already exists.")
            Return
        End If
```

```
        SetDimensionStyleSettings(dsDimStyle)
```

```
        'Activate DimensionStyle
        dsDimStyle.Activate()
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
        'Draw arc length Dimension
        DrawArcLengthDimension(dsSketchMgr)
```

```
        'Draw jogged Dimension for circle and arc
        DrawJoggedDimension(dsSketchMgr)
```

```
        'Draw rotated Dimension
        DrawRotatedDimension(dsSketchMgr)
```

```
        'Draw radius Dimension for circle and arc
        DrawRadialDimension(dsSketchMgr)
```

```
        'Draw diameter Dimension for circle and arc
        DrawDiameterDimension(dsSketchMgr)
```

```
        'Zoom to fit
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
    End Sub
```

```
    Sub SetDimensionStyleSettings(ByVal dsDimStyle As DimensionStyle)
        'Get DimensionStyle arrows options
        Dim dsArrowsDimStyleOptions As DimensionStyleArrowsOptions = dsDimStyle.GetDimensionStyleArrowsOptions()
```

```
        'Set start and end arrow types
        dsArrowsDimStyleOptions.SetStartArrow(dsDimensionArrowType_e.dsDimensionArrowType_ClosedBlank, String.Empty)
        dsArrowsDimStyleOptions.SetEndArrow(dsDimensionArrowType_e.dsDimensionArrowType_ClosedBlank, String.Empty)
```

```
        'Get DimensionStyle line options
        Dim dsLineDimStyleOptions As DimensionStyleLineOptions = dsDimStyle.GetDimensionStyleLineOptions()
```

```
        'Set Dimension line color
        Dim dsColor As Color = dsLineDimStyleOptions.DimensionLineColor
        dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Green)
        dsLineDimStyleOptions.DimensionLineColor = dsColor
```

```
        'Set extension line color
        dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Yellow)
        dsLineDimStyleOptions.ExtensionLineColor = dsColor
```

```
        'Get DimensionStyle radius and diameter Dimension options
        Dim dsRadialAndDiameterDimStyleOptions As DimensionStyleRadialDiameterDimensionOptions = dsDimStyle.GetDimensionStyleRadialDiameterDimensionOptions()
```

```
        'Set jog angle 45 degrees (in radians)
        dsRadialAndDiameterDimStyleOptions.RadiusDimensionJogAngle = Math.PI / 4
```

```
        'Set center mark
        Dim markSize As Double = 0.05
        dsRadialAndDiameterDimStyleOptions.SetCenterMarkDisplay(dsDimensionCenterMarkDisplay_e.dsDimensionCenterMarkDisplay_AsMark, markSize)
```

```
        'Get Dimension style text options
        Dim dsTextOptions As DimensionStyleTextOptions = dsDimStyle.GetDimensionStyleTextOptions()
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
    Sub DrawArcLengthDimension(ByVal dsSketchMgr As SketchManager)
        'Add arc to drawing
        Dim centerX As Double = -8
        Dim centerY As Double = 1
        Dim centerZ As Double = 0
        Dim radius As Double = 5
        Dim startAngle As Double = Math.PI / 6
        Dim endAngle As Double = Math.PI
        Dim dsArc As CircleArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, radius, startAngle, endAngle)
```

```
        'Add arc length Dimension
        Dim dimensionPosition As Double() = New Double() {-6, 6, 0}
        Dim dimensionTextOverride As String = String.Empty
        Dim dsArcLengthDim As ArcLengthDimension = dsSketchMgr.InsertArcLengthDimension(dsArc, dimensionPosition, dimensionTextOverride)
```

```
        'Print information about arc length Dimension
        PrintArcLengthDimProperties(dsArcLengthDim)
```

```
        'Add a partial arc length Dimension
        Dim firstPoint As Double() = New Double() {-4, 3, 0}
        Dim secondPoint As Double() = New Double() {-7, 6, 0}
        dimensionPosition(0) = -6
        dimensionPosition(1) = 7
        Dim dsArcLengthPartialDim As ArcLengthDimension = dsSketchMgr.InsertArcLengthDimensionPartial(dsArc, firstPoint, secondPoint, dimensionPosition, dimensionTextOverride)
```

```
        'Print information about partial arc length Dimension
        PrintArcLengthDimProperties(dsArcLengthDim)
    End Sub
```

```
    Sub DrawJoggedDimension(ByVal dsSketchMgr As SketchManager)
        'Draw a circle
        Dim centerX As Double = -7, centerY As Double = -5, centerZ As Double = 0
        Dim radius As Double = 3
        Dim dsCircle As Circle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Add jogged Dimension to circle
        Dim centerPositionOverride As Double() = New Double() {-12, -8, 0}
        Dim jogLinePosition As Double() = New Double() {-11, -8, 0}
        Dim dimensionPosition As Double() = New Double() {-10, -7.5, 0}
        Dim dimensionTextOverride As String = String.Empty
        Dim dsJoggedDimForCircle As JoggedDimension = dsSketchMgr.InsertJoggedDimensionCircle(dsCircle, centerPositionOverride, jogLinePosition, dimensionPosition, dimensionTextOverride)
```

```
        'Print information about jogged Dimension
        PrintJoggedDimProperties(dsJoggedDimForCircle)
```

```
        'Draw an arc
        centerX = 2
        centerY = -6
        Dim arcRadius As Double = 3
        Dim startAngle As Double = 0.0
        Dim endAngle As Double = Math.PI / 3
        Dim dsArc As CircleArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, arcRadius, startAngle, endAngle)
```

```
        'Add jogged Dimension to arc
        centerPositionOverride(0) = 7
        centerPositionOverride(1) = -3
        jogLinePosition(0) = 7
        jogLinePosition(1) = -4
        dimensionPosition(0) = 5.5
        dimensionPosition(1) = -4.5
        Dim dsJoggedDimForArc As JoggedDimension = dsSketchMgr.InsertJoggedDimensionArc(dsArc, centerPositionOverride, jogLinePosition, dimensionPosition, dimensionTextOverride)
```

```
        'Print information about jogged Dimension
        PrintJoggedDimProperties(dsJoggedDimForArc)
    End Sub
```

```
    Sub DrawRadialDimension(ByVal dsSketchMgr As SketchManager)
        'Draw a circle
        Dim centerX As Double = 2, centerY As Double = 2, centerZ As Double = 0
        Dim radius As Double = 3
        Dim dsCircle As Circle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Draw an arc
        centerX = 10
        centerY = 2
        Dim arcRadius As Double = 3
        Dim startAngle As Double = 0.0
        Dim endAngle As Double = Math.PI / 3
        Dim dsArc As CircleArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, arcRadius, startAngle, endAngle)
```

```
        'Add radius Dimension to circle
        Dim dimPosition As Double() = New Double() {7, 6, 0}
        Dim dimTextOverride As String = String.Empty
        Dim dsRadialCircleDim As RadialDimension = dsSketchMgr.InsertRadialDimensionCircle(dsCircle, dimPosition, dimTextOverride)
```

```
        'Print information about radius Dimension
        PrintRadialDimProperties(dsRadialCircleDim)
```

```
        'Add radius Dimension to arc
        dimPosition(0) = 16
        dimPosition(1) = 3
        Dim dsRadialArcDim As RadialDimension = dsSketchMgr.InsertRadialDimensionArc(dsArc, dimPosition, dimTextOverride)
```

```
        'Print information about radius Dimension
        PrintRadialDimProperties(dsRadialArcDim)
    End Sub
```

```
    Sub DrawDiameterDimension(ByVal dsSketchMgr As SketchManager)
        'Draw a circle
        Dim centerX As Double = 2, centerY As Double = 2, centerZ As Double = 0
        Dim radius As Double = 3
        Dim dsCircle As Circle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Draw an arc
        centerX = 10
        centerY = 2
        Dim arcRadius As Double = 3
        Dim startAngle As Double = 0.0
        Dim endAngle As Double = Math.PI / 3
        Dim dsArc As CircleArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, arcRadius, startAngle, endAngle)
```

```
        'Add diameter Dimension to circle
        Dim dimPosition As Double() = New Double() {3, 8, 0}
        'No text override - empty string
        Dim dimTextOverride As String = String.Empty
        Dim dsDiameterCircleDim As DiameterDimension = dsSketchMgr.InsertDiameterDimensionCircle(dsCircle, dimPosition, dimTextOverride)
```

```
        'Print information about diameter Dimension
        PrintDiameterDimProperties(dsDiameterCircleDim)
```

```
        'Add diameter Dimension to arc
        dimPosition(0) = 14
        dimPosition(1) = 6
        Dim dsDiameterArcDim As DiameterDimension = dsSketchMgr.InsertDiameterDimensionArc(dsArc, dimPosition, dimTextOverride)
```

```
        'Print information about diameter Dimension
        PrintDiameterDimProperties(dsDiameterArcDim)
    End Sub
```

```
    Sub DrawRotatedDimension(ByVal dsSketchMgr As SketchManager)
        'Draw line
        Dim startX As Double = 10
        Dim startY As Double = -5
        Dim startZ As Double = 0
        Dim endX As Double = 14
        Dim endY As Double = -5
        Dim endZ As Double = 0
        Dim dsLine As Line = dsSketchMgr.InsertLine(startX, startY, startZ, endX, endY, endZ)
```

```
        'Draw rotated Dimension
        Dim extLine1Point As Double() = New Double() {startX, startY, startZ}
        Dim extLine2Point As Double() = New Double() {endX, endY, endZ}
        Dim dimensionLinePosition As Double() = New Double() {16, -6, 0}
        Dim dimTextOverride As String = String.Empty
```

```
        'Angle 45 degrees (in radians)
        Dim rotationAngle As Double = Math.PI / 4
        Dim dsRotatedDim As RotatedDimension = dsSketchMgr.InsertRotatedDimension(extLine1Point, extLine2Point, dimensionLinePosition, dimTextOverride, rotationAngle)
```

```
        'Print information about rotated Dimension
        PrintRotatedDimProperties(dsRotatedDim)
    End Sub
```

```
    Sub PrintArcLengthDimProperties(ByVal dsArcLengthDim As ArcLengthDimension)
        Debug.Print(Environment.NewLine & "  Arc length Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As GeneralDimension = dsArcLengthDim.GetGeneralDimension()
        PrintGeneralDimProperties(dsGeneralDim)
```

```
        'Print specific parameters for arc length Dimension
        Debug.Print("    ArcSymbolType = " & Convert.ToString(dsArcLengthDim.ArcSymbolType))
        Debug.Print("    HasLeader = " & Convert.ToString(dsArcLengthDim.HasLeader))
        Debug.Print("    IsPartial = " & Convert.ToString(dsArcLengthDim.IsPartial))
```

```
        Dim x As Double, y As Double, z As Double
        'Get center point
        dsArcLengthDim.GetCenterPoint(x, y, z)
        Debug.Print("    Center point (" & x & "," & y & "," & z & ")")
```

```
        'Get arc point
        dsArcLengthDim.GetArcPoint(x, y, z)
        Debug.Print("    Arc point (" & x & "," & y & "," & z & ")")
```

```
        'Get extension line 1 point
        dsArcLengthDim.GetExtensionLine1Point(x, y, z)
        Debug.Print("    Extension line 1 point (" & x & "," & y & "," & z & ")")
```

```
        'Get extension line 2 point
        dsArcLengthDim.GetExtensionLine2Point(x, y, z)
        Debug.Print("    Extension line 2 point (" & x & "," & y & "," & z & ")")
    End Sub
```

```
    Sub PrintRadialDimProperties(ByVal dsRadialDim As RadialDimension)
        Debug.Print(Environment.NewLine & "  Radius Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As GeneralDimension = dsRadialDim.GetGeneralDimension()
        PrintGeneralDimProperties(dsGeneralDim)
```

```
        'Print specific parameters for radius Dimension
        Dim x As Double, y As Double, z As Double
        'Get center point
        dsRadialDim.GetCenterPoint(x, y, z)
        Debug.Print("    Center point (" & x & "," & y & "," & z & ")")
```

```
        'Get defining point
        dsRadialDim.GetDefiningPoint(x, y, z)
        Debug.Print("    Defining point (" & x & "," & y & "," & z & ")")
```

```
        'Print leader length value
        Debug.Print("    Leader length = " & Convert.ToString(dsRadialDim.LeaderLength))
    End Sub
```

```
    Sub PrintDiameterDimProperties(ByVal dsDiameterDim As DiameterDimension)
        Debug.Print(Environment.NewLine & "  Diameter Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As GeneralDimension = dsDiameterDim.GetGeneralDimension()
        PrintGeneralDimProperties(dsGeneralDim)
```

```
        'Print specific parameters for diameter Dimension
        Dim x As Double, y As Double, z As Double
        'Get defining point
        dsDiameterDim.GetDefiningPoint(x, y, z)
        Debug.Print("    Defining point (" & x & "," & y & "," & z & ")")
```

```
        'Get far defining point
        dsDiameterDim.GetFarDefiningPoint(x, y, z)
        Debug.Print("    Far defining point (" & x & "," & y & "," & z & ")")
```

```
        'Print leader length value
        Debug.Print("    Leader length = " & Convert.ToString(dsDiameterDim.LeaderLength))
    End Sub
```

```
    Sub PrintJoggedDimProperties(ByVal dsJoggedDim As JoggedDimension)
        Debug.Print(Environment.NewLine & "  Jogged Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As GeneralDimension = dsJoggedDim.GetGeneralDimension()
        PrintGeneralDimProperties(dsGeneralDim)
```

```
        'Print specific parameters for jogged Dimension
        Debug.Print("    Jog angle = " & Convert.ToString(dsJoggedDim.JogAngle))
```

```
        Dim x As Double, y As Double, z As Double
        'Get center point
        dsJoggedDim.GetCenterPoint(x, y, z)
        Debug.Print("    Center point (" & x & "," & y & "," & z & ")")
```

```
        'Get chord point
        dsJoggedDim.GetChordPoint(x, y, z)
        Debug.Print("    Chord point (" & x & "," & y & "," & z & ")")
```

```
        'Get jog point
        dsJoggedDim.GetJogPoint(x, y, z)
        Debug.Print("    Jog point (" & x & "," & y & "," & z & ")")
```

```
        'Get override center point
        dsJoggedDim.GetOverrideCenterPoint(x, y, z)
        Debug.Print("    Override center point (" & x & "," & y & "," & z & ")")
    End Sub
```

```
    Sub PrintRotatedDimProperties(ByVal dsRotatedDim As RotatedDimension)
        Debug.Print(Environment.NewLine & "  Rotated Dimension parameters...")
```

```
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Dim dsGeneralDim As GeneralDimension = dsRotatedDim.GetGeneralDimension()
        PrintGeneralDimProperties(dsGeneralDim)
```

```
        'Print specific parameters for rotated Dimension
        Debug.Print("    Rotation angle = " & Convert.ToString(dsRotatedDim.Rotation))
```

```
        Dim x As Double, y As Double, z As Double
        'Get Dimension line point
        dsRotatedDim.GetDimensionLinePoint(x, y, z)
        Debug.Print("    Dimension line point (" & x & "," & y & "," & z & ")")
```

```
        'Get extension line 1 point
        dsRotatedDim.GetExtensionLine1Point(x, y, z)
        Debug.Print("    Extension line 1 point (" & x & "," & y & "," & z & ")")
```

```
        'Get extension line 2 point
        dsRotatedDim.GetExtensionLine2Point(x, y, z)
        Debug.Print("    Extension line 2 point (" & x & "," & y & "," & z & ")")
    End Sub
```

```
    Sub PrintGeneralDimProperties(ByVal dsGeneralDim As GeneralDimension)
        'Get general Dimension object, which contains common Dimension properties,
        'and print them
        Debug.Print("    Dimension style = " & Convert.ToString(dsGeneralDim.DimensionStyle))
        Debug.Print("    Handle = " & Convert.ToString(dsGeneralDim.Handle))
        Debug.Print("    Measurement = " & dsGeneralDim.Measurement.ToString())
        Debug.Print("    Related = " & dsGeneralDim.Related.ToString())
        Debug.Print("    Text override = " & Convert.ToString(dsGeneralDim.TextOverride))
        Debug.Print("    TextRotation = " & Convert.ToString(dsGeneralDim.TextRotation))
```

```
        'Get text position
        Dim x As Double, y As Double
        dsGeneralDim.GetTextPosition(x, y)
        Debug.Print("    Text position (" & x & "," & y & ")")
    End Sub
```

```
End Module
```
