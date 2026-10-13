---
title: "Insert General Table Annotation Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_General_Table_in_Part_Example_VBNET.htm"
---

# Insert General Table Annotation Example (VB.NET)

## Get General Table Annotation Example (VB.NET)

This example shows how to create a general table annotation for 3D PDF files in SOLIDWORKS MBD.

```vb
 '--------------------------------------------------------------------------
 ' Preconditions: Open a part.
 '
 ' Postconditions: None.
 '--------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim modelDocExt As ModelDocExtension
     Dim myTable As TableAnnotation

     Sub main()

         Part = swApp.ActiveDoc
         modelDocExt = Part.Extension
         myTable = modelDocExt.GetGeneralTableAnnotation(True, 0, 0, swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft,  "", 2, 2)

     End Sub

     Public swApp As SldWorks

 End  Class
```
