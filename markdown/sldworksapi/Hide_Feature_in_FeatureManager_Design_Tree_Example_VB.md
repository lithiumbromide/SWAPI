---
title: "Hide Feature in FeatureManager Design Tree Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_Feature_in_FeatureManager_Design_Tree_Example_VB.htm"
---

# Hide Feature in FeatureManager Design Tree Example (VBA)

This example shows how to hide the selected feature in the FeatureManager design tree.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Select a feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Hides the selected feature in the FeatureManager
'    design tree, but it is still visible in the
'    graphics area.
' 2. Examine the Immediate window and graphics area.
'----------------------------------------------------
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
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
```

```
    Debug.Print "Feature = " & swFeat.Name
    Debug.Print "  Type     = " & swFeat.GetTypeName
    Debug.Print "  Hidden   = " & swFeat.GetUIState(swIsHiddenInFeatureMgr)
```

```
    swFeat.SetUIState swIsHiddenInFeatureMgr, True
```

```
    swModel.EditRebuild3
    Debug.Print ""
    Debug.Print "  Hidden   = " & swFeat.GetUIState(swIsHiddenInFeatureMgr)
```

```
End Sub
```
