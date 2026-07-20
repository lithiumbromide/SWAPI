---
title: "Get Dimension Values in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dimension_Values_in_Drawing_Example_VB.htm"
---

# Get Dimension Values in Drawing Example (VBA)

This example shows how to get the values of the dimensions in a drawing.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document.
 ' 2. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
     Dim swModel                     As SldWorks.ModelDoc2
     Dim swDraw                      As SldWorks.DrawingDoc
     Dim swView                      As SldWorks.View
     Dim swDispDim                   As SldWorks.DisplayDimension
     Dim swDim                       As SldWorks.Dimension
     Dim swAnn                       As SldWorks.Annotation

    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swDraw = swModel
    Debug.Print "File = " & swModel.GetPathName
    Set swView = swDraw.GetFirstView
    Do While Not swView Is Nothing
         Debug.Print "  View = " & swView.Name
        Set swDispDim = swView.GetFirstDisplayDimension6
        Do While Not swDispDim Is Nothing
             Set swAnn = swDispDim.GetAnnotation
             Set swDim = swDispDim.GetDimension
            Debug.Print "    ------------------------------------"
             Debug.Print "    AnnName = " & swAnn.GetName
             Debug.Print "      DimFullName                  = " & swDim.FullName
             Debug.Print "      DimName                      = " & swDim.Name
             Debug.Print "      swDimensionParamType_e type  = " & swDim.GetType
             Debug.Print "      DrivenState                  = " & swDim.DrivenState
             Debug.Print "      ReadOnly                     = " & swDim.ReadOnly
             Debug.Print "      Value                        = " & swDim.GetSystemValue2("")
             Debug.Print ""
             Debug.Print "      Arrowside                    = " & swDispDim.ArrowSide
             Debug.Print "      TextAll                      = " & swDispDim.GetText(swDimensionTextAll)
             Debug.Print "      TextPrefix                   = " & swDispDim.GetText(swDimensionTextPrefix)
             Debug.Print "      TextSuffix                   = " & swDispDim.GetText(swDimensionTextSuffix)
             Debug.Print "      CalloutAbove                 = " & swDispDim.GetText(swDimensionTextCalloutAbove)
             Debug.Print "      CalloutBelow                 = " & swDispDim.GetText(swDimensionTextCalloutBelow)
            Set swDispDim = swDispDim.GetNext3
        Loop
        Set swView = swView.GetNextView
    Loop
End Sub
```
