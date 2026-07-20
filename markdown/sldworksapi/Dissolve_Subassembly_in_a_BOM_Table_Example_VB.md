---
title: "Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Dissolve_Subassembly_in_a_BOM_Table_Example_VB.htm"
---

# Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (VBA)

This example shows how to expand, collapse, dissolve, and restore a subassembly in a BOM table.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\assemblyvisualize\food_processor.sldasm.
 ' 2. Select File > Make Drawing from Assembly.
 ' 3. Click OK.
 ' 4. Drag one or more views onto the drawing.
 ' 5. Ensure that the specified template exists.
 '
 ' Postconditions:
 ' 1. Inserts an indented BOM table in the drawing.
 ' 2. Collapses the blade shaft subassembly. Press F5 to continue.
 ' 3. Expands the blade shaft subassembly. Press F5 to continue.
 ' 4. Dissolves the blade shaft subassembly. Press F5 to restore the blade
 '    shaft subassembly.
 '
 ' NOTE: Because this document is used by a SOLIDWORKS
 ' online tutorial, do not save any changes when
 ' closing it.
 '-----------------------------------------------------------------------------
 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim swModelDocExt           As SldWorks.ModelDocExtension
 Dim swDrawing               As SldWorks.DrawingDoc
 Dim swView                  As SldWorks.View
 Dim boolstatus              As Boolean
 Dim swBOMAnnotation         As SldWorks.BomTableAnnotation
 Dim AnchorType              As Long
 Dim BomType                 As Long
 Dim Configuration           As String
 Dim TableTemplate           As String
 Option Explicit
 Sub main()
     Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set swDrawing = Part
     Set swModelDocExt = Part.Extension
    boolstatus = swDrawing.ActivateView("Drawing View1")
     Set swView = swDrawing.ActiveDrawingView
     AnchorType = swBOMConfigurationAnchor_TopLeft
     BomType = swBomType_Indented
     TableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
     Configuration = ""
     Set swBOMAnnotation = swView.InsertBomTable6(False, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate, False, swNumberingType_Detailed, True, True, True)

    'Collapse blade shaft subassembly
     swBOMAnnotation.Collapse 1, 8
     Stop

    'Expand blade shaft subassembly
     swBOMAnnotation.Expand 1, 8
     Stop

    'Dissolve blade shaft subassembly
     boolstatus = swBOMAnnotation.Dissolve(8)
     Stop

    'Restore blade shaft subassembly
     boolstatus = swBOMAnnotation.RestoreRestructuredComponents(0)

End Sub
```
