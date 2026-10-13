---
title: "Insert General Table Annotation Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_General_Table_in_Part_Example_CSharp.htm"
---

# Insert General Table Annotation Example (C#)

## Get General Table Annotation Example (C#)

This example shows how to create a general table annotation for 3D PDF files in SOLIDWORKS MBD.

```vb
 //--------------------------------------------------------------------------
 // Preconditions: Open a part.
 //
 // Postconditions: None.
 //--------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace GetGeneralTableAnno_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         ModelDocExtension modelDocExt;

         TableAnnotation myTable;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             modelDocExt = Part.Extension;
             myTable = modelDocExt.GetGeneralTableAnnotation(true, 0, 0, (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, "", 2, 2);

         }

         public SldWorks swApp;

     }
 }
```
