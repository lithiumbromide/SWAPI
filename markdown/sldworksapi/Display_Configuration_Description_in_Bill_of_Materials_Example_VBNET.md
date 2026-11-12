---
title: "Display Configuration Description in Bill of Materials Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Configuration_Description_in_Bill_of_Materials_Example_VBNET.htm"
---

# Display Configuration Description in Bill of Materials Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim vConfigNameArr() As Object
        Dim vConfigName As Object
        Dim swConfig As Configuration
        Dim swParentConfig As Configuration
        Dim swConfMgr As ConfigurationManager
        Dim vChildConfigArr() As Object
        Dim vChildConfig As Object
        Dim swChildConfig As Configuration

        swModel = swApp.ActiveDoc
        swConfMgr = swModel.ConfigurationManager
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("")
        ' Traverse configurations; always at least one configuration exists
        vConfigNameArr = swModel.GetConfigurationNames
        For Each vConfigName In vConfigNameArr
            swConfig = swModel.GetConfigurationByName(vConfigName)
            Debug.Print("  Configuration name = " & swConfig.Name)
            Debug.Print("    Description = " & swConfig.Description)
            swConfig.UseDescriptionInBOM = True
            Debug.Print("    Display description in bill of materials? " & swConfig.UseDescriptionInBOM)
            ' Process parent
            swParentConfig = swConfig.GetParent
            If Not swParentConfig Is Nothing Then
                Debug.Print("      Parent = " & swParentConfig.Name)
            End If
            ' Process children
            vChildConfigArr = swConfig.GetChildren
            If Not IsNothing(vChildConfigArr) Then
                For Each vChildConfig In vChildConfigArr
                    swChildConfig = vChildConfig
                    Debug.Print("      Child = " & swChildConfig.Name)
                Next
            End If
            Debug.Print("")
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
