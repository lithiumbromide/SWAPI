---
title: "Iterate Through Dimensions in Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Iterate_Through_Dimensions_in_Model_Example_VB.htm"
---

# Iterate Through Dimensions in Model Example (VBA)

This example shows how to iterate through the features and dimensions in a part.

```
'--------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\lesson2\tutor1.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Iterates through the features and dimensions in the part.
' 2. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeat As SldWorks.Feature
    Dim swSubFeat As SldWorks.Feature
    Dim swDispDim As SldWorks.DisplayDimension
    Dim swDim As SldWorks.Dimension
    Dim swAnn As SldWorks.Annotation
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swFeat = swModel.FirstFeature
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    Do While Not swFeat Is Nothing
        Debug.Print "  " + swFeat.Name
```

```
        Set swSubFeat = swFeat.GetFirstSubFeature
        Do While Not swSubFeat Is Nothing
            Debug.Print "      " + swSubFeat.Name
            Set swDispDim = swSubFeat.GetFirstDisplayDimension
            Do While Not swDispDim Is Nothing
                Set swAnn = swDispDim.GetAnnotation
                Set swDim = swDispDim.GetDimension
                Debug.Print "          [" & swDim.FullName & "] = " & swDim.GetSystemValue2("")
                Set swDispDim = swSubFeat.GetNextDisplayDimension(swDispDim)
            Loop
            Set swSubFeat = swSubFeat.GetNextSubFeature
        Loop
        Set swDispDim = swFeat.GetFirstDisplayDimension
        Do While Not swDispDim Is Nothing
            Set swAnn = swDispDim.GetAnnotation
            Set swDim = swDispDim.GetDimension
            Debug.Print "    [" & swDim.FullName & "] = " & swDim.GetSystemValue2("")
            Set swDispDim = swFeat.GetNextDisplayDimension(swDispDim)
        Loop
        Set swFeat = swFeat.GetNextFeature
    Loop
```

```
End Sub
```
