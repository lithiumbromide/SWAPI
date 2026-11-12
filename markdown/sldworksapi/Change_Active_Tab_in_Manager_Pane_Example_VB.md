---
title: "Change Active Tab in Manager Pane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Active_Tab_in_Manager_Pane_Example_VB.htm"
---

# Change Active Tab in Manager Pane Example (VBA)

This example shows how to change the active tab in the Manager Pane.

'------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly and click the FeatureManager design tree tab
' in the Manager Pane.
' 2. In the SOLIDWORKS Microsoft Visual Basic for Applications IDE:
' a. Copy [Main](#Main) to the main module.
' b. Click **Insert > Class Module** and copy [Class1](#Class1) to that module.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Ensures that the Manager Pane is visible.
' 2. Traverses the tabs in the Manager Pane:
' a. Changes the active tab.
' b. Fires a notification.
' 3. Examine the Immediate window and Manager Pane.
'-------------------------------------------------------------------
'Main

Option Explicit

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExtension As SldWorks.ModelDocExtension
Dim swAssembly As SldWorks.AssemblyDoc
Dim swModelViewManager As SldWorks.ModelViewManager
Dim tabs As Variant
Dim nbrTabs As Long
Dim nbrTab As Long
Dim swAssemblyEvents As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssembly = swModel
    Set swModelDocExtension = swModel.Extension
```

```
    'Set up events
    Set swAssemblyEvents = New Class1
    Set swAssemblyEvents.swAssembly = swApp.ActiveDoc
```

```
    Set swModelViewManager = swModel.ModelViewManager
```

```
    'Ensure that Manager Pane is visible
    swModelDocExtension.HideFeatureManager (False)
```

```
    'Get the tabs in the Manager Pane
    tabs = swModelViewManager.GetFeatureManagerTabs
    nbrTabs = UBound(tabs) + 1
    Debug.Print "Number of tabs in Manager Pane: " & nbrTabs
```

```
    'Traverse the tabs in the Manager Pane and change the active tab
    For nbrTab = 0 To UBound(tabs)
        swModelViewManager.ActiveFeatureManagerTabIndex = nbrTab
    Next nbrTab
```

```
    Debug.Print ""
```

```
    'Get each tab's index
    Debug.Print "FeatureManager design tree tab index: " & swModelViewManager.GetFeatureManagerTreeTabIndex
    Debug.Print "PropertyManager tab index:            " & swModelViewManager.GetPropertyManagerTabIndex
    Debug.Print "ConfigurationManager tab index:       " & swModelViewManager.GetConfigurationManagerTabIndex
    Debug.Print "DimXpertManager tab index:            " & swModelViewManager.GetDimXpertManagerTabIndex
    Debug.Print "DisplayManager tab index:             " & swModelViewManager.GetDisplayManagerTabIndex
```

```
End Sub
```

```
Back to top
```

```
'Class1
Option Explicit
```

```
Public WithEvents swAssembly As SldWorks.AssemblyDoc
```

```
Public Function swAssembly_FeatureManagerTabActivatedNotify(ByVal commandIndex As Long, ByVal commandTabName As String) As Long
    Debug.Print "Activated tab " & commandIndex & " whose name is " & commandTabName
End Function
```

```
Back to top
```
