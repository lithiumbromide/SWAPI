---
title: "Rename Components and Save Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rename_Components_and_Save_Assembly_Example_VBNET.htm"
---

# Rename Components and Save Assembly Example (VB.NET)

This example shows how to rename components in an assembly and returns an error when attempting to save the assembly without first saving its references.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly.
' 2. Selects a component.
' 3. Renames the selected component and the other component with the
'    the same name.
' 4. Attempts to save the assembly.
' 5. Gets whether the assembly has renamed components.
' 6. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim errorsRename As Integer
        Dim errorsSave As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam_boltconnection.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        status = swModelDocExt.SelectByID2("beam with holes-2@beam_boltconnection", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        errorsRename = swModelDocExt.RenameDocument("Renamed_beam_with_holes")
        Debug.Print("Rename document errors: " & errorsRename)
        status = swModel.Save3(swSaveAsOptions_e.swSaveAsOptions_Silent, errorsSave, warnings)
        If status = False Then
            Debug.Print("Save errors (8192 = Saving an assembly with renamed components requires saving the references): " & errorsSave)
        End If
        status = swModelDocExt.HasRenamedDocuments
        Debug.Print("Assembly document has renamed components: " & status)

        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
