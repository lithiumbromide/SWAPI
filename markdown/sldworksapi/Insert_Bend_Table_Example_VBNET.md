---
title: "Insert Bend Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Bend_Table_Example_VBNET.htm"
---

# Insert Bend Table Example (VB.NET)

This example shows how to insert a bend table in a drawing of a flattened sheet metal part.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing that contains a flat pattern view
 '    of a flattened sheet metal part.
 ' 2. Replace install_dir with your SOLIDWORKS installation directory.
 ' 3. Select the flat pattern view (Drawing View1)
 '    in the FeatureManager design tree.
 '
 ' Postconditions:
 ' 1. A bend table is inserted for the selected view.
 ' 2. Inspect the Immediate Window.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim swView As View
     Dim myBendTableAnnot As BendTableAnnotation
     Dim myBendTableFeat As BendTable

     Sub main()

         Part = swApp.ActiveDoc

         swView = Part.SelectionManager.GetSelectedObjectsDrawingView2(1, -1)
         myBendTableAnnot = swView.InsertBendTable(False, 0.3018189506239, 0.4876053587373,  swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, "A", "install_dir\lang\english\bendtable-standard.sldbndtbt")

         myBendTableFeat = myBendTableAnnot.BendTable
         Debug.Print(myBendTableFeat.GetFeature.Name)
         Debug.Print("Starting tag: " & myBendTableFeat.StartingValue)
         Debug.Print("swBendTableTagStyle_e option: " & myBendTableFeat.TagStyle)
         Debug.Print("Number of bend table annotations: " & myBendTableFeat.GetTableAnnotationCount)

         Part.ClearSelection2(True)

     End Sub

     Public swApp As SldWorks

 End  Class
```
