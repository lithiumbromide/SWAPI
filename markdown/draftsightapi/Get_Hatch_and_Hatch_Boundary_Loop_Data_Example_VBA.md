---
title: "Get Hatch and Hatch Boundary Loop Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBA.htm"
---

# Get Hatch and Hatch Boundary Loop Data Example (VBA)

This example shows how to get Hatch and Hatch boundary loop data.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight, construct a Circle, Rectangle, Spline, or
'    Ellipse, and apply a Hatch to the entity.
' 5. Open the Immediate window.
' 6. Run the macro.
'
' Postconditions:
' 1. When the prompt appears in the DraftSight command window to
'    select an entity, select the entity with the Hatch.
' 2. The selected entity's Hatch and Hatch boundary loop data is printed
'    to the Immediate Window.
'----------------------------------------------------------------
Option Explicit
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim dsSelectionMgr As DraftSight.SelectionManager
    Dim dsSelectionFilter As DraftSight.SelectionFilter
```

```
    Sub main()
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument
    If dsDoc Is Nothing Then
        MsgBox ("There are no open documents in DraftSight.")
        End
    End If

    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get Selection Manager
    Set dsSelectionMgr = dsDoc.GetSelectionManager
```

```
    'Get selection filter
     Set dsSelectionFilter = dsSelectionMgr.GetSelectionFilter
```

```
    'Clear selection filter
    dsSelectionFilter.Clear
```

```
    'Add Hatch entity to the selection filter
    dsSelectionFilter.AddEntityType dsObjectType_e.dsHatchType
```

```
    'Activate selection filter
    dsSelectionFilter.Active = True
```

```
    'Get command message object
    Dim dsCommandMessage As CommandMessage
    Set dsCommandMessage = dsApp.GetCommandMessage
```

```
    'Prompt user to select a Hatch entity
    'and get whether selected entity is a Hatch entity
    Dim singleSelection As Boolean
    singleSelection = True
    Dim prompt As String
    prompt = "Please select a Hatch entity."
    Dim errorMessage As String
    errorMessage = "Selected entity is not a Hatch entity."
    If dsCommandMessage.PromptForSelection(singleSelection, prompt, errorMessage) Then
            'Get selected entity
            Dim index As Long
            index = 0
            Dim entityType As dsObjectType_e
            Dim selectedEntity As Object
            Set selectedEntity = dsSelectionMgr.GetSelectedObject(dsSelectionSetType_e.dsSelectionSetType_Previous, index, entityType)
```

```
            If dsObjectType_e.dsHatchType <> entityType Then
                MsgBox (entityType & " was selected, but should be Hatch entity.")
            Else
                Dim dsHatch As Hatch
                Set dsHatch = selectedEntity
                PrintHatchParameters dsHatch
            End If
        End If
    End Sub
```

```
        Sub PrintHatchParameters(ByVal dsHatch As Hatch)
        Debug.Print ("Hatch parameters:")
```

```
        Debug.Print ("Color = " & dsHatch.Color.GetNamedColor)
        Debug.Print ("LineScale = " & dsHatch.LineScale)
        Debug.Print ("LineStyle = " & dsHatch.LineStyle)
        Debug.Print ("LineWeight = " & dsHatch.LineWeight)
        Debug.Print ("Layer = " & dsHatch.Layer)
        Debug.Print ("Visible = " & dsHatch.Visible)
        Debug.Print ("Erased = " & dsHatch.Erased)
        Debug.Print ("Handle = " & dsHatch.Handle)
```

```
        Dim x1 As Double, y1 As Double, z1 As Double
        Dim x2 As Double, y2 As Double, z2 As Double
        dsHatch.GetBoundingBox x1, y1, z1, x2, y2, z2
        Debug.Print ("BoundingBox: " & x1 & ", " & y1 & ", " & z1 & ", " & x2 & ", " & y2 & ", " & z2)
