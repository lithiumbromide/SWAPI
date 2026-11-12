---
title: "Insert Picture Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Picture_Example_CSharp.htm"
---

# Insert Picture Example (C#)

This example shows how to insert a picture in a drawing document.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Change the path and file name of the raster image to insert.
// 5. Start DraftSight and open a drawing.
// 6. Start debugging the project.
//
// Postconditions: See the DraftSight Command Window for output
// messages and all of your drawing's immediate child references.
//----------------------------------------------------------------
```

```vb
 using DraftSight.Interop.dsAutomation;
 using System;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;

 namespace GetChildReferences_CSharp
 {
       class  Program
      {
            static  void Main(string[] args)
           {
              DraftSight.Interop.dsAutomation.Application dsApp;
              Document dsDoc;
              Model dsModel;
              SketchManager dsSketchManager;
              ReferenceImage dsReference =   null;
               // Dim dsPdfReference As DraftSight.PdfReference;
               // Dim dsDgnReference As DraftSight.DgnReference;
              ImageDefinition dsImageDefinition;
              PdfDefinition dsPdfDefinition;
              DgnDefinition dsDgnDefinition;
               object extDefTypeArray;
               object extDefArray;
              CommandMessage commandline;

              string imageFileName;

               // Connect to DraftSight
              dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

               // Abort any command currently running in DraftSight
               // to avoid nested commands
              dsApp.AbortRunningCommand();

                  commandline = dsApp.GetCommandMessage();

                   // Get active document
                  dsDoc = dsApp.GetActiveDocument();
                   if (dsDoc !=   null)
                  {

                        // Get model space
                      dsModel = dsDoc.GetModel();

                        // Get Sketch Manager
                      dsSketchManager = dsModel.GetSketchManager();

                        // Specify raster image (*.png) to insert into the sketch
                        // Or you can specify a DGN or PDF reference
                      imageFileName =   @"c:\test\list.png";

                        // Insert raster image using ISketchManager::InsertPicture
                      dsReference = dsSketchManager.InsertPicture(imageFileName, 0.0, 0.0, 0.0, 1.0, 0.0);
                        // Or insert a DGN or PDF reference
                        // Set dsDgnReference = dsSketchManager.InsertDgn(imageFileName,...);
                        // Set dsPdfReference = dsSketchManager.InsertPdf(imageFileName,...);

                       if (dsReference ==   null)
                          commandline.PrintLine(imageFileName +  " file not found.");
                        else
                          commandline.PrintLine("A reference was inserted in the drawing.");
                  }
                   else
                      commandline.PrintLine("There are no open documents in DraftSight.");

                  // Get definition of the inserted raster image
                  dsImageDefinition = dsReference.GetDefinition();
                   // Or get the definition of the inserted DGN or PDF reference
                   // Set dsPdfDefinition = dsPdfReference.GetDefinition();
                   // Set dsDgnDefinition = dsDgnReference.GetDefinition();
                  commandline.PrintLine("Image is loaded? " + dsImageDefinition.IsLoaded());

                   // Get all immediate child references of the active document
                  // In addition to the just inserted raster image, your drawing may
                   // contain other immediate child references
                  dsDoc.GetImmediateChildReferences(out extDefTypeArray,   out extDefArray);

                   object[] defArray;
                   int[] defTypeArray;
                  defTypeArray = (int[])extDefTypeArray;
                  defArray = (object[])extDefArray;

                  dsObjectType_e objecttype;
                   object objectdefinition;
                     int i;

                   for (i = 0; i < defArray.Length; i++)
                  {
                      objecttype = (dsObjectType_e)defTypeArray[i];
                      objectdefinition = defArray[i];

                       if ((objecttype == dsObjectType_e.dsImageDefinitionType))
                      {
                          dsImageDefinition = (ImageDefinition)objectdefinition;
                          commandline.PrintLine("Path: " + dsImageDefinition.GetPath());
                          commandline.PrintLine("Found In Path: " + dsImageDefinition.GetFoundInPath());
                      }
                        else  if ((objecttype == dsObjectType_e.dsPdfDefinitionType))
                      {
                          dsPdfDefinition = (PdfDefinition)objectdefinition;
                          commandline.PrintLine("Path: " + dsPdfDefinition.GetPath());
                          commandline.PrintLine("Found In Path: " + dsPdfDefinition.GetFoundInPath());
                      }
                        else  if ((objecttype == dsObjectType_e.dsDgnDefinitionType))
                      {
                          dsDgnDefinition = (DgnDefinition)objectdefinition;
                          commandline.PrintLine("Path: " + dsDgnDefinition.GetPath());
                          commandline.PrintLine("Found In Path: " + dsDgnDefinition.GetFoundInPath());
                      }
                  }
              }

           }
     }
```
