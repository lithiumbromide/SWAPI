---
title: "Creating Flat Representations of 3D Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Creating_Flat_Representations_of_3D_Entities_Example_VBA.htm"
---

# Creating Flat Representations of 3D Entities Example (VBA)

This example shows how to flatten 3D entities.

'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
' embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
' install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5. Press F5 to debug the project.
'
' Postconditions:
' 1. Extrudes a 3D entity.
' 2. Creates a block with a flat representation of the 3D entity.
' 3. Creates a new block, Test, containing a circle.
' 4. Replaces the Test block with a flat representation
' of the 3D entity.
' 5. Exports to **c:\temp\newFile.dwg** a flat representation of the
' 3D entity.
'----------------------------------------------------------------

```vb
 Option Explicit
 Sub Main()

         Dim dsApp As DraftSight.Application

         'Connect to DraftSight application
         Set dsApp = GetObject(, "DraftSight.Application")
         dsApp.AbortRunningCommand

         Dim docPath As String
         docPath = "c:\temp"

         Dim dsDoc As Document
         Set dsDoc = dsApp.GetActiveDocument

         If dsDoc Is Nothing Then
             Return
         End If

         Dim dsModel As Model
         Set dsModel = dsDoc.GetModel()

         If dsModel Is Nothing Then
             Return
         End If

         Dim dsSketchManager As DraftSight.SketchManager
         Set dsSketchManager = dsModel.GetSketchManager()

         If dsSketchManager Is Nothing Then
             Return
         End If

         Dim dsPolyline As DraftSight.PolyLine
         Dim coordinates(7) As Double
         coordinates(0) = 128.253
         coordinates(1) = 166.459
         coordinates(2) = 128.253
         coordinates(3) = 43.84
         coordinates(4) = 307.848
         coordinates(5) = 43.84
         coordinates(6) = 307.848
         coordinates(7) = 166.459

         If True Then
             Set dsPolyline = dsSketchManager.InsertPolyline2D(coordinates, True)
         End If

         Dim dsEntities1(0) As PolyLine
         Set dsEntities1(0) = dsPolyline
         Dim extrudes As Object
```

Dim aBlock As DraftSight.BlockInstance

```vb
         dsSketchManager.ExtrudeEntitiesToSolidByHeight dsEntities1, 20, 0, extrudes
         Set aBlock = dsSketchManager.FlatShotByInsertAsBlock( 2#, 22#, 0#, 1#, 1#, 1#, 0#)

         Dim dsCircle As DraftSight.Circle

         If True Then
             Set dsCircle = dsSketchManager.InsertCircle(23#, 5#, 0#, 5#)
         End If

         Dim dsEntities(0) As DraftSight.Circle
         Set dsEntities(0) = dsCircle
         Dim dsEntityTypes_0(0) As Integer
         dsEntityTypes_0(0) = CInt(dsObjectType_e.dsCircleType)
         Dim dsBlockDefinition As DraftSight.BlockDefinition
         Set dsBlockDefinition = dsDoc.CreateBlockDefinition("Test", "", 0#, 0#, 0#, dsEntityTypes_0, dsEntities, dsBlockDefinitionEntities_e.dsBlockDefinitionEntities_RemoveFromDrawing)
         Dim dsBlockInstance As DraftSight.BlockInstance
         Set dsBlockInstance = dsSketchManager.InsertBlock2("Test", -1.075, 14.997, 0#, 1#, 1#, 1#, 0#)
         dsSketchManager.FlatShotByReplaceExistingBlock ("Test")
         dsSketchManager.FlatShotByExportToFile (docPath & "\" & "newFile.dwg")
         dsApp.Zoom dsZoomRange_e.dsZoomRange_Bounds, Nothing, Nothing

 End Sub
```
