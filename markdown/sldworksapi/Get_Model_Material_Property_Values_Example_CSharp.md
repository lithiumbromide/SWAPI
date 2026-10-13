---
title: "Get Model Material Property Values Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Material_Property_Values_Example_CSharp.htm"
---

# Get Model Material Property Values Example (C#)

This example shows how to get the material property values of components in lightweight mode.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\TopAssembly1.SLDASM in lightweight
 //    mode.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets the material property values of the lightweight components in the
 //    model.
 // 2. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetMatPropValues_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swDoc;
         AssemblyDoc swADoc;
         object[] varComp;
         double[] varMatProp;

         public void Main()
         {
             swDoc = (ModelDoc2)swApp.ActiveDoc;
             swADoc = (AssemblyDoc)swDoc;
             varComp = (object[])swADoc.GetComponents(true);
             int I = 0;
             for (I = 0; I < varComp.Length; I++)
             {
                 Component2 swComp = default(Component2);
                 swComp = (Component2)varComp[I];

                 varMatProp = (double[])swComp.GetModelMaterialPropertyValues(swComp.ReferencedConfiguration);
                 if (!((varMatProp == null)))
                 {
                     Debug.Print(swComp.Name2 + "(" + I + ")" + "ConfigName : " + swComp.ReferencedConfiguration + "MatProp : ");
                     Debug.Print("Red: " + (varMatProp[0]) * 255.0);
                     Debug.Print("Green: " + (varMatProp[1]) * 255.0);
                     Debug.Print("Blue: " + (varMatProp[2]) * 255.0);
                     Debug.Print("Ambient: " + (varMatProp[3]) * 100.0 +  "%");
                     Debug.Print("Diffuse: " + (varMatProp[4]) * 100.0 +  "%");
                     Debug.Print("Specularity: " + (varMatProp[5]) * 100.0 +  "%");
                     Debug.Print("Shininess: " + (varMatProp[6]) * 100.0 +  "%");
                     Debug.Print("Transparency: " + (varMatProp[7]) * 100.0 +  "%");
                     Debug.Print("Emission: " + (varMatProp[8]) * 100.0 +  "%");
                 }

                 Debug.Print("");
             }
             varComp = null;
         }

         public SldWorks swApp;

     }
 }
```
