---
title: "Get Sheet Metal Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Template_Sheet_Metal_Feature_Data_Example_VB.htm"
---

# Get Sheet Metal Feature Data Example (VBA)

This example shows how to get the sheet metal feature data from a sheet metal part created in SOLIDWORKS 2013 or later.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a sheet metal part created in SOLIDWORKS 2013 or later.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window to see whether
 ' a fixed face reference is selected.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swModelExt              As SldWorks.ModelDocExtension
     Dim swSelData               As SldWorks.SelectData
     Dim swSheetMetalTemplFeature            As SldWorks.Feature
     Dim swSheetMetal            As SldWorks.SheetMetalFeatureData
     Dim swFixedFace             As SldWorks.Face2
     Dim bRet                    As Boolean
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swModelExt = swModel.Extension

    Set swSheetMetalTemplFeature = swModelExt.GetTemplateSheetMetal
     Set swSheetMetal = swSheetMetalTemplFeature.GetDefinition

    ' Roll back the model
    bRet = swSheetMetal.AccessSelections(swModel, Nothing)
     Set swFixedFace = swSheetMetal.FixedReference
    If Not swFixedFace Is Nothing Then
        Debug.Print "A fixed face or fixed edge is selected."
         bRet = swFixedFace.Select4(False, swSelData)
    Else
        ' A fixed face or fixed edge is not required,
         ' so Null is a valid value
         Debug.Print "There is no fixed face or fixed edge in this sheet metal part."
    End If
    ' Cancel changes and roll forward the model
     swSheetMetal.ReleaseSelectionAccess
End Sub
```
