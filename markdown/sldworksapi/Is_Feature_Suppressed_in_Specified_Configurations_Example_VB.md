---
title: "Is Feature Suppressed in Configuration Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Is_Feature_Suppressed_in_Specified_Configurations_Example_VB.htm"
---

# Is Feature Suppressed in Configuration Example (VBA)

This example shows how to find out if a feature is suppressed in the specified configurations.

```
'-------------------------------------------------
' Preconditions:
' 1. Open a part or assembly with one configuration.
' 2. Select a feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Finds out if the selected feature is
'    suppressed in the configuration.
' 2. Examine the Immediate window.
'-------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim vConfNameArr As Variant
    Dim vSuppStateArr As Variant
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
```

```
    vConfNameArr = swModel.GetConfigurationNames
    vSuppStateArr = swFeat.IsSuppressed2(swThisConfiguration, vConfNameArr)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name
    For i = 0 To UBound(vConfNameArr)
        Debug.Print "    " & vConfNameArr(i) & " ---> " & vSuppStateArr(i)
    Next i
```

```
End Sub
```
