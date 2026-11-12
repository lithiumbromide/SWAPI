---
title: "Get and Set Component's Suppression State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Component_s_Suppression_State_Example_VB.htm"
---

# Get and Set Component's Suppression State Example (VBA)

This example shows how to get and set the suppression state of a fully resolved component in an assembly.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Select a component.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Sets the selected component's suppression state to
'    lightweight if the component is resolved.
' 2. Examine the Immediate window and the component in the
'    the FeatureManager design tree.
'--------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swComp                      As SldWorks.Component2
    Dim bRet                        As Boolean
    Dim nRetVal                     As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Comp = " & swComp.Name2
    Debug.Print "    Path = " & swComp.GetPathName
    Debug.Print "    Suppression state as defined in swComponentSuppressionState_e = " & swComp.GetSuppression2
    Debug.Print "    Is suppressed? " & swComp.IsSuppressed
```

```
    nRetVal = swComp.SetSuppression2(swComponentSuppressionState_e.swComponentFullyLightweight)
    Debug.Print "    Is set lightweight (2 = state was changed) =  " & nRetVal
```

```
End Sub
```
