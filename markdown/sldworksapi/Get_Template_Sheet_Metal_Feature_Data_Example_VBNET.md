---
title: "Get Sheet Metal Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Template_Sheet_Metal_Feature_Data_Example_VBNET.htm"
---

# Get Sheet Metal Feature Data Example (VB.NET)

This example shows how to get the sheet metal feature data from a sheet metal part created in SOLIDWORKS 2013 or later.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a sheet metal part created in SOLIDWORKS 2013 or later.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window to see whether a fixed face reference is selected.
 ' 2. Inspect the selection in the graphics window.
 ' 3. Press F5 to finish the macro.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swModelExt As ModelDocExtension
         Dim swSelData As SelectData = Nothing
         Dim swSheetMetalTemplFeature As Feature
         Dim swSheetMetal As SheetMetalFeatureData
         Dim swFixedFace As Face2
         Dim swEntity As Entity
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swModelExt = swModel.Extension

         swSheetMetalTemplFeature = swModelExt.GetTemplateSheetMetal
         swSheetMetal = swSheetMetalTemplFeature.GetDefinition

         ' Roll back the model
         bRet = swSheetMetal.AccessSelections(swModel, Nothing)
         swFixedFace = swSheetMetal.FixedReference

         If Not swFixedFace Is Nothing Then

             Debug.Print("A fixed face or fixed edge is selected.")
             swEntity = swFixedFace
             bRet = swEntity.Select4(False, swSelData)
              Stop

         Else

             ' A fixed face or fixed edge is not required,
             ' so Null is a valid value
             Debug.Print("There is no fixed face or fixed edge in this sheet metal part.")

         End If

         ' Cancel changes and roll forward the model
         swSheetMetal.ReleaseSelectionAccess()

     End Sub

     Public swApp As SldWorks

 End  Class
```
