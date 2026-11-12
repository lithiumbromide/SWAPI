---
title: "Get Render References (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Render_References_Example_CSharp.htm"
---

# Get Render References (C#)

This example shows how to get the render stock (SOLIDWORKS-supplied) references for a model.

```vb
 //-------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified part to open and
 //    kitchen background scene files exist.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Inserts the kitchen background scene in the part.
 // 2. Gets the names of the render references.
 // 3. Examine the Immediate window.
 //
 // NOTE: Because the part is used elsewhere, do
 // not save changes.
 //--------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace GetRenderStockReferencesCSharp.csproj
 {

     partial  class  SolidWorksMacro
     {

         public  void Main()
         {

             ModelDoc2 swModel;
             ModelDocExtension swModelDocExt;
             string modelName = null;
             object[] renderReferences = null;
             bool status = false;
             int errors = 0;
             int warnings = 0;
             int i = 0;

             modelName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\toaster.sldprt";
             swModel = (ModelDoc2)swApp.OpenDoc6(modelName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "",  ref errors,  ref warnings);
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Insert kitchen background scene
             // and rebuild the model to see it
             status = swModelDocExt.InsertScene("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\data\\graphics\\scenes\\03 presentation scenes\\00 kitchen_background.p2s");
             status = swModel.ForceRebuild3(true);

             // Get the render stock references for the
             // kitchen background scene and print
             // them to the Immediate window
             renderReferences = (object[])swModelDocExt.GetRenderStockReferences();
             for (i = 0; i <= renderReferences.GetUpperBound(0); i++)
             {
                 Debug.Print("Render reference: " + renderReferences[i]);

             }
         }

         ///  <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;

     }
 }
```
