---
title: "Get List of Configurations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_List_Of_Configurations_Example_VBNET.htm"
---

# Get List of Configurations Example (VB.NET)

This example shows how to get a list of configuration names for the active document.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Gets the name of the file, name of the active configuration,
'    and the names of all configurations.
' 3. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim configNames() As String
        Dim configName As String
        Dim swConfig As Configuration
        Dim i As Integer
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\pillow_block.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Get and print active model path and name
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("")
        'Get and print name of active configuration
        swConfig = swModel.GetActiveConfiguration
        Debug.Print("  Name of active configuration = " & swConfig.Name)
        Debug.Print("")

        'Get and print names of all configurations
        configNames = swModel.GetConfigurationNames
        For i = 0 To UBound(configNames)
            configName = configNames(i)
            swConfig = swModel.GetConfigurationByName(configName)
            Debug.Print("  Name of configuration(" & i & ") = " & configName)
            Debug.Print("    Use alternate name in BOM  = " & swConfig.UseAlternateNameInBOM)
            Debug.Print("    Alternate name             = " + swConfig.AlternateName)
            Debug.Print("    Comment                    = " + swConfig.Comment)
            Debug.Print("")
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
