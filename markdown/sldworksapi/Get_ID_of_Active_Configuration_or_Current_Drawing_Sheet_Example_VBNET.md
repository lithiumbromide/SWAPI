---
title: "Get ID of Active Configuration or Current Drawing Sheet Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VBNET.htm"
---

# Get ID of Active Configuration or Current Drawing Sheet Example (VB.NET)

This example shows how to get the name and ID of the active configuration of a part or assembly or the current sheet of a drawing.

**NOTE**: A unique ID is assigned to each configuration and drawing. This ID does not change when the name of the configuration or drawing sheet is changed.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Changes either the active configuration's name or
'    the current sheet's name to Test. However, the
'    document's ID is unchanged.
' 2. Examine the Immediate window.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swConfig As Configuration
        Dim swDrawingDoc As DrawingDoc
        Dim swSheet As Sheet
        Dim nDocType As Integer

        swModel = swApp.ActiveDoc

        ' Get type of model document
        If swModel.GetType = 1 Then
            nDocType = swDocumentTypes_e.swDocPART
        ElseIf swModel.GetType = 2 Then
            nDocType = swDocumentTypes_e.swDocASSEMBLY
        ElseIf swModel.GetType = 3 Then
            nDocType = swDocumentTypes_e.swDocDRAWING
        Else
            ' Not a SOLIDWORKS Design model document,
            ' so exit macro
            Exit Sub
        End If

        ' If a part or assembly document,
        ' then get the name of it and its ID
        If nDocType <> swDocumentTypes_e.swDocDRAWING Then
            swConfig = swModel.GetActiveConfiguration
            If Not swConfig Is Nothing Then
                Debug.Print("Active configuration's name = " & swConfig.Name & ", ID = " & swConfig.GetID)
                ' Change the active configuration's name
                swConfig.Name = "Test"
                ' Test to see if the ID remains the same
                ' after changing the name of the configuration
                Debug.Print("Active configuration's new name = " & swConfig.Name & ", ID = " & swConfig.GetID)
            End If
            Exit Sub
        End If

        ' A drawing sheet must be active,
        ' so get its name and ID
        swDrawingDoc = swModel
        swSheet = swDrawingDoc.GetCurrentSheet
        If Not swSheet Is Nothing Then
            Debug.Print("Current sheet's name = " & swSheet.GetName & ", ID = " & swSheet.GetID)
            ' Change current sheet's name
            swSheet.SetName("Test")
            ' Test to see if the ID remains the same
            ' after changing the name of the sheet
            Debug.Print("Current sheet's new name = " & swSheet.GetName & ", ID = " & swSheet.GetID)
        End If

    End Sub

    ''' <summary>

    ''' The SldWorks swApp variable is pre-assigned for you.

    ''' </summary>

    Public swApp As SldWorks

End Class
```
