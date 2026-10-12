---
title: "Get Whether Components Are Loaded Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Components_Are_Loaded_Example_VB.htm"
---

# Get Whether Components Are Loaded Example (VBA)

This example gets whether the components in an assembly document are loaded.

```vb
'--------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified assembly document exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Loads the Magnet-1 component.
 ' 2. Examine the Immediate window.
 '
 ' NOTE: Because this assembly document is used elsewhere,
 ' do not save changes.
 '-------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim sComponents(0) As String
Dim Components As Variant
Dim swComponent As SldWorks.Component2
Dim sName As String
Dim swAssembly As SldWorks.AssemblyDoc
Dim longstatus As Long, longwarnings As Long
Dim i As Long
Dim swConfigMgr As SldWorks.ConfigurationManager
Dim swConfig As SldWorks.Configuration

Sub main()
```

```vb
Set swApp = Application.SldWorks

' Selectively open speaker.sldasm
' Load only the Magnet-1 component
Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\pdmworks\speaker.sldasm")
sComponents(0) = "Magnet-1@speaker"
Components = sComponents
swDocSpecification.ComponentList = Components
swDocSpecification.Selective = True
sName = swDocSpecification.FileName
swDocSpecification.DocumentType = swDocASSEMBLY
swDocSpecification.DisplayState = "Default_Display State-1"
swDocSpecification.UseLightWeightDefault = True
swDocSpecification.LightWeight = True
swDocSpecification.Silent = True
swDocSpecification.IgnoreHiddenComponents = True
Set swModel = swApp.OpenDoc7(swDocSpecification)
longstatus = swDocSpecification.Error
longwarnings = swDocSpecification.Warning

' Get whether the components in the
' assembly document are loaded and suppressed; only
' Magnet-1 should be loaded and not suppressed
Set swAssembly = swModel
Set swConfigMgr = swModel.ConfigurationManager
Set swConfig = swConfigMgr.ActiveConfiguration
Components = swAssembly.GetComponents(True)
For i = 0 To UBound(Components)
    Set swComponent = Components(i)
    If (swComponent.IsLoaded) Then
        Debug.Print "Component: " & swComponent.Name & " is loaded."
    Else
        Debug.Print "Component: " & swComponent.Name & " is not loaded. "
    End If

    Debug.Print " Suppressed: " & swConfig.GetComponentSuppressionState(swComponent.Name)
    Debug.Print ""

Next
```

```vb
End Sub
```
