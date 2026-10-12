---
title: "Remove Textures from Assembly Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Textures_from_Assembly_Components_Example_VB.htm"
---

# Remove Textures from Assembly Components Example (VBA)

This example shows how to remove all textures from all components in an assembly.

```
'-------------------------------------------------
' Preconditions:
' 1. Open an assembly with one or more components
'    with textures applied to them at the component (part)
'    level.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Removes all textures applied to all components.
' 2. Examine the Immediate window.
' 3. Click the graphics area and examine the assembly.
'--------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean
```

```
Function RemoveTexture(swDoc As SldWorks.ModelDoc2, configName As String) As Boolean
```

```
    Dim swDocExt As SldWorks.ModelDocExtension
    Dim swTexture As SldWorks.Texture
```

```
    Set swDocExt = swDoc.Extension
    Set swTexture = swDocExt.GetTexture(configName)
    If Not swTexture Is Nothing Then
        Debug.Print "   Texture removed: " & swTexture.MaterialName
        RemoveTexture = swDocExt.RemoveTexture2(configName)
        swDoc.SetSaveFlag
    End If
```

```
End Function
```

```
Function TraverseComponents(parentComp As SldWorks.Component2)
```

```
    Dim vChildComponents As Variant
    Dim vObj As Variant
    Dim childComp As SldWorks.Component2
    Dim childDoc As SldWorks.ModelDoc2
    Dim childConfigName As String
```

```
    vChildComponents = parentComp.GetChildren
    For Each vObj In vChildComponents
        Set childComp = vObj
        Set childDoc = childComp.GetModelDoc
        childConfigName = childComp.ReferencedConfiguration
        Debug.Print "Component name: " & childComp.Name2
        Debug.Print "  Configuration name: " & childConfigName
        boolstatus = RemoveTexture(childDoc, childConfigName)
        Call TraverseComponents(childComp)
    Next vObj
```

```
End Function
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    Dim rootDoc As SldWorks.ModelDoc2
    Dim rootConfig As SldWorks.Configuration
    Dim rootComp As SldWorks.Component2
    Dim configMgr As SldWorks.ConfigurationManager
```

```
    Set rootDoc = swApp.ActiveDoc
    Set configMgr = Part.ConfigurationManager
    Set rootConfig = configMgr.ActiveConfiguration
    Set rootComp = rootConfig.GetRootComponent3(True)
```

```
    Call TraverseComponents(rootComp)
```

```
End Sub
```
