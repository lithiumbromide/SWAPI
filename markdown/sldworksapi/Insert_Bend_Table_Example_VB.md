---
title: "Insert Bend Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Bend_Table_Example_VB.htm"
---

# Insert Bend Table Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim swView As SldWorks.View
 Dim myBendTableAnnot As SldWorks.BendTableAnnotation
 Dim myBendTableFeat As SldWorks.BendTable
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    Set swView = Part.SelectionManager.GetSelectedObjectsDrawingView2(1, -1)
     Set myBendTableAnnot = swView.InsertBendTable(False, 0.3018189506239, 0.4876053587373, swBOMConfigurationAnchor_TopLeft, "A", "install_dir\lang\english\bendtable-standard.sldbndtbt")

    Set myBendTableFeat = myBendTableAnnot.BendTable
     Debug.Print myBendTableFeat.GetFeature.Name
     Debug.Print "Starting tag: " & myBendTableFeat.StartingValue
     Debug.Print "swBendTableTagStyle_e option: " & myBendTableFeat.TagStyle
     Debug.Print "Number of bend table annotations: " & myBendTableFeat.GetTableAnnotationCount

    Part.ClearSelection2 True

End Sub
```
