---
title: "Get Exploded Views for Configuration Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Exploded_Views_for_Configuration_Example_VBNET.htm"
---

# Get Exploded Views for Configuration Example (VB.NET)

This example shows how to get:

- number of exploded views for a configuration.
- name of each exploded view for a configuration.
- name of the configuration for each exploded view.
- name of the exploded view shown in the model.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of the active configuration.
' 2. Creates five exploded views for the active configuration.
' 3. Gets the number of exploded views for the active configuration.
' 4. Gets the name of:
'    * each exploded view for the active configuration
'    * configuration for each exploded view
'    and shows each exploded view.
' 5. Gets the name of the exploded view shown in the model.
' 6. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swAssembly As AssemblyDoc
        Dim swConfigMgr As ConfigurationManager
        Dim swConfig As Configuration
        Dim activeConfigName As String
        Dim viewNames() As String
        Dim viewName As String
        Dim i As Integer

        swModel = swApp.ActiveDoc
        swAssembly = swModel

        'Get active configuration name
        swConfigMgr = swModel.ConfigurationManager
        swConfig = swConfigMgr.ActiveConfiguration
        activeConfigName = swConfig.Name

        Debug.Print("Active configuration name: " & activeConfigName)

        'Create five exploded views in the active configuration
        For i = 0 To 4
            swAssembly.CreateExplodedView()
        Next i

        'Get the number of exploded views in the active configuration name
        Debug.Print("  Number of exploded views created: " & swAssembly.GetExplodedViewCount2(activeConfigName))

        'Get the name of each exploded view in the active configuration,
        'get the name of the configuration for each exploded view, and
        'show each exploded view
        viewNames = swAssembly.GetExplodedViewNames2(activeConfigName)

        For i = 0 To UBound(viewNames)
            viewName = viewNames(i)
            Debug.Print("    Exploded view name: " & viewName)
            Debug.Print("      Name of configuration for exploded view: " & swAssembly.GetExplodedViewConfigurationName(viewName))
            swAssembly.ShowExploded2(True, viewName)
        Next i
```

```
        'Get the name of exploded view shown in model
        viewName = ""
        swModelDocExt = swModel.Extension
        swModelDocExt.IsExploded(viewName)
        Debug.Print("Name of exploded view shown in model: " & viewName)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
