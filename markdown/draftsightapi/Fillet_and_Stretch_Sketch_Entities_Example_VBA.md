---
title: "Fillet and Stretch Sketch Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Fillet_and_Stretch_Sketch_Entities_Example_VBA.htm"
---

# Fillet and Stretch Sketch Entities Example (VBA)

This example shows how to fillet and stretch sketch entities.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VBA macro in a software product in which VBA is
 '    embedded.
 ' 2. Copy and paste this example into the Visual Basic IDE.
 ' 3. Add a reference to the DraftSight type library,
 '    install_dir\bin\dsAutomation.dll.
 ' 4. Start DraftSight and open a new drawing.
 ' 5. Run the macro.
 '
 ' Postconditions:
 ' 1. Three pairs of sketch entities are created and filleted.
 ' 2. Three sketch entities are created and stretched.
 '----------------------------------------------------------------
 Option Explicit
 Dim dsApp As DraftSight.Application
 Dim dsDoc As DraftSight.Document
 Sub Main()

        'Connect to DraftSight
         Set dsApp = GetObject(, "DraftSight.Application")
         'Abort any command currently running in DraftSight
         'to avoid nested commands
         dsApp.AbortRunningCommand
        'Get active document
         Set dsDoc = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MsgBox ("There are no opened documents in DraftSight.")
             Return
         End If
        'Get model space
         Dim dsModel As Model
         Set dsModel = dsDoc.GetModel()
        'Get sketch manager
         Dim dsSketchMgr As DraftSight.SketchManager
         Set dsSketchMgr = dsModel.GetSketchManager()
        'Fillet entities
         Call FilletEntities(dsSketchMgr)
        'Stretch entities
         Call StretchEntities(dsSketchMgr)
 End Sub
Sub StretchEntities(dsSketchMgr As DraftSight.SketchManager)
         'Stretch parameters
         Dim displacementX As Double
         displacementX = 4
         Dim displacementY As Double
         displacementY = 6
         Dim displacementZ As Double
         displacementZ = 0
         Dim dsEntities(0 To 2) As Object
         Dim crossingBoxStartCorner(0 To 2) As Double
         Dim crossingBoxEndCorner(0 To 2) As Double
        'Prepare entities for stretch
         DrawEntitiesForStretch dsSketchMgr, dsEntities, crossingBoxStartCorner, crossingBoxEndCorner
        'Zoom extents
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
        MsgBox ("Entities before STRETCH.")
        'Stretch entities
         dsSketchMgr.StretchEntities displacementX, displacementY, displacementZ, dsEntities, crossingBoxStartCorner, crossingBoxEndCorner
        'Zoom extents
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
        MsgBox ("Entities after STRETCH.")
 End Sub
Sub DrawEntitiesForStretch(dsSketchMgr As DraftSight.SketchManager, dsEntities() As Object, crossingBoxStartCorner() As Double, crossingBoxEndCorner() As Double)
         'Initialize output entities array
         Dim entitiesIndex As Long
         entitiesIndex = 0
         Dim entitiesCount As Long
         entitiesCount = 3
        'Draw PolyLine
         Dim closed As Boolean
         closed = True
         Dim coordinates(0 To 7) As Double
         coordinates(0) = 1
         coordinates(1) = 1
         coordinates(2) = 3
         coordinates(3) = 1
         coordinates(4) = 3
         coordinates(5) = 3
         coordinates(6) = 1
         coordinates(7) = 3

        Dim dsPolyline As Object
         Set dsPolyline = dsSketchMgr.InsertPolyline2D(coordinates, closed)
        'Add PolyLine to output array of entities
         Set dsEntities(entitiesIndex) = dsPolyline
         entitiesIndex = entitiesIndex + 1
        'Draw Line
         Dim startPoint(0 To 2) As Double
         startPoint(0) = 4
         startPoint(1) = 1
         startPoint(2) = 0
         Dim endPoint(0 To 2) As Double
         endPoint(0) = 4
         endPoint(1) = 5
         endPoint(2) = 0
         Dim dsLine As Object
         Set dsLine = dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))
        'Add Line to output array of entities
         Set dsEntities(entitiesIndex) = dsLine
         entitiesIndex = entitiesIndex + 1
        'Draw Circle
         Dim radius As Double
         radius = 1
         Dim centerPoint(0 To 2) As Double
         centerPoint(0) = 6
         centerPoint(1) = 2
         centerPoint(2) = 0
         Dim dsCircle As Object
         Set dsCircle = dsSketchMgr.InsertCircle(centerPoint(0), centerPoint(1), centerPoint(2), radius)
        'Add Circle to output array of entities
         Set dsEntities(entitiesIndex) = dsCircle
         entitiesIndex = entitiesIndex + 1
        'Specify crossing coordinates
         crossingBoxStartCorner(0) = 0.6
         crossingBoxStartCorner(1) = 2
         crossingBoxStartCorner(2) = 0
         crossingBoxEndCorner(0) = 8
         crossingBoxEndCorner(1) = 6
         crossingBoxEndCorner(2) = 0
 End Sub
