---
title: "Hide the FeatureManager Design Tree Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_the_FeatureManager_Example_VB.htm"
---

# Hide the FeatureManager Design Tree Example (VBA)

This example shows how to hide the FeatureManager design tree.

```
'------------------------------------------------------
' Preconditions: Open a model document.
'
' Postconditions:
' 1. Hides the FeatureManager design tree.
' 2. Examine SOLIDWORKS Design.
'--------------------------------------

Option Explicit
```

```vb
Sub main()

     Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swModDocExt As SldWorks.ModelDocExtension
     Dim bRet As Boolean

     Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModDocExt = swModel.Extension
     bRet = swModDocExt.HideFeatureManager(True)

 End Sub
```
