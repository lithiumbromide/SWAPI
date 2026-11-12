---
title: "Get Version Number in which Feature Was Created Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_SOLIDWORKS_Version_Number_in_Which_Feature_Was_Created_Example_VB.htm"
---

# Get Version Number in which Feature Was Created Example (VBA)

This example shows how to get the version number in which the selected feature was created.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part and select a feature.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the version of SOLIDWORKS Design in which the selected
'    feature was created.
' 2. Examine the Immediate window.
'-------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Debug.Print "Version of SOLIDWORKS Design in which feature was created = " & swFeat.GetCreatedVersion
```

```
End Sub
```