Sub FilletEntities(dsSketchMgr As DraftSight.SketchManager)
         Dim firstPointOnEntityDblArray(0 To 8) As Double
         Dim firstEntityArray(0 To 2) As Object
         Dim secondPointOnEntityDblArray(0 To 8) As Double
         Dim secondEntityArray(0 To 2) As Object
        'Prepare entities for fillet
         DrawEntitiesForFillet dsSketchMgr, firstPointOnEntityDblArray, firstEntityArray, secondPointOnEntityDblArray, secondEntityArray
        'Zoom extents
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
        MsgBox ("Entities before FILLET.")
        'Set fillet radius
         Dim filletRadius As Double
         filletRadius = 1.5
         SetFilletRadius dsDoc, filletRadius
        'Do fillet entities
         dsSketchMgr.FilletEntities firstPointOnEntityDblArray, firstEntityArray, secondPointOnEntityDblArray, secondEntityArray
        'Zoom extents
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
        MsgBox ("Entities after FILLET.")
 End Sub
Sub DrawEntitiesForFillet(dsSketchMgr As DraftSight.SketchManager, firstPointOnEntityDblArray() As Double, firstEntityArray() As Object, secondPointOnEntityDblArray() As Double, secondEntityArray() As Object)
         'Count of entity pairs to fillet
         Dim count As Integer
         count = 3
        Dim entityIndex As Long
         entityIndex = 0
         Dim coordinateIndex As Long
         coordinateIndex = 0
        '--------Draw the first pair of entities to fillet-----------------------
        'Draw a Line
         Dim startPoint(0 To 2) As Double
         startPoint(0) = 0
         startPoint(1) = 0
         startPoint(2) = 0
         Dim endPoint(0 To 2) As Double
         endPoint(0) = 5
         endPoint(1) = 0
         endPoint(2) = 0
         Dim dsLine As Object
         Set dsLine = dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))
        'Add Line to output arrays
         Set firstEntityArray(entityIndex) = dsLine
         firstPointOnEntityDblArray(coordinateIndex) = endPoint(0)
         firstPointOnEntityDblArray(coordinateIndex + 1) = endPoint(1)
         firstPointOnEntityDblArray(coordinateIndex + 2) = endPoint(2)
        'Draw Arc
         Dim radius As Double
         radius = 1
         Dim centerPoint(0 To 2) As Double
         centerPoint(0) = 2
         centerPoint(1) = -1
         centerPoint(2) = 0
         Dim startAngle As Double
         startAngle = 3.141576
         Dim endAngle As Double
         endAngle = 1.5 * 3.141576
         Dim dsArc As Object
         Set dsArc = dsSketchMgr.InsertArc(centerPoint(0), centerPoint(1), centerPoint(2), radius, startAngle, endAngle)
        'Add Arc to output arrays
         Set secondEntityArray(entityIndex) = dsArc
         secondPointOnEntityDblArray(coordinateIndex) = centerPoint(0) - radius
         secondPointOnEntityDblArray(coordinateIndex + 1) = centerPoint(1)
         secondPointOnEntityDblArray(coordinateIndex + 2) = centerPoint(2)
        'Increase entity index
         entityIndex = entityIndex + 1
         'Increase coordinate index
         coordinateIndex = coordinateIndex + 3
        '--------Draw the second pair of entities to fillet----------------------
        'Draw a Line
         startPoint(0) = 11
         startPoint(1) = 0
         startPoint(2) = 0
         endPoint(0) = 16
         endPoint(1) = 0
         endPoint(2) = 0
         Set dsLine = dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))
        'Add Line to output arrays
         Set firstEntityArray(entityIndex) = dsLine
         firstPointOnEntityDblArray(coordinateIndex) = endPoint(0)
         firstPointOnEntityDblArray(coordinateIndex + 1) = endPoint(1)
         firstPointOnEntityDblArray(coordinateIndex + 2) = endPoint(2)
        'Draw a Circle
         centerPoint(0) = 18
         centerPoint(1) = -1
         centerPoint(2) = 0
         radius = 1
         Dim dsCircle As Object
         Set dsCircle = dsSketchMgr.InsertCircle(centerPoint(0), centerPoint(1), centerPoint(2), radius)
        'Add Circle to output arrays
         Set secondEntityArray(entityIndex) = dsCircle
         secondPointOnEntityDblArray(coordinateIndex) = centerPoint(0) - radius
         secondPointOnEntityDblArray(coordinateIndex + 1) = centerPoint(1)
         secondPointOnEntityDblArray(coordinateIndex + 2) = centerPoint(2)
        'Increase entity index
         entityIndex = entityIndex + 1
         'Increase coordinate index
         coordinateIndex = coordinateIndex + 3
        '--------Draw the third pair of entities to fillet-----------------------
        'Draw first Circle
         centerPoint(0) = 7
         centerPoint(1) = -1
         centerPoint(2) = 0
         radius = 1
         Dim dsFirstCircle As Object
         Set dsFirstCircle = dsSketchMgr.InsertCircle(centerPoint(0), centerPoint(1), centerPoint(2), radius)
        'Add Circle to output arrays
         Set firstEntityArray(entityIndex) = dsFirstCircle
         firstPointOnEntityDblArray(coordinateIndex) = centerPoint(0)
         firstPointOnEntityDblArray(coordinateIndex + 1) = centerPoint(1) + radius
         firstPointOnEntityDblArray(coordinateIndex + 2) = centerPoint(2)
        'Draw second Circle
         centerPoint(0) = 9
         Dim dsSecondCircle As Object
         Set dsSecondCircle = dsSketchMgr.InsertCircle(centerPoint(0), centerPoint(1), centerPoint(2), radius)
        'Add Circle to output arrays
         Set secondEntityArray(entityIndex) = dsSecondCircle
         secondPointOnEntityDblArray(coordinateIndex) = centerPoint(0)
         secondPointOnEntityDblArray(coordinateIndex + 1) = centerPoint(1) + radius
         secondPointOnEntityDblArray(coordinateIndex + 2) = centerPoint(2)
 End Sub
Sub SetFilletRadius(dsDoc As DraftSight.Document, filletRadius As Double)
         Dim setResult As dsSetCommandOptionResult_e
         Dim filletRadCommandOption As dsCommandOptionDouble_e
         filletRadCommandOption = dsCommandOptionDouble_SetFltRad
        dsDoc.SetCommandOptionDouble filletRadCommandOption, filletRadius, setResult
         If dsSetCommandOptionResult_e.dsSetCommandOptionResult_Success <> setResult Then
             MsgBox ("Document.SetCommandOptionDouble() returns " & setResult & " after setting of " & filletRadCommandOption & " command option.")
         End If
 End Sub
```
