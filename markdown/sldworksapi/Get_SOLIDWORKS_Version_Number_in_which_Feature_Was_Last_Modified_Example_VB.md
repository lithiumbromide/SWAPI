---
title: "Get Version Number in which Feature Was Last Modified Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_SOLIDWORKS_Version_Number_in_which_Feature_Was_Last_Modified_Example_VB.htm"
---

# Get Version Number in which Feature Was Last Modified Example (VBA)

## Get Version Number in Which Feature Was Last Modified Example (VBA)

This example shows how to get the version number in which the selected feature was last modified.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part and select a feature.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of the selected feature, its type, and the version
'    of SOLIDWORKS Design in which the selected feature was last modified.
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
    Debug.Print "Feature = " + swFeat.Name + "[" + swFeat.GetTypeName + "]"
    Debug.Print "Version of SOLIDWORKS Design in which feature was last modified = " & swFeat.GetModifiedVersion
```

```
End Sub
```
