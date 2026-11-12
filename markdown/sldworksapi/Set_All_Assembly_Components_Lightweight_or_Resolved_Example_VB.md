---
title: "Set All Assembly Components Lightweight or Resolved Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_All_Assembly_Components_Lightweight_or_Resolved_Example_VB.htm"
---

# Set All Assembly Components Lightweight or Resolved Example (VBA)

This example shows how to set all assembly components to either lightweight or resolved.

```
'-----------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Sets all assembly components to either
'    lightweight or fully resolved.
' 2. Examine the FeatureManager design tree
'    and Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub ProcessComponent(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swComp As SldWorks.Component2, swComponentSuppressionState As swComponentSuppressionState_e, sPadStr As String)
```

```
    Dim vChildCompArr As Variant
    Dim vChildComp As Variant
    Dim swChildComp As SldWorks.Component2
    Dim nRetVal As Long
```

```
    vChildCompArr = swComp.GetChildren
    For Each vChildComp In vChildCompArr
        Set swChildComp = vChildComp
        nRetVal = swChildComp.SetSuppression2(swComponentSuppressionState)
        Debug.Print sPadStr & swChildComp.Name2 & " <" & swChildComp.ReferencedConfiguration & "> --> " & swChildComp.GetPathName
        ProcessComponent swApp, swModel, swChildComp, swComponentSuppressionState, sPadStr + "  "
    Next vChildComp
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
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConfig As SldWorks.Configuration
    Dim swRootComp As SldWorks.Component2
    Dim bRet As Boolean
    Dim nSuppressState As Long
    Dim nResponse As Long
```

```
    nResponse = MsgBox("Set all components to lightweight or resolved (Yes = Lightweight; No = Resolved)?", vbYesNo)
    If nResponse = vbYes Then
        nSuppressState = swComponentLightweight
    Else
        nSuppressState = swComponentFullyResolved
    End If
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swFeatMgr = swModel.FeatureManager
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
    Set swRootComp = swConfig.GetRootComponent3(True)
    swFeatMgr.EnableFeatureTree = False
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    ProcessComponent swApp, swModel, swRootComp, nSuppressState, "  "
```

```
    swFeatMgr.EnableFeatureTree = True
```

```
End Sub
```
