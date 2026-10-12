---
title: "Move Rollback Bar Using Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Rollback_Bar_Using_Feature_Example_VBNET.htm"
---

# Move Rollback Bar Using Feature Example (VB.NET)

This example shows how to move the rollback bar above and below a selected feature in a part document.

```
'-----------------------------------------------------
' Preconditions: Verify that the part to open exists.
' 2. Run the macro.
'
' Postconditions:
' 1. Opens the part document.
' 2. Selects the Sweep1 feature.
' 3. Moves the rollback bar to feature above the
'    Sweep1 feature; i.e., the Revolve1 feature.
' 4. Examine the graphics area to verify, then press
'    F5
' 5. Moves the rollback bar to below the Sweep1 feature.
'-------------------------------------------------------
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.sldworks
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swPart As PartDoc
        Dim swFeatureMgr As FeatureManager
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer, warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swPart = swModel
        swModelDocExt = swModel.Extension
        ' Move rollback bar to above Sweep1
        status = swModelDocExt.SelectByID2("Sweep1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swPart.EditRollback()
        Stop
        'Examine graphics area, then press F5
        ' Move rollback bar to below Sweep1
        swFeatureMgr = swModel.FeatureManager
        status = swFeatureMgr.EditRollback(swMoveRollbackBarTo_e.swMoveRollbackBarToBeforeFeature, "")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
