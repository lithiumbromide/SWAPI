---
title: "Insert Cosmetic Weld Bead Using Geometric Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VBNET.htm"
---

# Insert Cosmetic Weld Bead Using Geometric Entities Example (VB.NET)

This example shows how to insert a cosmetic weld bead using geometric entities.

```
'----------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a cosmetic weld bead using the
'    selected geometric entities (i.e., faces).
' 2. To verify, examine the graphics area and
'    expand the Weld Folder and its subfolder
'    in the FeatureManager design tree.
' 3. Examine the Immediate window.
'
' NOTE: Because the part document is used elsewhere,
' do not save any changes to it.
'-----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeature As Feature
        Dim swSelMgr As SelectionMgr
        Dim swFeatureMgr As FeatureManager
        Dim swCosmeticWeldBeadFeatureData As CosmeticWeldBeadFeatureData
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim entityType As Integer

        'Open model document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\driveworksxpress\leg.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Select the faces
        swModelDocExt = swModel.Extension
        'From face
        status = swModelDocExt.SelectByID2("", "FACE", 0.447611268878973, 0.185506718400291, 0.00676112086262037, True, 4, Nothing, 0)
        'To face
        status = swModelDocExt.SelectByID2("", "FACE", 0.567647499089958, 0.0888999999998532, 0.00208831790428121, True, 8, Nothing, 0)

        swSelMgr = swModel.SelectionManager
        Dim weldFromFace(0) As Face2
        Dim weldFromArray(0) As Object
        weldFromFace(0) = swSelMgr.GetSelectedObject6(1, 4)
        weldFromArray = weldFromFace

        Dim weldToFace(0) As Face2
        Dim weldToArray(0) As Object
        weldToFace(0) = swSelMgr.GetSelectedObject6(1, 8)
        weldToArray = weldToFace

        'Create cosmetic weld bead using the selected faces
        Dim weldObjs(1) As Object
        swFeatureMgr = swModel.FeatureManager
        weldObjs = swFeatureMgr.InsertCosmeticWeldBead2(0, weldFromArray, weldToArray, 15 / 1000)

        'Get the weld-from and weld-to entities and their types
        status = swModelDocExt.SelectByID2("Weld Bead1", "COSMETIC_WELD", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelMgr.GetSelectedObject6(1, -1)
        swCosmeticWeldBeadFeatureData = swFeature.GetDefinition
        swCosmeticWeldBeadFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print(swFeature.Name)
        weldObjs = swCosmeticWeldBeadFeatureData.GetEntitiesWeldFrom(entityType)
        Debug.Print("  Weld-from type: " & entityType)
        weldObjs = swCosmeticWeldBeadFeatureData.GetEntitiesWeldTo(entityType)
        Debug.Print("  Weld-to type:   " & entityType)
        swCosmeticWeldBeadFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
