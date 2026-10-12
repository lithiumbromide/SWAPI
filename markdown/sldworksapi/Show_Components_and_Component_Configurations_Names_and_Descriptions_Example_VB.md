---
title: "Show Components and Component Configurations Names and Descriptions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Show_Components_and_Component_Configurations_Names_and_Descriptions_Example_VB.htm"
---

# Show Components and Component Configurations Names and Descriptions Example (VBA)

This example shows how to show and hide component and configuration names and descriptions in the FeatureManager design tree.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\smartcomponents\pillow_block.sldasm.
' 2. Collapse the bearing<1> component.
' 3. Widen the FeatureManager design tree.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. At each Stop statement, read the comments and press F5
'    to continue.
' 2. Examine the Immediate window.
'-------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim SelMgr As SldWorks.SelectionMgr
Dim swFeatMgr As SldWorks.FeatureManager
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    Set SelMgr = Part.SelectionManager
    Set swFeatMgr = Part.FeatureManager
```

```
    Debug.Print "Tree Display settings upon opening document"
    Debug.Print vbTab & "Show Component Names                      : " & swFeatMgr.ShowComponentNames
    Debug.Print vbTab & "Show Component Descriptions               : " & swFeatMgr.ShowComponentDescriptions
    Debug.Print vbTab & "Show Component Configuration Names        : " & swFeatMgr.ShowComponentConfigurationNames
    Debug.Print vbTab & "Show Component Configuration Descriptions : " & swFeatMgr.ShowComponentConfigurationDescriptions & vbCrLf
```

```
    Stop
    ' To verify the settings, right-click pillow_block at the
    ' the top of the FeatureManager design tree and point at Tree Display
    ' Compare the settings with the output in the Immediate window
    ' Then click anywhere in the graphics area to close the short-cut menu
```

```
    ' Examine the FeatureManager design tree to
    ' verify that the names of the components are not shown
```

```
    If (swFeatMgr.ShowComponentDescriptions) Then
        swFeatMgr.ShowComponentDescriptions = False
    Else
        swFeatMgr.ShowComponentDescriptions = True
    End If
```

```
    Stop
    ' Show Component Descriptions is set to true
```

```
    ' Examine the FeatureManager design tree, and
    ' verify that the descriptions of the components
    ' are shown
```

```
    If (swFeatMgr.ShowComponentConfigurationNames) Then
        swFeatMgr.ShowComponentConfigurationNames = False
    Else
        swFeatMgr.ShowComponentConfigurationNames = True
    End If
```

```
    Stop
    ' Show Component Configuration Names is set to false
```

```
    ' Examine the FeatureManager design tree, and
    ' verify that the names of the configurations are
    ' not shown
```

```
    If (swFeatMgr.ShowComponentConfigurationDescriptions) Then
        swFeatMgr.ShowComponentConfigurationDescriptions = False
    Else
        swFeatMgr.ShowComponentConfigurationDescriptions = True
    End If
```

```
    Stop
    ' Show Component Configuration Descriptions is set to true
```

```
    ' Examine the FeatureManager design tree, and
    ' verify that the descriptions of the configurations
    ' are shown
```

```
    Debug.Print "Display modified settings"
    Debug.Print vbTab & "Show Component Names                      : " & swFeatMgr.ShowComponentNames
    Debug.Print vbTab & "Show Component Descriptions               : " & swFeatMgr.ShowComponentDescriptions
    Debug.Print vbTab & "Show Component Configuration Names        : " & swFeatMgr.ShowComponentConfigurationNames
    Debug.Print vbTab & "Show Component Configuration Descriptions : " & swFeatMgr.ShowComponentConfigurationDescriptions & vbCrLf
```

```
    ' FeatureManager::ShowComponentNames and FeatureManager::ShowComponentDescriptions
    ' cannot both be set to false
    swFeatMgr.ShowComponentDescriptions = True
    If (swFeatMgr.ShowComponentNames) Then
        swFeatMgr.ShowComponentNames = False
    End If
```

```
    Debug.Print "Try to set FeatureManager::ShowComponentDescriptions to false while FetureManager::ShowComponentNames is false"
    Debug.Print vbTab & "Before call to Show Component Descriptions : " & swFeatMgr.ShowComponentDescriptions
    swFeatMgr.ShowComponentDescriptions = False  ' This call does not work because FeatureManager::ShowComponentNames display is set to false
    Debug.Print vbTab & "After call to Show Component Descriptions  : " & swFeatMgr.ShowComponentDescriptions & vbCrLf
```

```
    ' Restore original settings
    If (swFeatMgr.ShowComponentDescriptions) Then
        swFeatMgr.ShowComponentNames = True
        swFeatMgr.ShowComponentDescriptions = False
    Else
        swFeatMgr.ShowComponentNames = True
    End If
```

```
    If (swFeatMgr.ShowComponentConfigurationNames) Then
        swFeatMgr.ShowComponentConfigurationNames = False
    Else
        swFeatMgr.ShowComponentConfigurationNames = True
    End If
```

```
    If (swFeatMgr.ShowComponentConfigurationDescriptions) Then
        swFeatMgr.ShowComponentConfigurationDescriptions = False
    Else
        swFeatMgr.ShowComponentConfigurationDescriptions = True
    End If
```

```
    Debug.Print "Original settings restored"
    Debug.Print vbTab & "Show Component Names                      : " & swFeatMgr.ShowComponentNames
    Debug.Print vbTab & "Show Component Descriptions               : " & swFeatMgr.ShowComponentDescriptions
    Debug.Print vbTab & "Show Component Configuration Names        : " & swFeatMgr.ShowComponentConfigurationNames
    Debug.Print vbTab & "Show Component Configuration Descriptions : " & swFeatMgr.ShowComponentConfigurationDescriptions & vbCrLf
```

```
    Debug.Print "Macro done executing!"
```

```
End Sub
```
