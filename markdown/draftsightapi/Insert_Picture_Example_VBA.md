---
title: "Insert Picture Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Picture_Example_VBA.htm"
---

# Insert Picture Example (VBA)

This example shows how to insert a picture in a drawing document.

```vb
  '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VBA macro in a software product in which VBA is
 '    embedded.
 ' 2. Copy and paste this example into the Visual Basic IDE.
 ' 3. Add a reference to the DraftSight type library,
 '    install_dir\bin\dsAutomation.dll.
 ' 4. Change the path and file name of a raster image to insert.
 ' 5. Start DraftSight and open a drawing.
 ' 6. Run the macro.
 '
 ' Postconditions: See the DraftSight Command Window for output
 ' messages and all of your drawing's immediate child references.
  '--------------------------------------------------------------
 Option Explicit

 Sub main()

     Dim dsApp As DraftSight.Application
     Dim dsDoc As DraftSight.Document
     Dim dsModel As DraftSight.Model
     Dim dsSketchManager As DraftSight.SketchManager
     Dim dsReference As DraftSight.ReferenceImage
     'Dim dsPdfReference As DraftSight.PdfReference
     'Dim dsDgnReference As DraftSight.DgnReference
     Dim dsImageDefinition As DraftSight.ImageDefinition
     Dim dsPdfDefinition As DraftSight.PdfDefinition
     Dim dsDgnDefinition As DraftSight.DgnDefinition
     Dim extDefTypeArray As Variant
     Dim extDefArray As Variant
     Dim commandline As DraftSight.CommandMessage

     Dim imageFileName As String

     'Connect to DraftSight
     Set dsApp = GetObject(, "DraftSight.Application")

     'Abort any command currently running in DraftSight
     'to avoid nested commands
     dsApp.AbortRunningCommand

     Set commandline = dsApp.GetCommandMessage()

     'Get active document
     Set dsDoc = dsApp.GetActiveDocument()
     If Not dsDoc Is Nothing Then

         'Get model space
         Set dsModel = dsDoc.GetModel()

         'Get Sketch Manager
         Set dsSketchManager = dsModel.GetSketchManager()

         'Specify raster image (*.png) to insert into the sketch
         'Or you can specify a DGN or PDF reference
         imageFileName = "c:\test\list.png"

         'Insert raster image
         Set dsReference = dsSketchManager.InsertPicture(imageFileName, 0#, 0#, 0#, 1#, 0#)
         'Or insert a DGN or PDF reference
         'Set dsDgnReference = dsSketchManager.InsertDgn(imageFileName,...)
         'Set dsPdfReference = dsSketchManager.InsertPdf(imageFileName,...)

         If dsReference Is Nothing Then
             commandline.PrintLine imageFileName & " file not found."
         Else
             commandline.PrintLine "A reference was inserted in the drawing."
         End If
     Else
         commandline.PrintLine "There are no open documents in DraftSight."
     End If

     'Get definition of the inserted raster image
     Set dsImageDefinition = dsReference.GetDefinition()
     'Or get the definition of the inserted DGN or PDF reference
     'Set dsPdfDefinition = dsPdfReference.GetDefinition()
     'Set dsDgnDefinition = dsDgnReference.GetDefinition()
     commandline.PrintLine "Image is loaded? " & dsImageDefinition.IsLoaded

     'Get all immediate child references of the active document
     'In addition to the just inserted raster image, your drawing may
     'contain other immediate child references
     dsDoc.GetImmediateChildReferences extDefTypeArray, extDefArray

     Dim objecttype As dsObjectType_e
     Dim objectdefinition As Object
     Dim i As Long

     For i = 0 To UBound(extDefTypeArray)

         objecttype = extDefTypeArray(i)
         Set objectdefinition = extDefArray(i)

         If (objecttype = dsObjectType_e.dsImageDefinitionType) Then
             Set dsImageDefinition = objectdefinition
             commandline.PrintLine "Path: " & dsImageDefinition.GetPath()
             commandline.PrintLine "Found In Path: " & dsImageDefinition.GetFoundInPath()
         ElseIf (objecttype = dsObjectType_e.dsPdfDefinitionType) Then
             Set dsPdfDefinition = objectdefinition
             commandline.PrintLine "Path: " & dsPdfDefinition.GetPath()
             commandline.PrintLine "Found In Path: " & dsPdfDefinition.GetFoundInPath()
         ElseIf (objecttype = dsObjectType_e.dsDgnDefinitionType) Then
             Set dsDgnDefinition = objectdefinition
             commandline.PrintLine "Path: " & dsDgnDefinition.GetPath()
             commandline.PrintLine "Found In Path: " & dsDgnDefinition.GetFoundInPath()
         End If
     Next

 End Sub
```
