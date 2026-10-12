---
title: "Get Display State Names and Visibilities of Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_Names_and_Visibilites_of_Components_Example_VBNET.htm"
---

# Get Display State Names and Visibilities of Components Example (VB.NET)

This example shows how to get the names of the display states in an assembly and the visibilities of the assembly components in each display state.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly that contains multiple components
'    and display states.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swConfigMgr As ConfigurationManager
        Dim swConfig As Configuration
        Dim components As Object = Nothing
        Dim docType As Integer
        Dim i As Integer
        Dim j As Integer
        Dim displayStateNames As Object
        Dim displayStateName As String
        Dim displayStateVisibilities As Object
        Dim displayStateVisibility As Integer
        Dim visibility As String = ""

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        docType = swModel.GetType
        If docType = swDocumentTypes_e.swDocASSEMBLY Then
            swConfigMgr = swModel.ConfigurationManager
            swConfig = swConfigMgr.ActiveConfiguration
            displayStateNames = swConfig.GetDisplayStates
            For i = 0 To UBound(displayStateNames)
                displayStateName = displayStateNames(i)
                Debug.Print("Display state name: " & displayStateName)
                displayStateVisibilities = swConfig.GetDisplayStateComponentVisibility(displayStateName, False, False, components)
                Debug.Print("  Display state visibility: ")
                For j = 0 To UBound(displayStateVisibilities)
                    displayStateVisibility = displayStateVisibilities(j)
                    Select Case displayStateVisibility
                        Case 0
                            visibility = "Hidden"
                        Case 1
                            visibility = "Shown"
                    End Select
                    Debug.Print("    " & components(j).Name2 & ": " & visibility)
                Next j
            Next i
        Else
            Debug.Print("Open an assembly document with multiple display states.")
            Exit Sub
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
