---
title: "Insert Picture Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Picture_Example_VBNET.htm"
---

# Insert Picture Example (VB.NET)

This example shows how to insert a picture in a drawing document.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Change the path and file name of the picture file to insert.
' 5. Start DraftSight and open a drawing.
' 6. Start debugging the project.
'
' Postconditions: See the DraftSight Command Window for output
' messages and all of your drawing's immediate child references.
'----------------------------------------------------------------
```

```vb
 Imports DraftSight.Interop.dsAutomation
 Module   Module1

       Sub Main()
            Dim dsApp  As Application
            Dim dsDoc  As Document
            Dim dsModel  As Model
            Dim dsSketchManager  As SketchManager
            Dim dsReference  As ReferenceImage =   Nothing
            'Dim dsPdfReference As DraftSight.PdfReference
            'Dim dsDgnReference As DraftSight.DgnReference
            Dim dsImageDefinition  As ImageDefinition
            Dim dsPdfDefinition  As PdfDefinition
            Dim dsDgnDefinition  As DgnDefinition
            Dim extDefTypeArray(0)  As   Integer
            Dim extDefArray(0)  As   Object
            Dim commandline  As CommandMessage

            Dim imageFileName  As   String

            'Connect to DraftSight
           dsApp = GetObject(,   "DraftSight.Application")

            'Abort any command currently running in DraftSight
            'to avoid nested commands
           dsApp.AbortRunningCommand

           commandline = dsApp.GetCommandMessage()

            'Get active document
           dsDoc = dsApp.GetActiveDocument()
            If  Not dsDoc  Is  Nothing   Then

               'Get model space
              dsModel = dsDoc.GetModel()

               'Get Sketch Manager
              dsSketchManager = dsModel.GetSketchManager()

               'Specify raster image (*.png) to insert into the sketch
               'Or you can specify a DGN or PDF reference
              imageFileName =   "c:\test\list.png"

               'Insert raster image using ISketchManager::InsertPicture
              dsReference = dsSketchManager.InsertPicture(imageFileName, 0#, 0#, 0#, 1.0#, 0#)
               'Or insert a DGN or PDF reference
               'Set dsDgnReference = dsSketchManager.InsertDgn(imageFileName,...)
               'Set dsPdfReference = dsSketchManager.InsertPdf(imageFileName,...)

               If dsReference  Is   Nothing   Then
                  commandline.PrintLine(imageFileName   " file not found.")
               Else
                  commandline.PrintLine("A reference was inserted in the drawing.")
               End  If
            Else
              commandline.PrintLine("There are no open documents in DraftSight.")
            End  If

            'Get definition of the inserted raster image
           dsImageDefinition = dsReference.GetDefinition()
            'Or get the definition of the inserted DGN or PDF reference
            'Set dsPdfDefinition = dsPdfReference.GetDefinition()
            'Set dsDgnDefinition = dsDgnReference.GetDefinition()
           commandline.PrintLine("Image is loaded? " & dsImageDefinition.IsLoaded)

          'Get all immediate child references of the active document
            'In addition to the just inserted raster image, your drawing may
            'contain other immediate child references
           dsDoc.GetImmediateChildReferences(extDefTypeArray, extDefArray)

            Dim objecttype  As dsObjectType_e
            Dim objectdefinition  As   Object
            Dim i  As   Integer

            For i = 0  To UBound(extDefTypeArray)

              objecttype = extDefTypeArray(i)
              objectdefinition = extDefArray(i)

               If (objecttype = dsObjectType_e.dsImageDefinitionType)  Then
                  dsImageDefinition = objectdefinition
                  commandline.PrintLine("Path: " & dsImageDefinition.GetPath())
                  commandline.PrintLine("Found In Path: " & dsImageDefinition.GetFoundInPath())
               ElseIf (objecttype = dsObjectType_e.dsPdfDefinitionType)  Then
                  dsPdfDefinition = objectdefinition
                  commandline.PrintLine("Path: " & dsPdfDefinition.GetPath())
                  commandline.PrintLine("Found In Path: " & dsPdfDefinition.GetFoundInPath())
               ElseIf (objecttype = dsObjectType_e.dsDgnDefinitionType)  Then
                  dsDgnDefinition = objectdefinition
                  commandline.PrintLine("Path: " & dsDgnDefinition.GetPath())
                  commandline.PrintLine("Found In Path: " & dsDgnDefinition.GetFoundInPath())
               End  If
            Next
       End  Sub

 End  Module
```
