---
title: "Get Dimension of Distance Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dimension_of_Distance_Mate_Example_VB.htm"
---

# Get Dimension of Distance Mate Example (VBA)

This example shows how to get the dimension value of a distance mate in an assembly.

NOTE: You can use this sample code to get all the dimension values for any selected feature in the FeatureManager design tree.

```
'-------------------------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\motor casing and switch top plate.sldasm.
' 2. Expand MateGroup1 and select Distance8.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the dimension value of Distance8.
' 2. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'------------------------------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub ProcessFeature(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swFeat As SldWorks.Feature)
    Dim swDispDim  As SldWorks.DisplayDimension
    Dim swDim As SldWorks.Dimension
    Dim dimValue As Variant
```

```
    Debug.Print "  " + swFeat.Name
```

```
    Set swDispDim = swFeat.GetFirstDisplayDimension
    While (Not swDispDim Is Nothing)
        Set swDim = swDispDim.GetDimension
        dimValue = swDim.GetSystemValue3(swThisConfiguration, Empty)
        Debug.Print "    " + swDim.FullName + " = " & (dimValue(0) * 1000) & " mm "
        Set swDispDim = swFeat.GetNextDisplayDimension(swDispDim)
    Wend
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Debug.Print "File = " & swModel.GetPathName
    ProcessFeature swApp, swModel, swFeat
```

```
End Sub
```
