---
title: "Create a SpeedPak Configuration Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_SpeedPak_Example_VBNET.htm"
---

# Create a SpeedPak Configuration Example (VB.NET)

This example shows how to create a SpeedPak configuration for the active configuration.

```
'--------------------------------------------------------------
' Preconditions: Open an assembly.
'
' Postconditions:
' 1. Adds active_configuration (Default_speedpak) to the
'    ConfigurationManager.
' 2. Click the ConfigurationManager tab and expand Default.
'-------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim boolstatus As Boolean
        Dim swConfigMgr As ConfigurationManager

        swModel = swApp.ActiveDoc
        swConfigMgr = swModel.ConfigurationManager

        ' Add a SpeedPak configuration with a part/body
        ' selection threshold of 0.5 to the active configuration
        swConfigMgr.AddSpeedPak2(1, 0.5)
        boolstatus = swModel.ForceRebuild3(False)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
