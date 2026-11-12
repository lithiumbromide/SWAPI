---
title: "Get Model Textures Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Texture_Example_CSharp.htm"
---

# Get Model Textures Example (C#)

This example shows how to get the texture applied to components that are displayed in lightweight mode.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open in lightweight mode public_documents\samples\tutorial\api\TopAssembly1.SLDASM
 // 2. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window for the textures of the
 // lightweight components in the model.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetModelTexture_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swDoc;
         AssemblyDoc swADoc;
         object varComp;
         Object[] compArray;
         Texture swTexture;

         public void Main()
         {
             swDoc = (ModelDoc2)swApp.ActiveDoc;
             swADoc = (AssemblyDoc)swDoc;
             varComp = swADoc.GetComponents(true);
             compArray = (Object[])varComp;

             int I = 0;
             string compName = null;
             for (I = 0; I < compArray.Length; I++)
             {
                 Component2 swComp = default(Component2);
                 swComp = (Component2)compArray[I];
                 compName = swComp.ReferencedConfiguration;

                 swTexture = swComp.GetModelTexture(compName);
                 if ((swTexture != null))
                 {
                     Debug.Print(swComp.Name2 + "(" + I + ")" + "ConfigName : " + compName + "MatProp : ");
                     Debug.Print(swTexture.MaterialName);
                     Debug.Print("");
                 }
             }
             varComp = null;

         }

         public SldWorks swApp;

     }
 }
```
