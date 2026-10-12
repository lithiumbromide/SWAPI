---
title: "Add Configuration and Promote Child Components in BOM Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Configuration_and_Promote_Child_Components_in_BOM_Example_VBNET.htm"
---

# Add Configuration and Promote Child Components in BOM Example (VB.NET)

This example shows how to add a configuration to an assembly and promote its child components one level in a BOM.

```
'----------------------------------------
' Preconditions:
' 1. Specified assembly document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Adds a new configuration named Config2.
' 3. Sets the option to dissolve the assembly's
'    configuration when it appears in a BOM and
'    promote all of its child components one level.
' 4. To verify, examine the option value printed to
'    the Immediate window.
'
' NOTE: Because this assembly document is used
' elsewhere, do not save changes when closing it.
'----------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swAssembly As AssemblyDoc
    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swConfig As Configuration
    Dim fileName As String
    Dim status As Boolean
    Dim errors As Integer
    Dim warnings As Integer

    Sub main()

        'Open assembly document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bowl and chute.sldasm"
        swAssembly = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModel = swAssembly

        'Add configuration named Config2
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("bowl and chute.SLDASM", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swConfig = swModel.AddConfiguration3("Config2", "", "", swConfigurationOptions2_e.swConfigOption_DoDisolveInBOM + swConfigurationOptions2_e.swConfigOption_DontShowPartsInBOM)

        'Dissolve the assembly's configuration
        'when it appears in a BOM and promote all of
        'its child components one level
        swConfig.ChildComponentDisplayInBOM = swChildComponentInBOMOption_e.swChildComponent_Promote
        Debug.Print("Child component display option in BOM: " & swConfig.ChildComponentDisplayInBOM)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
