---
title: "Get Face Hatch Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Face_Hatch_Data_Example_CSharp.htm"
---

# Get Face Hatch Data Example (C#)

This example shows how to get the number of face hatches in a standard or derived (detail, section, projected, broken, etc.) drawing view and their data.

```vb
//------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\introsw\bolt-assembly.slddrw.
 // 2. Select Section View A-A in the FeatureManager design tree.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets face hatch data.
 // 2. Examine the Immediate window.
 //--------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace UseMaterialHatchFaceHatchCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             View swView = default(View);
             object[] vFaceHatch = null;
             FaceHatch swFaceHatch = default(FaceHatch);
             int i = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swView = (View)swSelMgr.GetSelectedObject6(1, -1);
             Debug.Print("View = " + swView.Name);
             Debug.Print(" Type = " + swView.Type);
             vFaceHatch = (object[])swView.GetFaceHatches();
             if ((vFaceHatch == null))
             {
                 Debug.Print(" No face hatches in selected view.");
                 return;
             }
             Debug.Print(" Number of face hatches in this view = " + (vFaceHatch.Length));
             if ((vFaceHatch != null))
             {
                 Debug.Print(" Face hatches =");
                 Debug.Print("");
                 for (i = 0; i <= vFaceHatch.Length - 1; i++)
                 {
                     swFaceHatch = (FaceHatch)vFaceHatch[i];
                     // Get face hatch data
                     // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
                     Debug.Print("   Angle               = " + swFaceHatch.Angle * 57.3 + " degrees");
                     Debug.Print("   Color               = " + swFaceHatch.Color);
                     Debug.Print("   Definition          = " + swFaceHatch.Definition);
                     Debug.Print("   Layer               = " + swFaceHatch.Layer);
                     Debug.Print("   Pattern             = " + swFaceHatch.Pattern);
                     Debug.Print("   Scale               = " + swFaceHatch.Scale2);
                     Debug.Print("   SolidFill           = " + swFaceHatch.SolidFill);
                     Debug.Print("   Material crosshatch = " + swFaceHatch.UseMaterialHatch);
                     Debug.Print("   -----------------------");
                 }
             }
         }
         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```
