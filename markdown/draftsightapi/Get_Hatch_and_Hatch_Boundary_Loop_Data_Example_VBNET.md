---
title: "Get Hatch and Hatch Boundary Loop Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_VBNET.htm"
---

# Get Hatch and Hatch Boundary Loop Data Example (VB.NET)

This example shows how to get Hatch and Hatch boundary loop data.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Start DraftSight, construct a Circle, Rectangle, Spline, or
 '    Ellipse, and apply a Hatch to the entity.
 ' 6. Open the Immediate window.
 ' 7. Start debugging the project.
 '
 ' Postconditions:
 ' 1. When the prompt appears in the DraftSight command window to
 '    select an entity, select the entity with the Hatch.
 ' 2. The selected entity's Hatch and Hatch boundary loop data is printed
 '    to the Immediate Window.
 '----------------------------------------------------------------

 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms
 Imports System.Diagnostics

 Module Module1

     Dim dsApp As DraftSight.Interop.dsAutomation.Application

     Sub Main()
         'Connect to DraftSight application
         dsApp = GetObject(,  "DraftSight.Application")

         'Get active document
         Dim dsDoc As Document = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MessageBox.Show("There are no open documents in DraftSight.")
             Return
         End If

         dsApp.AbortRunningCommand(); ' abort any command currently running in DraftSight to avoid nested commands

         'Get Selection Manager
         Dim dsSelectionMgr As SelectionManager = dsDoc.GetSelectionManager()

         'Get selection filter
         Dim dsSelectionFilter As SelectionFilter = dsSelectionMgr.GetSelectionFilter()

         'Clear selection filter
         dsSelectionFilter.Clear()

         'Add hatch entity to the selection filter
         dsSelectionFilter.AddEntityType(dsObjectType_e.dsHatchType)

         'Activate selection filter
         dsSelectionFilter.Active = True

         'Get command message object
         Dim dsCommandMessage As CommandMessage = dsApp.GetCommandMessage()

         'Prompt user to select a Hatch entity
         'and get whether selected entity is a Hatch entity
         Dim singleSelection As Boolean = True
         Dim prompt As String = "Please select a Hatch entity."
         Dim errorMessage As String = "Selected entity is not a Hatch entity."
         If dsCommandMessage.PromptForSelection(singleSelection, prompt, errorMessage) Then
             'Get selected entity
             Dim index As Integer = 0
             Dim entityType As dsObjectType_e
             Dim selectedEntity As Object = dsSelectionMgr.GetSelectedObject(dsSelectionSetType_e.dsSelectionSetType_Previous, index, entityType)

             If dsObjectType_e.dsHatchType <> entityType  Then
                 MessageBox.Show(entityType & " was selected, but should be Hatch entity.")
             Else
                 Dim dsHatch As Hatch = TryCast(selectedEntity, Hatch)
                 PrintHatchParameters(dsHatch)
             End If
         End If
     End Sub

     Sub PrintHatchParameters(ByVal dsHatch As Hatch)
         Debug.Print(Environment.NewLine   "Hatch parameters:")

         Debug.Print("Color = " & dsHatch.Color.GetNamedColor())
         Debug.Print("LineScale = " & Convert.ToString(dsHatch.LineScale))
         Debug.Print("LineStyle = " & Convert.ToString(dsHatch.LineStyle))
         Debug.Print("LineWeight = " & Convert.ToString(dsHatch.LineWeight))
         Debug.Print("Layer = " & Convert.ToString(dsHatch.Layer))
         Debug.Print("Visible = " & Convert.ToString(dsHatch.Visible))
         Debug.Print("Erased = " & Convert.ToString(dsHatch.Erased))
         Debug.Print("Handle = " & Convert.ToString(dsHatch.Handle))

         Dim x1 As Double, y1 As  Double, z1  As  Double
         Dim x2 As Double, y2 As  Double, z2  As  Double
         dsHatch.GetBoundingBox(x1, y1, z1, x2, y2, z2)
         Debug.Print(String.Format("BoundingBox: ({0},{1},{2}) and ({3},{4},{5})", x1, y1, z1, x2, y2, _
          z2))

         'Iterate through Hatch boundary loops
         Dim loopsCount As Integer = dsHatch.GetBoundaryLoopsCount()
         Debug.Print("Count of loops = " & loopsCount)
         For index As Integer = 0 To loopsCount - 1
             Debug.Print("Loop(" & index & "):")

             'Get Hatch boundary loop
             Dim dsHatchBoundaryLoop As DraftSight.Interop.dsAutomation.HatchBoundaryLoop = dsHatch.GetHatchBoundaryLoop(index)

             Debug.Print("Type = " + Convert.ToString(dsHatchBoundaryLoop.Type))
             Debug.Print("IsPolyline = " + Convert.ToString(dsHatchBoundaryLoop.IsPolyLine))

             If dsHatchBoundaryLoop.IsPolyLine Then
                 'Get 2D PolyLine boundary loop data
                 GetPolyLineBoundaryLoopData(dsHatchBoundaryLoop)
             Else
                 'Get edges count
                 Dim edgesCount As Integer = dsHatchBoundaryLoop.GetEdgesCount()
                 Debug.Print("Edges count = " & edgesCount)
                 For edgeIndex As Integer = 0 To edgesCount - 1
                     Dim edgeType As dsHatchEdgeType_e = dsHatchBoundaryLoop.GetEdgeType(edgeIndex)
                     Debug.Print("Edge type = " & edgeType)

                     Select Case edgeType
                         Case dsHatchEdgeType_e.dsHatchEdgeType_Line
                             If True  Then
                                 'Get Line edge data
                                 GetLineEdgeData(dsHatchBoundaryLoop, edgeIndex)

                                 Exit Select
                             End If
                         Case dsHatchEdgeType_e.dsHatchEdgeType_CircleArc
                             If True  Then
                                 'Get Circle edge data
                                 GetArcEdgeData(dsHatchBoundaryLoop, edgeIndex)

                                 Exit Select
                             End If
                         Case dsHatchEdgeType_e.dsHatchEdgeType_EllipseArc
                             If True  Then
                                 'Get Ellipse edge data
                                 GetEllipseEdgeData(dsHatchBoundaryLoop, edgeIndex)

                                 Exit Select
                             End If
                         Case dsHatchEdgeType_e.dsHatchEdgeType_Spline
                             If True  Then
                                 'Get Spline edge data
                                 GetSplineEdgeData(dsHatchBoundaryLoop, edgeIndex)

                                 Exit Select
                             End If
                     End Select
                 Next
             End If
         Next
     End Sub

     Sub GetSplineEdgeData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop, ByVal edgeIndex As Integer)
         Dim degree As Integer
         Dim rational As Boolean
         Dim periodic As Boolean
         Dim knotValues As Object
         Dim controlPoints As Object
         dsHatchBoundaryLoop.GetSplineEdgeData(edgeIndex, degree, rational, periodic, knotValues, controlPoints)
         Debug.Print("Spline edge data:")
         Debug.Print("   Degree = " & degree)
         Debug.Print("   Rational = " & rational)
         Debug.Print("   Periodic = " & periodic)

         If knotValues IsNot Nothing Then
             Dim knotValuesDblArray As Double() = DirectCast(knotValues, Double())
             If knotValuesDblArray IsNot Nothing Then
                 For index As Integer = 0 To knotValuesDblArray.Length - 1
                     Debug.Print("   Knot(" & index   "):" & knotValuesDblArray(index))
                 Next
             End If
         End If

         If controlPoints IsNot Nothing Then
             Dim controlPointsDblArray As Double() = DirectCast(controlPoints, Double())
             If controlPointsDblArray IsNot Nothing Then
                 Dim controlPointIndex As Integer = 0
                 For index As Integer = 0 To controlPointsDblArray.Length - 1 Step 2
                     Debug.Print(String.Format("   Control point({0}): ({1},{2})", controlPointIndex, controlPointsDblArray(index), controlPointsDblArray(index + 1)))

                     controlPointIndex += 1
                 Next
             End If
         End If
     End Sub

     Sub GetEllipseEdgeData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop, ByVal edgeIndex As Integer)
         Dim centerX As Double
         Dim centerY As Double
         Dim majorAxisX As Double
         Dim majorAxisY As Double
         Dim minorAxisLengthRatio As Double
         Dim startAngle As Double
         Dim endAngle As Double
         Dim isCounterclockwiseFlag As Boolean
         dsHatchBoundaryLoop.GetEllipseEdgeData(edgeIndex, centerX, centerY, majorAxisX, majorAxisY, minorAxisLengthRatio, _
          startAngle, endAngle, isCounterclockwiseFlag)
         Debug.Print("Ellipse edge data:")
         Debug.Print("   Center X = " & centerX)
         Debug.Print("   Center Y = " & centerY)
         Debug.Print("   Major axis X = " & majorAxisX)
         Debug.Print("   Major axis Y = " & majorAxisY)
         Debug.Print("   Minor axis length ratio = " & minorAxisLengthRatio)
         Debug.Print("   Start angle = " & startAngle)
         Debug.Print("   End angle = " & endAngle)
         Debug.Print("   Is counter-clockwise = " & isCounterclockwiseFlag)
     End Sub

     Sub GetArcEdgeData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop, ByVal edgeIndex As Integer)
         Dim centerX As Double
         Dim centerY As Double
         Dim radius As Double
         Dim startAngle As Double
         Dim endAngle As Double
         Dim isCounterclockwiseFlag As Boolean
         dsHatchBoundaryLoop.GetArcEdgeData(edgeIndex, centerX, centerY, radius, startAngle, endAngle, _
          isCounterclockwiseFlag)
         Debug.Print("Arc edge data:")
         Debug.Print("   Center X = " & centerX)
         Debug.Print("   Center Y = " & centerY)
         Debug.Print("   Radius = " & radius)
         Debug.Print("   Start angle = " & startAngle)
         Debug.Print("   End angle = " & endAngle)
         Debug.Print("   Is counter-clockwise = " & isCounterclockwiseFlag)
     End Sub

     Sub GetLineEdgeData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop, ByVal edgeIndex As Integer)
         Dim startPointX As Double
         Dim startPointY As Double
         Dim endPointX As Double
         Dim endPointY As Double
         dsHatchBoundaryLoop.GetLineEdgeData(edgeIndex, startPointX, startPointY, endPointX, endPointY)
         Debug.Print("Line edge data:")
         Debug.Print("   Start point X = " & startPointX)
         Debug.Print("   Start Point Y = " & startPointY)
         Debug.Print("   End point X = " & endPointX)
         Debug.Print("   End point Y = " & endPointY)
     End Sub

     Sub GetPolyLineBoundaryLoopData(ByVal dsHatchBoundaryLoop As HatchBoundaryLoop)
         Dim hasBulge As Boolean
         Dim isClosed As Boolean
         Dim coordinates As Object
         Dim bulges As Object
         dsHatchBoundaryLoop.GetPolyLineBoundaryLoopData(hasBulge, isClosed, coordinates, bulges)

         Debug.Print("2D PolyLine boundary loop data:")
         Debug.Print("   Has bulge = " & hasBulge)
         Debug.Print("   Is closed = " & isClosed)
         If coordinates IsNot Nothing Then
             Dim coordinatesDblArray As Double() = DirectCast(coordinates, Double())
             If coordinatesDblArray IsNot Nothing Then
                 Dim vertexIndex As Integer = 0
                 For coordinateIndex As Integer = 0 To coordinatesDblArray.Length - 1 Step 2
                     Debug.Print(String.Format("   Coordinate({0}): ({1},{2},{3})", System.Math.Max(System.Threading.Interlocked.Increment(vertexIndex), vertexIndex - 1), coordinatesDblArray(coordinateIndex), coordinatesDblArray(coordinateIndex + 1)))
                 Next
             End If
         End If

         If hasBulge AndAlso bulges IsNot Nothing Then
             Dim bulgesDblArray As Double() = DirectCast(bulges, Double())
             If bulgesDblArray IsNot Nothing Then
                 For bulgeIndex As Integer = 0 To bulgesDblArray.Length - 1
                     Debug.Print("   Bulge(" & bulgeIndex   "):" & bulgesDblArray(bulgeIndex))
                 Next
             End If
         End If
     End Sub

 End Module
```
