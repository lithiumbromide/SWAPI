---
title: "Get Whether Components Are Loaded Example(VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Components_Are_Loaded_Example_VBNET.htm"
---

# Get Whether Components Are Loaded Example(VB.NET)

## Get Whether Components Are Loaded Example (VB.NET)

This example gets whether the components in an assembly document are loaded.

```vb
'----------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified assembly document exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Loads the Magnet-1 component.
 ' 2. Examine the Immediate window.
' NOTE: Because this assembly document is used elsewhere,
 ' do not save changes.
 '-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDocSpecification As DocumentSpecification
        Dim sComponents(0) As String
        Dim Components As Object
        Dim swComponent As Component2
        Dim sName As String
        Dim swAssembly As AssemblyDoc
        Dim longstatus As Integer
        Dim longwarnings As Integer
        Dim i As Integer
        Dim swConfigMgr As ConfigurationManager
        Dim swConfig As Configuration

        ' Selectively open speaker.sldasm assembly
        ' Load only the Magnet-1 component
        swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\pdmworks\speaker.sldasm")
        sComponents(0) = "Magnet-1@speaker"
        Components = sComponents
        swDocSpecification.ComponentList = Components
        swDocSpecification.Selective = True
        sName = swDocSpecification.FileName
        swDocSpecification.DocumentType = swDocumentTypes_e.swDocASSEMBLY
        swDocSpecification.DisplayState = "Default_Display State-1"
        swDocSpecification.UseLightWeightDefault = True
        swDocSpecification.LightWeight = True
        swDocSpecification.Silent = True
        swDocSpecification.IgnoreHiddenComponents = True
        swModel = swApp.OpenDoc7(swDocSpecification)
        longstatus = swDocSpecification.Error
        longwarnings = swDocSpecification.Warning

        ' Get whether the components in the
        ' assembly document are loaded and suppressed; only
        ' Magnet-1 should be loaded and not suppressed
        swAssembly = swModel
        swConfigMgr = swModel.ConfigurationManager
        swConfig = swConfigMgr.ActiveConfiguration
        Components = swAssembly.GetComponents(True)
        For i = 0 To UBound(Components)
            swComponent = Components(i)
            If (swComponent.IsLoaded) Then
                Debug.Print("Component: " & swComponent.Name & " is loaded.")
            Else
                Debug.Print("Component: " & swComponent.Name & " is not loaded.")
            End If

            Debug.Print("  Suppressed: " & swConfig.GetComponentSuppressionState(swComponent.Name))
            Debug.Print("")

        Next
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks
End Class
```
