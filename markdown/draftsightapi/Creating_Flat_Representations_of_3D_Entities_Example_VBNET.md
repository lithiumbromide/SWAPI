---
title: "Creating Flat Representations of 3D Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Creating_Flat_Representations_of_3D_Entities_Example_VBNET.htm"
---

# Creating Flat Representations of 3D Entities Example (VB.NET)

This example shows how to flatten 3D entities.

'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the IDE.
' 3. Add a reference to:
' `install_dir`\**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
' 4. Add a reference to **System**.
' 5. Start DraftSight.
' 6. Press F5 to debug the project.
'
' Postconditions:
' 1. Extrudes a 3D entity.
' 2. Creates a block with a flat representation of the 3D entity.
' 3. Creates a new block, Test, containing a circle.
' 4. Replaces the Test block with a flat representation
' of the 3D entity.
' 5. Exports to `mainpath`**\newFile.dwg** a flat representation of the
' 3D entity.
'----------------------------------------------------------------

```vb
 Imports System
 Imports System.IO
 Imports System.Text.RegularExpressions
 Imports System.Reflection
 Imports System.Collections.Generic
 Imports System.Linq
 Imports System.Text
 Imports System.Threading.Tasks
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices

 Module   Module1

       Sub Main()

            Dim Application  As DraftSight.Interop.dsAutomation.Application

         'Connect to DraftSight application
         Application =   DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

            If Application  Is   Nothing   Then
               Return
            End  If

           Application.AbortRunningCommand()
            Dim appPath  As  String = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location)
            Dim extract  As  String() = Regex.Split(appPath,  "bin")
            Dim mainPath  As  String = extract(0).TrimEnd("\"c)
            Dim dsDoc  As Document = application.GetActiveDocument()

            If dsDoc  Is  Nothing   Then
               Return
            End  If

            Dim dsModel  As Model = dsDoc.GetModel()

            If dsModel  Is  Nothing   Then
               Return
            End  If

            Dim dsSketchManager  As SketchManager = dsModel.GetSketchManager()

            If dsSketchManager  Is   Nothing   Then
               Return
            End  If

            Dim dsPolyline  As PolyLine

            If  True  Then
              dsPolyline = dsSketchManager.InsertPolyline2D(New  Double() {128.253, 166.459, 128.253, 43.84, 307.848, 43.84, 307.848, 166.459},  True)
            End  If

            Dim dsEntities1  As DispatchWrapper() =  New DispatchWrapper(0) {}
           dsEntities1(0) =   New DispatchWrapper(dsPolyline)
            Dim extrudes  As  Object =   Nothing
           dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities1, 20, 0, extrudes)
           dsSketchManager.FlatShotByInsertAsBlock(2.0, 22.0, 0.0, 1.0, 1.0, 1.0, 0.0)
            Dim dsCircle  As Circle

            If  True  Then
              dsCircle = dsSketchManager.InsertCircle(23.0, 5.0, 0.0, 5.0)
            End  If

            Dim dsEntities  As DispatchWrapper() =  New DispatchWrapper(0) {}
           dsEntities(0) =   New DispatchWrapper(dsCircle)
            Dim dsEntityTypes_0  As   Integer() =   New   Integer() {CInt(dsObjectType_e.dsCircleType)}
            Dim dsBlockDefinition  As BlockDefinition = dsDoc.CreateBlockDefinition("Test",  "", 0.0, 0.0, 0.0, dsEntityTypes_0, dsEntities, dsBlockDefinitionEntities_e.dsBlockDefinitionEntities_RemoveFromDrawing)
            Dim dsBlockInstance  As BlockInstance = dsSketchManager.InsertBlock2("Test", -1.075, 14.997, 0.0, 1.0, 1.0, 1.0, 0.0)
           dsSketchManager.FlatShotByReplaceExistingBlock("Test")
           dsSketchManager.FlatShotByExportToFile(mainPath    "\"    "newFile.dwg")
           application.Zoom(dsZoomRange_e.dsZoomRange_Bounds,   Nothing,   Nothing)
       End  Sub

 End  Module
```
