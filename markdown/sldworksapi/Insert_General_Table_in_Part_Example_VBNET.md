---
title: "Insert General Table in Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_General_Table_in_Part_Example_VBNET.htm"
---

# Insert General Table in Part Example (VB.NET)

This example shows how to insert a general table annotation into a model document.

```vb
 '---------------------------------------------------
 ' Preconditions: Open a part.
 '
 ' Postconditions:
 ' 1. Inserts a general table in the part.
 ' 2. Examine the graphics area.
 '---------------------------------------------------
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
         myTable = modelDocExt.InsertGeneralTableAnnotation(True, 0, 0, swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft,  "", 2, 2)

     End Sub

     Public swApp As SldWorks

 End  Class
```
