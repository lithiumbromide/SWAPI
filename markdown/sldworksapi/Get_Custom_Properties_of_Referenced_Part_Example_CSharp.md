---
title: "Get Custom Properties of Referenced Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Custom_Properties_of_Referenced_Part_Example_CSharp.htm"
---

# Get Custom Properties of Referenced Part Example (C#)

This example shows how to get the custom property data of a referenced part.

```vb
 //----------------------------------------------------
 // Preconditions:
 // 1. Open a part that contains a referenced part
 //    with a custom property and a value.
 // 2. Open the referenced part.
 // 3. Switch back to the part opened in step 1.
 // 4. In the macro, replace Property_Name with the name of
 //    the referenced part's custom property.
 // 5. Open the Immediate window.
 //
 // Postconditions: Prints the custom property data
 // to the Immediate window.
 //---------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace Get4CustomPropertyManagerCSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt =  default(ModelDocExtension);
             CustomPropertyManager swCustProp =  default(CustomPropertyManager);
             string val = "";
             string valout = "";
             bool status;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;

             // Get the custom property data
             swCustProp = swModelDocExt.get_CustomPropertyManager("");
             status = swCustProp.Get4("Property_Name", false, out val, out valout);

             Debug.Print("Value:                    " + val);
             Debug.Print("Evaluated value:          " + valout);
             Debug.Print("Up-to-date data:          " + status);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
