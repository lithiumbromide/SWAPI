---
title: "Get Display State Names and Visibilities of Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_Names_and_Visibilites_of_Components_Example_VB.htm"
---

# Get Display State Names and Visibilities of Components Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swConfigMgr As SldWorks.ConfigurationManager
Dim swConfig As SldWorks.Configuration
Dim components As Variant
Dim docType As Long
Dim i As Long
Dim j As Long
Dim displayStateNames As Variant
Dim displayStateName As String
Dim displayStateVisibilities As Variant
Dim visibility As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    docType = swModel.GetType
    If docType = swDocumentTypes_e.swDocASSEMBLY Then
```

```
        Set swConfigMgr = swModel.ConfigurationManager
        Set swConfig = swConfigMgr.ActiveConfiguration
        displayStateNames = swConfig.GetDisplayStates
        For i = 0 To UBound(displayStateNames)
            displayStateName = displayStateNames(i)
            Debug.Print "Display state name: " & displayStateName
            displayStateVisibilities = swConfig.GetDisplayStateComponentVisibility(displayStateName, False, False, components)
            Debug.Print ("  Display state visibility: ")
            For j = 0 To UBound(displayStateVisibilities)
                Select Case displayStateVisibilities(j)
                    Case 0
                        visibility = "Hidden"
                    Case 1
                        visibility = "Shown"
                End Select
                Debug.Print ("    " & components(j).Name2 & ": " & visibility)
            Next j
        Next i
    Else
        Debug.Print "Open an assembly document with multiple display states."
        Exit Sub
    End If
```

```
End Sub
```
