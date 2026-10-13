---
title: "Save Solid Body to File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Solid_Body_to_File_Example_CSharp.htm"
---

# Save Solid Body to File Example (C#)

This example shows how to save a weldment member to another part document.

```vb
//----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 //
 // Postconditions:
 // 1. Updates the cut list in the weldment part.
 // 2. Saves the first weldment member in the FeatureManager design tree to
 //    RefWeldment1.sldprt, and saves the cut list properties in the parent part
 //    to the cut list of the new part.
 // 3. Opens RefWeldment1.sldprt and updates its cut list. (This step could
 //    take a few minutes to complete.)
 // 4. At  System.Diagnostics.Debugger.Break(), press F5.
 // 5. Closes RefWeldment1.sldprt.
 // 6. To verify steps 2 and 3, open and inspect RefWeldment1.sldprt, which resides
 //    in the same folder as this macro.
 //
 // NOTE: Because weldment_box3.sldprt is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace CreatePartForSolidBody_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         Feature swFeat;
         BodyFolder swBodyFolder;
         bool updateBoolstatus;
         bool boolstatus;
         int longstatus;
         int longWarnings;
         ModelDoc2 currentModel;
         ModelDoc2 swModel;
         int modelType;
         string modelTitle;

         public void Main()
         {
             currentModel = (ModelDoc2)swApp.ActiveDoc;

             modelTitle = currentModel.GetTitle();
             modelType = currentModel.GetType();

             swFeat = (Feature)currentModel.FirstFeature();
             if (swFeat == null)
                 ErrorMsg(swApp, "Failed to get first feature");

             while ((swFeat != null))
             {
                 if (swFeat.GetTypeName2() == "SolidBodyFolder")
                 {
                     swBodyFolder = (BodyFolder)swFeat.GetSpecificFeature2();
                     if (swBodyFolder == null)
                         ErrorMsg(swApp,  "Failed to get body folder");

                     boolstatus = swBodyFolder.SetAutomaticCutList(true);

                     boolstatus = swBodyFolder.UpdateCutList();

                     break;
                 }
                 swFeat = (Feature)swFeat.GetNextFeature();
             }

             updateBoolstatus = false;

             swFeat = (Feature)currentModel.FirstFeature();
             if (swFeat == null)
                 ErrorMsg(swApp, "Failed to get first feature");

             while ((swFeat != null))
             {
                 if (swFeat.GetTypeName2() == "WeldMemberFeat")
                 {
                     boolstatus = swFeat.Select2(false, 0);
                     if (boolstatus == false)
                         ErrorMsg(swApp,  "Failed to select feature");

                     // Save the selected solid body weldment member to another part,
                     // transferring the solid body's cut list properties to the new part's cut list;
                     // automatically creates a weldment and cut list folder
                     boolstatus = ((PartDoc)currentModel).SaveToFile3(swApp.GetCurrentMacroPathFolder() + "\\RefWeldment1" + ".sldprt", 1, swCutListTransferOptions_e.swCutListTransferOptions_CutListProperties, false, "", out longstatus, out longWarnings);

                     System.Diagnostics.Debugger.Break();

                     if (boolstatus == false)
                         ErrorMsg(swApp,  "Failed to insert weldment member into new part");

                     swModel = (ModelDoc2)swApp.ActiveDoc;
                     if (swModel == null)
                         ErrorMsg(swApp,  "Failed to set open model as active document");

                     updateBoolstatus = true;
                     break;
                 }
                 swFeat = (Feature)swFeat.GetNextFeature();
             }

             if (updateBoolstatus == true)
             {
                 swFeat = (Feature)currentModel.FirstFeature();
                 if (swFeat == null)
                     ErrorMsg(swApp,  "Failed to get first feature");

                 while ((swFeat != null))
                 {
                     if (swFeat.GetTypeName2() == "SolidBodyFolder")
                     {
                         swBodyFolder = (BodyFolder)swFeat.GetSpecificFeature2();
                         if (swBodyFolder == null)
                             ErrorMsg(swApp,  "Failed to get body folder");

                         boolstatus = swBodyFolder.SetAutomaticCutList(true);
                         if (boolstatus == false)
                             ErrorMsg(swApp,  "Failed to set cut list to automatic");

                         boolstatus = swBodyFolder.UpdateCutList();
                         if (boolstatus == false)
                             ErrorMsg(swApp,  "Failed to update cut list");

                         swApp.CloseDoc(swModel.GetTitle());
                         break;
                     }
                     swFeat = (Feature)swFeat.GetNextFeature();
                 }
             }

         }

         public void ErrorMsg(SldWorks Swapp, string Message)
         {
             Swapp.SendMsgToUser2(Message, 0, 0);
             Swapp.RecordLine("'*** WARNING - General");
             Swapp.RecordLine("'*** " + Message);
             Swapp.RecordLine("");
         }

         public SldWorks swApp;

     }

 }
```
