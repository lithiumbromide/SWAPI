---
title: "Modify Break Corner Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Break_Corner_Feature_Example_VBNET.htm"
---

# Modify Break Corner Feature Example (VB.NET)

This example shows how to create and modify a break corner feature in a sheet metal part.

```
'---------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified document.
' 2. Selects a face on Edge-Flange1.
' 3. Creates a break corner feature.
' 4. Unsuppresses the flat pattern feature.
' 5. Accesses the break corner feature and
'    and modifies it.
' 6. Suppresses the flat pattern feature.
' 7. Examine the graphics area and the Immediate window.
'
' NOTE: Because the part document is used elsewhere,
' do not save any changes.
'----------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swBreakCornerFeatureData As BreakCornerFeatureData
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\sm1-remove-edges.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", -0.111589911985732, 0.0979999999999563, 0.0841212722518208, True, 0, Nothing, 0)
        swModel.InsertSheetMetalBreakCorner(swBreakCornerTypes_e.swBreakCornerTypeChamfer, 0.005)

        'Select and unsuppress the flat pattern feature
        status = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditUnsuppress2()
        swModel.ClearSelection2(True)

        'Select the break corner feature
        'and change some of its properties
        status = swModelDocExt.SelectByID2("Break-Corner1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, 0)
        swBreakCornerFeatureData = swFeature.GetDefinition
        status = swBreakCornerFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("AccessSelections: " & status)
        Debug.Print("")
        Debug.Print("  -------------Original--------------")
        Debug.Print("    CenteredOnBendLines: " & swBreakCornerFeatureData.CenteredOnBendLines)
        Debug.Print("    InternalCornersOnly: " & swBreakCornerFeatureData.InternalCornersOnly)
        swBreakCornerFeatureData.InternalCornersOnly = True
        swBreakCornerFeatureData.CenteredOnBendLines = True
        Debug.Print("")
        Debug.Print("  -------------Modified--------------")
        Debug.Print("    CenteredOnBendLines: " & swBreakCornerFeatureData.CenteredOnBendLines)
        Debug.Print("    InternalCornersOnly: " & swBreakCornerFeatureData.InternalCornersOnly)
        status = swFeature.ModifyDefinition(swBreakCornerFeatureData, swModel, Nothing)
        Debug.Print("")
        Debug.Print("ModifyDefinition: " & status)
        swModel.ClearSelection2(True)

        'Select and suppress the flat pattern feature
        status = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditSuppress2()
        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
