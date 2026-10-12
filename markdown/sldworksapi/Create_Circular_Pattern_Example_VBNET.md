---
title: "Create Circular Pattern Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Circular_Pattern_Example_VBNET.htm"
---

# Create Circular Pattern Example (VB.NET)

This example shows how to create a circular-pattern feature using selected direction axis, pattern seed features, and variable spacing between pattern instances.

'----------------------------------------------------------------------------
' Preconditions: Open `public_documents`\samples\tutorial\api\varyinstance.sldprt
'
' Postconditions: Creates a circular-pattern feature.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'-----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

Public Sub Main()

Dim swModel As ModelDoc2
Dim swModelDocExt As ModelDocExtension
Dim swFeatureMgr As FeatureManager
Dim boolstatus As Boolean
Dim status As Integer

```
        swModel = swApp.ActivateDoc3("varyInstance.sldprt", False, swRebuildOnActivation_e.swUserDecision, status)
        swModelDocExt = swModel.Extension

        boolstatus = swModelDocExt.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0.00843730075439453, 0.00364341890551145, -0.0354416044676498, False, 4, Nothing, 0)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to select a seed feature") : GoTo LastLine

        boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.00628473027779819, -0.168045059787516, -0.0496550391792034, True, 1, Nothing, 0)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to select an edge for direction 1") : GoTo LastLine

        boolstatus = swModelDocExt.SelectByID2("Fillet1", "BODYFEATURE", 0.000782948437176856, 0.00455320522434022, -0.0350770617062892, True, 4, Nothing, 0)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to select a seed feature") : GoTo LastLine

        swFeatureMgr = swModel.FeatureManager

        boolstatus = swFeatureMgr.InsertVaryInstanceIncrement("D1@Sketch2@varyInstance.SLDPRT", 4, 1, 0, 0.003)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to add an increment value to dimension D1@Sketch2@varyInstance.SLDPRT") : GoTo LastLine

        boolstatus = swFeatureMgr.InsertVaryInstanceIncrement("D1@Cut-Extrude1@varyInstance.SLDPRT", 4, 1, 0, -0.001)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to add an increment value to dimension D1@Cut-Extrude1@varyInstance.SLDPRT") : GoTo LastLine

        boolstatus = swFeatureMgr.InsertVaryInstanceIncrement("D1@Fillet1@varyInstance.SLDPRT", 4, 1, 0, 0.0001)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to add an increment value to dimension D1@Fillet1@varyInstance.SLDPRT") : GoTo LastLine

        boolstatus = swFeatureMgr.InsertVaryInstanceIncrement("Space Increment", 4, 2, 0, 0.0349065850398866)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to add an increment value to direction 1 spacing") : GoTo LastLine

        boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Sketch2@varyInstance.SLDPRT", 4, 1, -1, 5, -1, 0.05)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to override value of dimension D1@Sketch2@varyInstance.SLDPRT at instance (5, 0)") : GoTo LastLine

        boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Sketch2@varyInstance.SLDPRT", 4, 1, -1, 3, -1, 0.06)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to override value of dimension D1@Sketch2@varyInstance.SLDPRT at instance (3, 0)") : GoTo LastLine

        boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Cut-Extrude1@varyInstance.SLDPRT", 4, 1, -1, 5, -1, 0.005)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to override value of dimension D1@Cut-Extrude1@varyInstance.SLDPRT at instance (5, 0)") : GoTo LastLine

        boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Fillet1@varyInstance.SLDPRT", 4, 1, -1, 5, -1, 0.006)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to override value of dimension D1@Fillet1@varyInstance.SLDPRT at instance (5, 0)") : GoTo LastLine

        boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Fillet1@varyInstance.SLDPRT", 4, 1, -1, 3, -1, 0.004)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to override value of dimension D1@Fillet1@varyInstance.SLDPRT at instance (3, 0)") : GoTo LastLine

        boolstatus = swFeatureMgr.InsertVaryInstanceOverride("Space Increment", 4, 2, 0, 5, -1, 1.30899693899575)
        If boolstatus = False Then ErrorMsg(swApp, "Failed to override value of direction 1 spacing increment at instance (3, 0)") : GoTo LastLine

        Dim myFeature As Feature
        myFeature = swFeatureMgr.FeatureCircularPattern4(6, 0.174532925199434, True, "NULL", False, False, True)
        If myFeature Is Nothing Then ErrorMsg(swApp, "Failed to create a vary instance circular pattern") : GoTo LastLine

LastLine:

    End Sub

    Function ErrorMsg(ByVal SwApp As Object, ByVal Message As String) As String
        SwApp.SendMsgToUser2(Message, 0, 0)
        SwApp.RecordLine("'*** WARNING - General")
        SwApp.RecordLine("'*** " & Message)
        SwApp.RecordLine("")
        Return ""
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you
    ''' </summary>
    Public swApp As SldWorks

End Class
```
