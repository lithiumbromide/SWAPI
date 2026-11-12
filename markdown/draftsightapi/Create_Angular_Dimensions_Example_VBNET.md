---
title: "Create Angular Dimensions Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Angular_Dimensions_Example_VBNET.htm"
---

# Create Angular Dimensions Example (VB.NET)

This example shows how to create angular Dimensions using 3 points, 2 lines, and an arc.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this project into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation
' 4. Set a breakpoint at:
'    dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
' 5. Start DraftSight and open a document.
' 6. Click Start Debugging.
'
' Postconditions:
' 1. Angular Dimensions using 3 points, 2 lines, and an arc are created.
' 2. Examine the Output or Immediate window.
' 3. Click Continue.
' 4. Examine the drawing.
'------------------------------------------------------------
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
```

```
        'Connect to the DraftSight application
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get the active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get the model space
        Dim dsModel As Model = dsDoc.GetModel()
```

```
        'Get the sketch manager
        Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()
```

```
        'Add an angular Dimension using three points
        Dim dsAngular3PointDim As AngularDimension = AddAngularDimensionUsing3Points(dsSketchMgr)
```

```
        'Print the angular Dimension's properties
        PrintAngularDimProperties(dsAngular3PointDim)
```

```
        'Add the angular Dimension using two lines
        Dim dsAngular2LinesDim As AngularDimension = AddAngularDimensionUsing2Lines(dsSketchMgr)
```

```
        'Print the angular Dimension's properties
        PrintAngularDimProperties(dsAngular2LinesDim)
```

```
        'Add an angular Dimension for the arc
        Dim dsAngularArcDim As AngularDimension = AddAngularDimensionForArc(dsSketchMgr)
```

```
        'Print the angular Dimension's properties
        PrintAngularDimProperties(dsAngularArcDim)
```

```
        'Zoom to fit
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
    End Sub
```

```
    Private Function AddAngularDimensionForArc(ByVal dsSketchMgr As SketchManager) As AngularDimension
        'Draw an arc
        Dim centerX As Double = 18, centerY As Double = 2, centerZ As Double = 0
        Dim radius As Double = 3
        Dim startAngle As Double = 0.0, endAngle As Double = Math.PI / 2
        Dim dsArc As CircleArc = dsSketchMgr.InsertArc(centerX, centerY, centerZ, radius, startAngle, endAngle)
```

```
        'Angular Dimension's position
        Dim dimPosition As Double() = New Double() {20, 5, 0}
```

```
        'Text override
        Dim dimTextOverride As String = "AngularDimArc"
```

```
        Dim dsAngularDim As AngularDimension = dsSketchMgr.InsertAngularDimensionArc(dsArc, dimPosition, dimTextOverride)
```

```
        Debug.Print(Environment.NewLine + "An angular Dimension for an arc was added.")
```

```
        Return dsAngularDim
    End Function
```

```
    Private Function AddAngularDimensionUsing2Lines(ByVal dsSketchMgr As SketchManager) As AngularDimension
        'Draw two lines for an angular Dimension
        Dim dsFirstLine As Line = dsSketchMgr.InsertLine(7, 0, 0, 10, 3, 0)
        Dim dsSecondLine As Line = dsSketchMgr.InsertLine(12, 0, 0, 15, 2, 0)
```

```
        'Angular Dimension position
        Dim dimPosition As Double() = New Double() {13, 4, 0}
```

```
        'No text override - empty string
        Dim dimTextOverride As String = String.Empty
```

```
        Dim dsAngularDim As AngularDimension = dsSketchMgr.InsertAngularDimension2Line(dsFirstLine, dsSecondLine, dimPosition, dimTextOverride)
```

```
        Debug.Print(Environment.NewLine + "An angular Dimension using two lines was added.")
```

```
        Return dsAngularDim
    End Function
```

```
    Private Function AddAngularDimensionUsing3Points(ByVal dsSketchMgr As SketchManager) As AngularDimension
        'Angular Dimension parameters
        Dim centerPoint As Double() = New Double() {0, 0, 0}
        Dim angleStartPoint As Double() = New Double() {2, 2, 0}
        Dim angleEndPoint As Double() = New Double() {2, 4, 0}
        Dim dimPosition As Double() = New Double() {5, 5, 0}
```

```
        'No text override - empty string
        Dim dimTextOverride As String = String.Empty
```

```
        Dim dsAngular3PointDim As AngularDimension = dsSketchMgr.InsertAngularDimension3Point(centerPoint, angleStartPoint, angleEndPoint, dimPosition, dimTextOverride)
```

```
        Debug.Print(Environment.NewLine + "An angular Dimension using three points was added.")
```

```
        Return dsAngular3PointDim
    End Function
```

```
    Private Sub PrintAngularDimProperties(ByVal dsAngularDim As AngularDimension)
        Debug.Print("  Angular Dimension parameters...")
```

```
        Debug.Print("    Type = " + dsAngularDim.Type.ToString())
```

```
        'Get general Dimension object, which contains common Dimension properties
        Dim dsGeneralDim As GeneralDimension = dsAngularDim.GetGeneralDimension()
```

```
        Debug.Print("    Dimension style = " + dsGeneralDim.DimensionStyle)
        Debug.Print("    Handle = " + dsGeneralDim.Handle)
        Debug.Print("    Measurement (in radians) = " + dsGeneralDim.Measurement.ToString())
        Debug.Print("    Related = " + dsGeneralDim.Related.ToString())
        Debug.Print("    Text override = " + dsGeneralDim.TextOverride)
        Debug.Print("    Text rotation = " + dsGeneralDim.TextRotation.ToString)
```

```
        'Get text position
        Dim x As Double, y As Double
        dsGeneralDim.GetTextPosition(x, y)
        Debug.Print("    Text position (" + x.ToString + "," + y.ToString + ")")
```

```
        'Print specific parameters for angular Dimension
        Dim z As Double
        'Get center point
        dsAngularDim.GetCenterPoint(x, y, z)
        Debug.Print("    Center point (" + x.ToString + "," + y.ToString + "," + z.ToString + ")")
```

```
        'Get arc point
        dsAngularDim.GetArcPoint(x, y, z)
        Debug.Print("    Arc point (" + x.ToString + "," + y.ToString + "," + z.ToString + ")")
```

```
        'Get first line's start point
        dsAngularDim.GetLine1Point(x, y, z)
        Debug.Print("    Line1's start point (" + x.ToString + "," + y.ToString + "," + z.ToString + ")")
```

```
        'Get first line end point
        dsAngularDim.GetLine1EndPoint(x, y, z)
        Debug.Print("    Line1's end point (" + x.ToString + "," + y.ToString + "," + z.ToString + ")")
```

```
        'Get second line start point
        dsAngularDim.GetLine2Point(x, y, z)
        Debug.Print("    Line2's start point (" + x.ToString + "," + y.ToString + "," + z.ToString + ")")
```

```
        'Get second line end point
        dsAngularDim.GetLine2EndPoint(x, y, z)
        Debug.Print("    Line2's end point (" + x.ToString + "," + y.ToString + "," + z.ToString + ")")
    End Sub
```

```
End Module
```
