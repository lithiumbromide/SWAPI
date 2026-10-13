---
title: "Set Material Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Material_Example_CSharp.htm"
---

# Set Material Example (C#)

This example shows how to get the names of the material schema, material databases, and bodies in a part document. This example also shows how to apply a SOLIDWORKS Design Material to all of the bodies in a part document.

```vb
//----------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified document exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified part document.
 // 2. Applies the material ABS PC (polycarbonate plastic)
 //    from the Material database to all
 //    bodies in the part.
 // 3. To verify, examine:
 //    * DisplayManager tab
 //    * graphics area
 //    * Immediate window
 //
 // NOTE: Because the part document is used elsewhere,
 // do not save changes.
 //----------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetMaterialBodyCSharp.csproj
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             PartDoc swPart = default(PartDoc);
             Body2 swBody = default(Body2);
             int errors = 0;
             int warnings = 0;
             object[] vMatDBarr = null;
             object[] vMatDB = null;
             object[] Bodies = null;
             int BodyMaterialError = 0;
             string sMatName = "";
             string sMatDB = "";
             int i = 0;
             int j = 0;

             // Open the document
             swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt", (int)swDocumentTypes_e.swDocPART,
 (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swPart = (PartDoc)swModel;
             // Get the material schema and names
             // of available materials databases
             vMatDBarr = (object[])swApp.GetMaterialDatabases();
             Debug.Print("Material schema pathname = " + swApp.GetMaterialSchemaPathName());
             for (i=0; i < vMatDBarr.Length; i++)
             {
                 Debug.Print(" Material database: " + vMatDB);
             }
             Debug.Print("");
             Bodies = (object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, false);
             for (j = 0; j < Bodies.Length; j++)
             {
                 swBody = (Body2)Bodies[j];
                 // Get the name of the body
                 Debug.Print(swBody.Name);

                 swBody.Select2(false, null);

                 // Set the SOLIDWORKS Design material for that body
                 BodyMaterialError = swBody.SetMaterialProperty("Default", "solidworks
 materials.sldmat", "ABS PC");
                 // Comment out the previous statement and uncomment the following statement to use
 custom material
                 //BodyMaterialError = swBody.SetMaterialProperty("Default", "custom materials.sldmat",
 "Custom Plastic");

                 // Get the names of the body's material and the
                 // database to which it belongs
                 sMatName = swBody.GetMaterialPropertyName("", out sMatDB);
                 if (string.IsNullOrEmpty(sMatName))
                 {
                     Debug.Print("Body " + j + "'s material name: No material applied");
                 }
                 else
                 {
                     Debug.Print("Body " + j + "'s material name: " + sMatName);
                     Debug.Print("Body " + j + "'s material database: " + sMatDB);
                     Debug.Print(" ");
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
