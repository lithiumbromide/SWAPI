---
title: "Remove Material Properties from Assembly Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Material_Properties_from_Assembly_Component_Example_VB.htm"
---

# Remove Material Properties from Assembly Component Example (VBA)

This example shows how to remove the material properties from the selected assembly component.

```vb
'--------------------------------------------
'
'  Preconditions:
'      (1)  Assembly is open.
'      (2)  Component with changed material properties (for example, color)
'           is selected.
'
' Postconditions:  Material properties from selected component are removed.
'
'--------------------------------------------
Option Explicit

    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swComp                      As SldWorks.Component2
    Dim swConfig                    As SldWorks.Configuration
    Dim vConfigName                 As Variant
    Dim bRet                        As Boolean

Sub main()

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent2(1)
    ' Get the names of the configurations in the assembly
    vConfigName = swModel.GetConfigurationNames

    ' Remove the material properties from the selected
    ' component in this configuration in this assembly
    bRet = swComp.RemoveMaterialProperty2(swThisConfiguration, (vConfigName))
    Debug.Print (" Material removed: "); bRet

    swModel.GraphicsRedraw2
End Sub
'-----------------------------------------
```
