---
title: "Get Nearest Children Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Nearest_Children_Example_CSharp.htm"
---

# Get Nearest Children Example (C#)

This example shows how get the nearest child external references in an unopened drawing.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Replace the first parameter of GetImmediateChildReferences
//    with your local drawing file that contains an external reference.
// 5. Start DraftSight with an empty drawing.
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
             DraftSight.Interop.dsAutomation.ReferenceManager dsRefMgr;
             DraftSight.Interop.dsAutomation.ImageDefinition dsImageDefinition;
             DraftSight.Interop.dsAutomation.PdfDefinition dsPdfDefinition;
             DraftSight.Interop.dsAutomation.DgnDefinition dsDgnDefinition;
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
            dsRefMgr = dsApp.GetReferenceManager();

              // Get all nearest child references of the specified document
              dsRefMgr.GetImmediateChildReferences("C:\\temp\\dwgWithRef.dwg", out extDefTypeArray,   out extDefArray);

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
