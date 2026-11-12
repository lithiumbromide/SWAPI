---
title: "Insert and Change DeleteFace Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm"
---

# Insert and Change DeleteFace Feature Example (C#)

This example shows how to insert a DeleteFace feature and how to modify that feature.

```vb
// ---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\fillets\knob.sldprt.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates and modifies a DeleteFace feature.
 // 2. Examine the Immediate window.
 //
 // NOTE: Because this part document is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace DeleteFaceFeatureDataCSharp.csproj
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {
        ModelDoc2 swModel = default(ModelDoc2);
         ModelDocExtension swModelDocExt = default(ModelDocExtension);
         Feature swFeature = default(Feature);
         DeleteFaceFeatureData swDeleteFaceFeature = default(DeleteFaceFeatureData);
         string featureName = null;
         bool boolstatus = false;
         int opt = 0;

        swModel = (ModelDoc2)swApp.ActiveDoc;
         swModelDocExt = (ModelDocExtension)swModel.Extension;

        // Select a face for the
         // DeleteFace feature
         boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.002251015125069, -0.001872569429423, 0.02015405789763, false, 0, null, 0);

        // Create a DeleteFace feature
         boolstatus = swModelDocExt.InsertDeleteFace((int)swFaceDeleteOption_e.swFaceDelete_Default);

         // Get the DeleteFace feature
         swFeature = (Feature)swModel.FirstFeature();
         while ((swFeature != null)) {
             featureName = swFeature.Name;
            while (featureName != "DeleteFace1") {
                 swFeature = (Feature)swFeature.GetNextFeature();
                 featureName = swFeature.Name;
             }

            Debug.Print("Feature name: " + featureName);
             swDeleteFaceFeature = (DeleteFaceFeatureData)swFeature.GetDefinition();
             boolstatus = swDeleteFaceFeature.AccessSelections(swModel, null);
             Debug.Print(" Number of deleted faces: " + swDeleteFaceFeature.GetDeletedFacesCount());

            // Get the DeleteFace feature's option
             opt = swDeleteFaceFeature.Options;
             Debug.Print(" Before changing the option...");
             DeleteFaceOptions(opt);

            // Change the DeleteFace feature's option
             swDeleteFaceFeature.Options = (int)swFaceDeleteOption_e.swFaceDelete_Patch;
             opt = swDeleteFaceFeature.Options;
             Debug.Print(" After changing the option...");
             DeleteFaceOptions(opt);

            // Save modification made to DeleteFace feature
             boolstatus = swFeature.ModifyDefinition(swDeleteFaceFeature, swModel, null);

            // Get next feature until no more features
             swFeature = (Feature)swFeature.GetNextFeature();
        }
    }

    public void DeleteFaceOptions(long options)
     {
         switch (options) {
             case 0:
                 Debug.Print("  Option = swFaceDelete_Default");
                 break;
             case 1:
                 Debug.Print("  Option = swFaceDelete_Patch");
                 break;
             case 2:
                 Debug.Print("  Option = swFaceDelete_Fill");
                 break;
             case 3:
                 Debug.Print("  Option = swFaceDelete_FillWithTangent");
                 break;
         }
     }

        /// <summary>
         ///  The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
    }
}
```
