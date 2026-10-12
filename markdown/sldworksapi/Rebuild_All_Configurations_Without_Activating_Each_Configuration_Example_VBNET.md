---
title: "Rebuild All Configurations Without Activating Each Configuration Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rebuild_All_Configurations_Without_Activating_Each_Configuration_Example_VBNET.htm"
---

# Rebuild All Configurations Without Activating Each Configuration Example (VB.NET)

This example shows how to rebuild only those features that need to be rebuilt in all configurations without activating each configuration.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm.
' 2. Right-click membrane<1> and click Suppress in the active
'    configuration, Dual Speaker.
' 3. Click Don't Save.
' 4. Click the ConfigurationManager tab and right-click Single
'    Speaker Glueable and click Show Configuration to make this
'    configuration the active configuration.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Gets whether each configuration needs to be rebuilt.
' 2. Rebuilds only those features that need to be rebuilt in all
'    configurations without activating each configuration.
' 3. Gets whether each configuration needs to be rebuilt.
' 4. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swConfiguration As Configuration
    Dim vConfNameArr As Object
    Dim vConfName As Object

    Public Sub main()

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        'Get whether each configuration needs to be rebuilt
        Debug.Print("Traverse assembly without activating other configurations...")
        TraverseConfigurations(swModel)

        'Rebuild only those features that need to be rebuilt in all configurations
        'without activating each configuration
        swModelDocExt.EditRebuildAll()

        'Get whether each configuration needs to be rebuilt
        Debug.Print("Traverse assembly without activating other configurations...")
        TraverseConfigurations(swModel)

    End Sub

    Sub TraverseConfigurations(ByVal swModel As ModelDoc2)
        vConfNameArr = swModel.GetConfigurationNames
        For Each vConfName In vConfNameArr
            swConfiguration = swModel.GetConfigurationByName(vConfName)
            Debug.Print("  Name of the configuration: " & swConfiguration.Name)
            Debug.Print("    Does the configuration need to be rebuilt? " & swConfiguration.NeedsRebuild)
        Next
        Debug.Print("")
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