```

```
        'Iterate through Hatch boundary loops
        Dim loopsCount As Long
        loopsCount = dsHatch.GetBoundaryLoopsCount()
        Debug.Print ("Count of loops = " & loopsCount)
        Dim index As Long
        For index = 0 To loopsCount - 1
            Debug.Print ("Loop(" & index & "):")
```

```
            'Get Hatch boundary loop
            Dim dsHatchBoundaryLoop As DraftSight.HatchBoundaryLoop
            Set dsHatchBoundaryLoop = dsHatch.GetHatchBoundaryLoop(index)
```

```
            Debug.Print ("Type = " & dsHatchBoundaryLoop.Type)
            Debug.Print ("IsPolyline = " & dsHatchBoundaryLoop.IsPolyLine)
```

```
            If dsHatchBoundaryLoop.IsPolyLine Then
                'Get 2D PolyLine boundary loop data
                GetPolyLineBoundaryLoopData dsHatchBoundaryLoop
            Else
                'Get edges count
                Dim edgesCount As Long
                edgesCount = dsHatchBoundaryLoop.GetEdgesCount()
                Debug.Print ("Edges count = " & edgesCount)
                Dim edgeIndex As Long
                For edgeIndex = 0 To edgesCount - 1
                    Dim edgeType As dsHatchEdgeType_e
                    edgeType = dsHatchBoundaryLoop.GetEdgeType(edgeIndex)
                    Debug.Print ("Edge type = " & edgeType)
```

```
                    Select Case edgeType
                        Case dsHatchEdgeType_e.dsHatchEdgeType_Line
                            If True Then
                                'Get Line edge data
                                GetLineEdgeData dsHatchBoundaryLoop, edgeIndex
                            End If
                        Case dsHatchEdgeType_e.dsHatchEdgeType_CircleArc
                            If True Then
                                'Get Circle edge data
                                GetArcEdgeData dsHatchBoundaryLoop, edgeIndex
                                End
                            End If
                        Case dsHatchEdgeType_e.dsHatchEdgeType_EllipseArc
                            If True Then
                                'Get Ellipse edge data
                                GetEllipseEdgeData dsHatchBoundaryLoop, edgeIndex
                            End If
                        Case dsHatchEdgeType_e.dsHatchEdgeType_Spline
                            If True Then
                                'Get Spline edge data
                                GetSplineEdgeData dsHatchBoundaryLoop, edgeIndex
                            End If
                    End Select
                Next
            End If
        Next
    End Sub
```

```
Sub GetSplineEdgeData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop, ByVal edgeIndex As Long)
        Dim degree As Long
        Dim rational As Boolean
        Dim periodic As Boolean
        Dim knotValues As Variant
        Dim controlPoints As Variant
        dsHatchBoundaryLoop.GetSplineEdgeData edgeIndex, degree, rational, periodic, knotValues, controlPoints
        Debug.Print ("Spline edge data:")
        Debug.Print ("   Degree = " & degree)
        Debug.Print ("   Rational = " & rational)
        Debug.Print ("   Periodic = " & periodic)
```

```
        If IsArray(knotValues) Then
            Dim knotValue As Double
            Dim index As Long
            index = 0
            For index = 0 To UBound(knotValues)
                Debug.Print ("   Knot(" & index & "):" & knotValues(index))
            Next
        End If
```

```
        If IsArray(controlPoints) Then
             Dim controlPointIndex As Long
             controlPointIndex = 0
             For index = 0 To UBound(controlPoints) - 1
 		Debug.Print (" Control point({0}): ({1},{2}), " & index & ", " & controlPoints(index) & ", " & controlPoints(index + 1))
                controlPointIndex = controlPointIndex + 1
             Next
        End If
    End Sub
