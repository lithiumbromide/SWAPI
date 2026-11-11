---
title: "Fillet and Stretch Sketch Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Fillet_and_Stretch_Sketch_Entities_Example_VBNET.htm"
---

# Fillet and Stretch Sketch Entities Example (VB.NET)

This example shows how to fillet and stretch sketch entities.

```vb
 '--------------------------------------------------------------
 'Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Start DraftSight and open a new drawing.
 ' 6. Run the macro.
 '
 'Postconditions:
 '1. Three pairs of sketch entities are created and filleted.
 '2. Three sketch entities are created and stretched.
 '----------------------------------------------------------------
 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms

 Module Module1
     Dim dsApp As DraftSight.Interop.dsAutomation.Application
     Dim dsDoc As Document

     Sub Main(ByVal args As String())
         'Connect to DraftSight application
         dsApp = ConnectToDraftSight()
         If dsApp Is Nothing Then
             Return
         End If

         dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

         'Get active document
         dsDoc = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MessageBox.Show("There are no opened documents in DraftSight.")
             Return
         End If

         'Get model space
         Dim dsModel As Model = dsDoc.GetModel()

         'Get sketch manager
         Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

         'Fillet entities
         FilletEntities(dsSketchMgr)

         'Stretch entities
         StretchEntities(dsSketchMgr)
     End Sub

     Sub StretchEntities(ByVal dsSketchMgr As SketchManager)
         'Stretch parameters
         Dim displacementX As Double = 4
         Dim displacementY As Double = 6
         Dim displacementZ As Double = 0
         Dim dsEntities As DispatchWrapper() = Nothing
         Dim crossingBoxStartCorner As Double() = Nothing
         Dim crossingBoxEndCorner As Double() = Nothing

         'Prepare entities for stretch
         DrawEntitiesForStretch(dsSketchMgr, dsEntities, crossingBoxStartCorner, crossingBoxEndCorner)

         'Zoom extents
         dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

         MessageBox.Show("Entities before STRETCH.")

         'Stretch entities
         dsSketchMgr.StretchEntities(displacementX, displacementY, displacementZ, dsEntities, crossingBoxStartCorner, crossingBoxEndCorner)

         'Zoom extents
         dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

         MessageBox.Show("Entities after STRETCH.")
     End Sub

     Sub DrawEntitiesForStretch(ByVal dsSketchMgr As SketchManager, ByRef dsEntities As DispatchWrapper(), ByRef crossingBoxStartCorner As Double(), ByRef crossingBoxEndCorner As Double())
         'Initialize output entities array
         Dim entitiesIndex As Integer = 0
         Dim entitiesCount As Integer = 3
         dsEntities = New DispatchWrapper(entitiesCount) {}

         'Draw polyline
         Dim closed As Boolean = True
         Dim coordinates As Double() = {1, 1, 3, 1, 3, 3, _
          1, 3}
         Dim dsPolyline As PolyLine = dsSketchMgr.InsertPolyline2D(coordinates, closed)

         'Add polyline to output array of entities
         dsEntities(System.Math.Max(System.Threading.Interlocked.Increment(entitiesIndex), entitiesIndex - 1)) = New DispatchWrapper(dsPolyline)

         'Draw line
         Dim startPoint As Double() = {4, 1, 0}
         Dim endPoint As Double() = {4, 5, 0}
         Dim dsLine As Line = dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))

         'Add line to output array of entities
         dsEntities(System.Math.Max(System.Threading.Interlocked.Increment(entitiesIndex), entitiesIndex - 1)) = New DispatchWrapper(dsLine)

         'Draw circle
         Dim radius As Double = 1
         Dim centerPoint As Double() = {6, 2, 0}
         Dim dsCircle As Circle = dsSketchMgr.InsertCircle(centerPoint(0), centerPoint(1), centerPoint(2), radius)

         'Add circle to output array of entities
         dsEntities(System.Math.Max(System.Threading.Interlocked.Increment(entitiesIndex), entitiesIndex - 1)) = New DispatchWrapper(dsCircle)

         'Specify crossing coordinates
         crossingBoxStartCorner =  New  Double() {0.6, 2, 0}
         crossingBoxEndCorner = New Double() {8, 6, 0}
     End Sub

     Sub FilletEntities(ByVal dsSketchMgr As SketchManager)
         Dim firstPointOnEntityDblArray As Double() = Nothing
         Dim firstEntityArray As DispatchWrapper() = Nothing
         Dim secondPointOnEntityDblArray As Double() = Nothing
         Dim secondEntityArray As DispatchWrapper() = Nothing

         'Prepare entities for fillet
         DrawEntitiesForFillet(dsSketchMgr, firstPointOnEntityDblArray, firstEntityArray, secondPointOnEntityDblArray, secondEntityArray)

         'Zoom extents
         dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

         MessageBox.Show("Entities before FILLET.")

         'Set fillet radius
         Dim filletRadius As Double = 1.5
         SetFilletRadius(dsDoc, filletRadius)

         'Do fillet entities
         dsSketchMgr.FilletEntities(firstPointOnEntityDblArray, firstEntityArray, secondPointOnEntityDblArray, secondEntityArray)

         'Zoom extents
         dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)

         MessageBox.Show("Entities after FILLET.")
     End Sub

     Sub DrawEntitiesForFillet(ByVal dsSketchMgr As SketchManager, ByRef firstPointOnEntityDblArray As Double(), ByRef firstEntityArray As DispatchWrapper(), ByRef secondPointOnEntityDblArray As Double(), ByRef secondEntityArray As DispatchWrapper())
         'Count of entity pairs to fillet
         Dim count As Integer = 3

         'Initialize output arrays
         firstPointOnEntityDblArray =  New  Double(count * 3 - 1) {}
         firstEntityArray = New DispatchWrapper(count - 1) {}
         secondPointOnEntityDblArray = New Double(count * 3 - 1) {}
         secondEntityArray = New DispatchWrapper(count - 1) {}
         Dim entityIndex As Integer = 0
         Dim coordinateIndex As Integer = 0

         '--------Draw the first pair of entities to fillet-----------------------

         'Draw a line
         Dim startPoint As Double() = {0, 0, 0}
         Dim endPoint As Double() = {5, 0, 0}
         Dim dsLine As Line = dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))

         'Add line entity to output arrays
         firstEntityArray(entityIndex) = New DispatchWrapper(dsLine)
         firstPointOnEntityDblArray(coordinateIndex) = endPoint(0)
         firstPointOnEntityDblArray(coordinateIndex + 1) = endPoint(1)
         firstPointOnEntityDblArray(coordinateIndex + 2) = endPoint(2)

         'Draw an arc
         Dim radius As Double = 1
         Dim centerPoint As Double() = {2, -1, 0}
         Dim startAngle As Double = Math.PI
         Dim endAngle As Double = 1.5 * Math.PI
         Dim dsArc As CircleArc = dsSketchMgr.InsertArc(centerPoint(0), centerPoint(1), centerPoint(2), radius, startAngle, endAngle)

         'Add arc entity to output arrays
         secondEntityArray(entityIndex) = New DispatchWrapper(dsArc)
         secondPointOnEntityDblArray(coordinateIndex) = centerPoint(0) - radius
         secondPointOnEntityDblArray(coordinateIndex + 1) = centerPoint(1)
         secondPointOnEntityDblArray(coordinateIndex + 2) = centerPoint(2)

         'Increase entity index
         entityIndex += 1
         'Increase coordinate index
         coordinateIndex += 3

         '--------Draw the second pair of entities to fillet----------------------

         'Draw a line
         startPoint =  New  Double() {11, 0, 0}
         endPoint = New Double() {16, 0, 0}
         dsLine = dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))

         'Add line entity to output arrays
         firstEntityArray(entityIndex) = New DispatchWrapper(dsLine)
         firstPointOnEntityDblArray(coordinateIndex) = endPoint(0)
         firstPointOnEntityDblArray(coordinateIndex + 1) = endPoint(1)
         firstPointOnEntityDblArray(coordinateIndex + 2) = endPoint(2)

         'Draw a circle
         centerPoint =  New  Double() {18, -1, 0}
         radius = 1
         Dim dsCircle As Circle = dsSketchMgr.InsertCircle(centerPoint(0), centerPoint(1), centerPoint(2), radius)

         'Add circle entity to output arrays
         secondEntityArray(entityIndex) = New DispatchWrapper(dsCircle)
         secondPointOnEntityDblArray(coordinateIndex) = centerPoint(0) - radius
         secondPointOnEntityDblArray(coordinateIndex + 1) = centerPoint(1)
         secondPointOnEntityDblArray(coordinateIndex + 2) = centerPoint(2)

         'Increase entity index
         entityIndex += 1
         'Increase coordinate index
         coordinateIndex += 3

         '--------Draw the third pair of entities to fillet-----------------------

         'Draw first circle
         centerPoint =  New  Double() {7, -1, 0}
         radius = 1
         Dim dsFirstCircle As Circle = dsSketchMgr.InsertCircle(centerPoint(0), centerPoint(1), centerPoint(2), radius)

         'Add circle entity to output arrays
         firstEntityArray(entityIndex) = New DispatchWrapper(dsFirstCircle)
         firstPointOnEntityDblArray(coordinateIndex) = centerPoint(0)
         firstPointOnEntityDblArray(coordinateIndex + 1) = centerPoint(1) + radius
         firstPointOnEntityDblArray(coordinateIndex + 2) = centerPoint(2)

         'Draw second circle
         centerPoint(0) = 9
         Dim dsSecondCircle As Circle = dsSketchMgr.InsertCircle(centerPoint(0), centerPoint(1), centerPoint(2), radius)

         'Add circle entity to output arrays
         secondEntityArray(entityIndex) = New DispatchWrapper(dsSecondCircle)
         secondPointOnEntityDblArray(coordinateIndex) = centerPoint(0)
         secondPointOnEntityDblArray(coordinateIndex + 1) = centerPoint(1) + radius
         secondPointOnEntityDblArray(coordinateIndex + 2) = centerPoint(2)
     End Sub

     Sub SetFilletRadius(ByVal dsDoc As Document, ByVal filletRadius As Double)
         Dim setResult As dsSetCommandOptionResult_e
         Dim filletRadCommandOption As dsCommandOptionDouble_e = dsCommandOptionDouble_e.dsCommandOptionDouble_SetFltRad

         dsDoc.SetCommandOptionDouble(filletRadCommandOption, filletRadius, setResult)
         If dsSetCommandOptionResult_e.dsSetCommandOptionResult_Success <> setResult Then
             MessageBox.Show("Document.SetCommandOptionDouble() returns " & setResult.ToString()   " after setting of " & filletRadCommandOption & " command option.")
         End If
     End Sub

     Function ConnectToDraftSight() As DraftSight.Interop.dsAutomation.Application
         Dim dsApp As DraftSight.Interop.dsAutomation.Application =  Nothing

         Try
             'Connect to DraftSight
             dsApp =  DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)
         Catch ex As Exception
             MessageBox.Show("Failed to connect to DraftSight. Cause: " & ex.Message)
             dsApp = Nothing
         End Try

         Return dsApp
     End Function
 End Module
```
