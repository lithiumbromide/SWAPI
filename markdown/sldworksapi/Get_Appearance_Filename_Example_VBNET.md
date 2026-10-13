---
title: "Get Appearance File Name Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Appearance_Filename_Example_VBNET.htm"
---

# Get Appearance File Name Example (VB.NET)

This example shows how to get the file name of the first appearance applied to a model.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified model document exists.
' 2. Verify that the specified materials file exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified model document.
' 2. Applies the specified appearance to the selected face.
' 3. Gets the material IDs.
' 4. Gets the file name of the first appearance applied to the model.
' 5. Examine the graphics area and the Immediate window.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFace As Face2
        Dim swConfiguration As Configuration
        Dim swRenderMaterial As RenderMaterial
        Dim nbrRenderMaterials As Integer
        Dim fileName As String
        Dim warnings As Integer
        Dim errors As Integer
        Dim status As Boolean
        Dim materialName As String
        Dim displayStateNames() As String
        Dim materialID1 As Integer
        Dim materialID2 As Integer

        'Open model document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cover_plate.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Create material for the appearance
        materialName = "C:\Program Files\SolidWorks Corp\SolidWorks\data\graphics\Materials\plastic\low gloss\blue low gloss plastic.p2m"
        swModelDocExt = swModel.Extension
        swRenderMaterial = swModelDocExt.CreateRenderMaterial(materialName)

        'Verify that RealView Graphics is set
        Debug.Print("RealView Graphics set? " & swModelDocExt.ViewDisplayRealView)

        'Select a face and add an appearance
        status = swModelDocExt.SelectByID2("", "FACE", 0.0417924256550464, 0.0796803314056547, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFace = swSelectionMgr.GetSelectedObject6(1, -1)
        status = swRenderMaterial.AddEntity(swFace)
        Debug.Print("Appearance added to selected face? " & status)

        swModel.ClearSelection2(True)

        'Get the names of display states
        'Add the appearance to all display states
        swConfiguration = swModel.GetActiveConfiguration
        displayStateNames = swConfiguration.GetDisplayStates
        status = swModelDocExt.AddDisplayStateSpecificRenderMaterial(swRenderMaterial, swDisplayStateOpts_e.swAllDisplayState, displayStateNames, materialID1, materialID2)
        Debug.Print("Material IDs returned by IModelDocExtension::AddDisplayStateSpecificRenderMaterial: ")
        Debug.Print("  ID1: " & materialID1)
        Debug.Print("  ID2: " & materialID2)

        'Get the number of appearances
        nbrRenderMaterials = swModelDocExt.GetRenderMaterialsCount2(swDisplayStateOpts_e.swAllDisplayState, displayStateNames)

        'If one or more appearances are applied to the model,
        'then get the file name of the first appearance applied
        If nbrRenderMaterials > 0 Then
            swRenderMaterial.GetMaterialIds(materialID1, materialID2)
            Debug.Print("Material IDs returned by IModelDocExtension::GetMaterialIds: ")
            Debug.Print("  ID1: " & materialID1)
            Debug.Print("  ID2: " & materialID2)
            Debug.Print("First appearance's file name: " & swRenderMaterial.FileName)
        Else
            Debug.Print("No appearances applied to this model.")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
