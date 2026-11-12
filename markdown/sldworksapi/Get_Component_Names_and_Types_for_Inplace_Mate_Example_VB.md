---
title: "Get Component Names and Types for Inplace Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_Names_and_Types_for_Inplace_Mate_Example_VB.htm"
---

# Get Component Names and Types for Inplace Mate Example (VBA)

This example shows how to get the names of the components for an Inplace mate.

```
'----------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\bladed shaft.sldasm.
' 2. In the FeatureManager design tree, expand blade extension >
'    Mates in bladed shaft and click Inplace5.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the Inplace mate.
' 2. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub ProcessMateInPlace(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swMateInPlace As SldWorks.MateInPlace)
```

```
    Dim swComp As SldWorks.Component2
    Dim nNumMateEnt As Long
    Dim i As Long
```

```
    Set swComp = swMateInPlace.Component: Debug.Assert Not Nothing Is swComp
```

```
    nNumMateEnt = swMateInPlace.GetMateEntityCount
```

```
    Debug.Print "    Component = " & swComp.Name2
    For i = 0 To nNumMateEnt - 1
        Debug.Print "    Mate Component = " & swMateInPlace.MateComponentName(i)
        Debug.Print "      Type of Inplace mate entity = " & swMateInPlace.MateEntityType(i)
    Next i
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
    Dim swMateInPlace As SldWorks.MateInPlace
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swMateInPlace = swFeat.GetSpecificFeature2
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name & " [" & swFeat.GetTypeName & "]"
```

```
    ProcessMateInPlace swApp, swModel, swMateInPlace
```

```
End Sub
```
