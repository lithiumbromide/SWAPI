---
title: "Add Spotlight and Get Light Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Spotlight_and_Get_Light_Feature_Example_VBNET.htm"
---

# Add Spotlight and Get Light Feature Example (VB.NET)

This example shows how to add a spotlight to a model and get its light feature.

```
'-------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Adds a spotlight.
' 3. Gets the spotlight's feature and prints its ID to
'    the Immediate window.
' 4. Examine the Immediate window, FeatureManager design tree, and
'    graphics area.
'
' NOTE: Because this assembly document is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swModelView As ModelView
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swLight As Light
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim rect() As Integer

        'Open assembly
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\appearances\usb_flash_drive1.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Add spotlight
        status = swModel.AddLightSource("SW#5", 2, "Spot1")
        status = swModel.SetLightSourcePropertyValuesVB("SW#5", 2, 0.5, 8454143, 1, -0.0999999999999991, 0.170000000000101, 1.10999999999999, 0.179999999999999, -0.0900000000001008, -1.02999999999999, 45, 0, 0, 0, 0.4, 0.4, 0, False)
        status = swModel.LockLightToModel(4, True)
        swModelView = swModel.ActiveView
        swModelView.GraphicsRedraw(rect)

        'Get spotlight's feature ID
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Spot1", "LIGHTS", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swLight = swFeature.GetSpecificFeature2
        Debug.Print("Light ID: " & swLight.GetID)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
