---
title: "Remove Material Properties From Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Material_From_Bodies_Example_VB.htm"
---

# Remove Material Properties From Bodies Example (VBA)

## Remove Material Properties from Bodies Example (VBA)

This example shows how to remove materials from bodies in a multibody part. This example also works with a part with a single body and an assembly with single and multibody components.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\multibody\multi_inter.sldprt.
' 2. Expand Solid Bodies(2) > right-click Extrude-Thin1 > click
'    Appearances > Body > any color in Appearances(color) > OK.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the FeatureManager design tree.
' 2. Removes the color that you applied to Extrude-Thin1.
' 3. Examine the Immediate window and graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Option Explicit
```

```
Dim bRet As Boolean
```

```
Sub ProcessComponent(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swComp As SldWorks.Component2)
    Dim vChildComp As Variant
    Dim swChildComp As SldWorks.Component2
    Dim vBody As Variant
    Dim childComp As Variant
```

```
    Debug.Print swComp.Name2 & " <" & swComp.ReferencedConfiguration & ">"
```

```
    ' Solid bodies
    Dim vBodyArr As Variant
    Dim swBody As Body2
    vBodyArr = swComp.GetBodies2(swSolidBody)
    If Not IsEmpty(vBodyArr) Then
        Debug.Print "  Number of bodies: " & UBound(vBodyArr) + 1
        For Each vBody In vBodyArr
            Set swBody = vBody
            Dim vConfigName As Variant
            Debug.Print "    Body name: " & swBody.Name
            vConfigName = swModel.GetConfigurationNames
            bRet = swBody.RemoveMaterialProperty(swThisConfiguration, (vConfigName))
            Debug.Print "      Material removed from body? " & bRet
        Next
    End If
```

```
    vChildComp = swComp.GetChildren
    For Each childComp In vChildComp
        Set swChildComp = childComp
        ProcessComponent swApp, swModel, swChildComp
    Next
```

```
End Sub
```

```
Sub ProcessAssembly(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2)
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConf As SldWorks.Configuration
    Dim swRootComp As SldWorks.Component2
```

```
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConf = swConfigMgr.ActiveConfiguration
    Set swRootComp = swConf.GetRootComponent3(True)
    ProcessComponent swApp, swModel, swRootComp
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
    Dim swPart As SldWorks.PartDoc
    Dim vBody As Variant
    Dim j As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    swModel.ClearSelection2 True
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    Select Case swModel.GetType
        Case swDocPART
            Set swPart = swModel
            ' Solid bodies
            Dim vBodyArr As Variant
            Dim swBody As Body2
            vBodyArr = swPart.GetBodies2(swSolidBody, True)
```

```
            If Not IsEmpty(vBodyArr) Then
                Debug.Print "  Number of bodies: " & UBound(vBodyArr) + 1
                Debug.Print "    Material removed from: "
                j = 1
                For Each vBody In vBodyArr
                    Set swBody = vBody
                    Dim vConfigName As Variant
                    vConfigName = swModel.GetConfigurationNames
                    bRet = swBody.RemoveMaterialProperty(swAllConfiguration, (vConfigName))
                    Debug.Print "      Body " & j & "? " & bRet
                    j = j + 1
                Next
            End If
        Case swDocASSEMBLY
            ProcessAssembly swApp, swModel
        Case Else
            Exit Sub
    End Select
```

```
End Sub
```
