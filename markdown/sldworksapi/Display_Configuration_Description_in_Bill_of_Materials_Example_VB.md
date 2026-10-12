---
title: "Display Configuration Description in Bill of Materials Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Configuration_Description_in_Bill_of_Materials_Example_VB.htm"
---

# Display Configuration Description in Bill of Materials Example (VBA)

This example shows how to traverse an assembly and display the description of each configuration in the bill of materials.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\smartcomponents\pillow_block.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the configurations.
' 2. Gets the name of each configuration and its description.
' 3. Sets and gets whether to display the description of each configuration
'    in the bill of materials.
' 4. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim vConfigNameArr As Variant
    Dim vConfigName As Variant
    Dim swConfig As SldWorks.Configuration
    Dim swParentConfig As SldWorks.Configuration
    Dim swConfMgr As SldWorks.ConfigurationManager
    Dim vChildConfigArr As Variant
    Dim vChildConfig  As Variant
    Dim swChildConfig As SldWorks.Configuration
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConfMgr = swModel.ConfigurationManager
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print ""
    ' Traverse configurations; always at least one configuration exists
    vConfigNameArr = swModel.GetConfigurationNames
    For Each vConfigName In vConfigNameArr
        Set swConfig = swModel.GetConfigurationByName(vConfigName)
        Debug.Print "  Configuration name = " & swConfig.Name
        Debug.Print "    Description = " & swConfig.Description
        swConfig.UseDescriptionInBOM = True
        Debug.Print "    Display description in bill of materials? " & swConfig.UseDescriptionInBOM
```

```
        ' Process parent
        Set swParentConfig = swConfig.GetParent
        If Not swParentConfig Is Nothing Then
            Debug.Print "      Parent = " & swParentConfig.Name
        End If
```

```
        ' Process children
        vChildConfigArr = swConfig.GetChildren
        If Not IsEmpty(vChildConfigArr) Then
            For Each vChildConfig In vChildConfigArr
                Set swChildConfig = vChildConfig
                Debug.Print "      Child = " & swChildConfig.Name
            Next
        End If
        Debug.Print ""
    Next
```

```
End Sub
```