```

```
    Sub GetEllipseEdgeData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop, ByVal edgeIndex As Long)
        Dim centerX As Double
        Dim centerY As Double
        Dim majorAxisX As Double
        Dim majorAxisY As Double
        Dim minorAxisLengthRatio As Double
        Dim startAngle As Double
        Dim endAngle As Double
        Dim isCounterclockwiseFlag As Boolean
        dsHatchBoundaryLoop.GetEllipseEdgeData edgeIndex, centerX, centerY, majorAxisX, majorAxisY, minorAxisLengthRatio, startAngle, endAngle, isCounterclockwiseFlag
        Debug.Print ("Ellipse edge data:")
        Debug.Print ("   Center X = " & centerX)
        Debug.Print ("   Center Y = " & centerY)
        Debug.Print ("   Major axis X = " & majorAxisX)
        Debug.Print ("   Major axis Y = " & majorAxisY)
        Debug.Print ("   Minor axis length ratio = " & minorAxisLengthRatio)
        Debug.Print ("   Start angle = " & startAngle)
        Debug.Print ("   End angle = " & endAngle)
        Debug.Print ("   Is counter-clockwise = " & isCounterclockwiseFlag)
    End Sub
```

```
    Sub GetArcEdgeData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop, ByVal edgeIndex As Long)
        Dim centerX As Double
        Dim centerY As Double
        Dim radius As Double
        Dim startAngle As Double
        Dim endAngle As Double
        Dim isCounterclockwiseFlag As Boolean
        dsHatchBoundaryLoop.GetArcEdgeData edgeIndex, centerX, centerY, radius, startAngle, endAngle, isCounterclockwiseFlag
        Debug.Print ("Arc edge data:")
        Debug.Print ("   Center X = " & centerX)
        Debug.Print ("   Center Y = " & centerY)
        Debug.Print ("   Radius = " & radius)
        Debug.Print ("   Start angle = " & startAngle)
        Debug.Print ("   End angle = " & endAngle)
        Debug.Print ("   Is counter-clockwise = " & isCounterclockwiseFlag)
    End Sub
```

```
    Sub GetLineEdgeData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop, ByVal edgeIndex As Long)
        Dim startPointX As Double
        Dim startPointY As Double
        Dim endPointX As Double
        Dim endPointY As Double
        dsHatchBoundaryLoop.GetLineEdgeData edgeIndex, startPointX, startPointY, endPointX, endPointY
        Debug.Print ("Line edge data:")
        Debug.Print ("   Start point X = " & startPointX)
        Debug.Print ("   Start Point Y = " & startPointY)
        Debug.Print ("   End point X = " & endPointX)
        Debug.Print ("   End point Y = " & endPointY)
    End Sub
```

```
    Sub GetPolyLineBoundaryLoopData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop)
        Dim hasBulge As Boolean
        Dim isClosed As Boolean
        Dim coordinates As Object
        Dim bulges As Object
        dsHatchBoundaryLoop.GetPolyLineBoundaryLoopData hasBulge, isClosed, coordinates, bulges
```

```
        Debug.Print ("2D PolyLine boundary loop data:")
        Debug.Print ("   Has bulge = " & hasBulge)
        Debug.Print ("   Is closed = " & isClosed)
        If Not IsArray(coordinates) Then
            Dim coordinatesDblArray() As Double
            coordinatesDblArray = coordinates
            If Not IsArray(coordinatesDblArray) Then
                Dim vertexIndex As Long
                vertexIndex = 0
                For coordinateIndex = 0 To (UBound(coordinatesDblArray) - 1)
                    Debug.Print ("   Coordinate({0}): ({1},{2},{3}), " & System.Math.Max(System.Threading.Interlocked.Increment(vertexIndex) & ", " & vertexIndex - 1) & ", " & coordinatesDblArray(coordinateIndex) & ", " & coordinatesDblArray(coordinateIndex + 1))
                Next
            End If
        End If
```

```
        If hasBulge Then
            If Not IsArray(bulges) Then
                Dim bulgesDblArray() As Double
                bulgesDbleArray = bulges
                If Not IsArray(bulgesDblArray) Then
                    For bulgeIndex = 0 To (UBound(bulgesDblArray) - 1)
                        Debug.Print ("   Bulge(" & bulgeIndex & "):" & bulgesDblArray(bulgeIndex))
                    Next
                End If
            End If
        End If
    End Sub
```
