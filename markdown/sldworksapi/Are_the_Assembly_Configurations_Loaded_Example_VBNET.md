---
title: "Are the Assembly Configurations Loaded Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Are_the_Assembly_Configurations_Loaded_Example_VBNET.htm"
---

# Are the Assembly Configurations Loaded Example (VB.NET)

This example shows how to find out if the configurations in an assembly are loaded, whether the configurations need to be updated and rebuilt, and the configuration types.

```
'------------------------------------------------------------
' Preconditions:
' 1. Verify that the assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Loads all configurations.
' 2. Examine the Immediate window to see the states of the
'    configurations.
'
' NOTE: Because the assembly is used elsewhere, do not save
' changes.
'-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swConfiguration As Configuration
        Dim swConfigurationMgr As ConfigurationManager
        Dim ConfNameArr As Object
        Dim ConfName As Object
        Const DocFilename As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\pdmworks\speaker.sldasm"
        Dim boolstatus As Boolean
        Dim Errors As Long
        Dim Warnings As Long

        ' Open document; exit if it doesn't open
        swModel = swApp.OpenDoc6(DocFilename, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", Errors, Warnings)
        If swModel Is Nothing Then
            Exit Sub
        Else
            Debug.Print("File = " & swModel.GetPathName)
            Debug.Print("")
        End If

        swConfigurationMgr = swModel.ConfigurationManager
        swConfiguration = swConfigurationMgr.ActiveConfiguration
        ConfNameArr = swModel.GetConfigurationNames

        Debug.Print("Traverse assembly without activating other configurations...")
        For Each ConfName In ConfNameArr
            swConfiguration = swModel.GetConfigurationByName(ConfName)
            Debug.Print("  Name of the configuration: " & swConfiguration.Name)
            Debug.Print("    Is the configuration loaded? " & swConfiguration.IsLoaded)
            Debug.Print("    Does the configuration need to be updated? " & swConfiguration.IsDirty)
            Debug.Print("    Does the configuration need to be rebuilt? " & swConfiguration.NeedsRebuild)
            Debug.Print("    What is the configuration type? " & swConfiguration.Type)
        Next

        Debug.Print("")

        ' Traverse the assembly again, but this time activate all
        ' configurations, which loads them
        Debug.Print("Traverse assembly and activate all configurations...")
        For Each ConfName In ConfNameArr
            swConfiguration = swModel.GetConfigurationByName(ConfName)
            boolstatus = swModel.ShowConfiguration2(ConfName)
            swConfiguration = swConfigurationMgr.ActiveConfiguration
            Debug.Print("  Name of the configuration: " & swConfiguration.Name)
            Debug.Print("    Is the configuration loaded? " & swConfiguration.IsLoaded)
            Debug.Print("    Does the configuration need to be updated? " & swConfiguration.IsDirty)
            Debug.Print("    Does the configuration need to be rebuilt? " & swConfiguration.NeedsRebuild)
            Debug.Print("    What is the configuration type? " & swConfiguration.Type)

        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
