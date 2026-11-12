---
title: "Add Spring to Motion Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Spring_to_Motion_Study_Example_VBNET.htm"
---

# Add Spring to Motion Study Example (VB.NET)

This example shows how to add a spring to a motion study.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\wrench.sldasm.
 ' 2. Verify that the MotionManager tab is visible. If it is not visible,
 '    click View > MotionManager.
 ' 3. Right-click the project, select Add Reference, click Browse, and
 '    select install_dir\api\redist\SolidWorks.Interop.swmotionstudy.dll.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1 Adds a spring feature between the grips of the wrench.
 ' 2. Examine the Immediate window.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SwMotionStudy
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swMotionMgr As MotionStudyManager
        Dim swMotionStudy1 As MotionStudy
        Dim swSpringFeat As SimulationSpringFeatureData
        Dim boolstatus As Boolean
        Dim swFeat As Feature
        Dim swSelMgr As SelectionMgr

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager

        ' Get the MotionManager
        swMotionMgr = swModelDocExt.GetMotionStudyManager()
        If (swMotionMgr Is Nothing) Then
            Exit Sub
        End If

        ' Get "MotionStudy1_Distance=0.5in"
        swMotionStudy1 = swMotionMgr.GetMotionStudy("MotionStudy1_Distance=0.5in")
        If (swMotionStudy1 Is Nothing) Then
            MsgBox("MotionStudy1_Distance=0.5in is not available.")
            Exit Sub
        End If

        ' Activate "MotionStudy1_Distance=0.5in"
        swMotionStudy1.Activate()

        ' Define spring feature
        swSpringFeat = swMotionStudy1.CreateDefinition(swFeatureNameID_e.swFmAEMLinearMotionSpring)
        If swSpringFeat Is Nothing Then
            Debug.Print("ERROR: Creation of Spring feature data object failed.")
            Exit Sub
        End If

       ' Select spring's endpoints
        Dim swFace1 As Face2, swFace2 As Face2
        swModel.ShowNamedView2("*Left", 3)
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03344586330968, 0.0525345575174, 0, True, 0, Nothing, 0)
        swFace1 = swSelMgr.GetSelectedObject6(1, -1)
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02244533711473, 0.0131288302002, 0.0002238961779386, True, 0, Nothing, 0)
        swFace2 = swSelMgr.GetSelectedObject6(2, -1)

       ' Set spring characteristics
        swSpringFeat.SetEndPoints(swFace1, swFace2)
        swSpringFeat.CoilDiameter = 0.0102
        swSpringFeat.NumberOfCoils = 3
        swSpringFeat.WireDiameter = 0.00152
        swSpringFeat.FreeLength = 0.02

        ' Create Spring feature
        swFeat = swMotionStudy1.CreateFeature(swSpringFeat)
        If swFeat Is Nothing Then
            Debug.Print(" ERROR: Creation of the Spring feature failed.")
        Else
            Debug.Print("Type of the feature added: " & swFeat.GetTypeName2)
        End If

         Debug.Print("Type of spring as defined in swSpringType_e: " & swSpringFeat.Type)

    End Sub
    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
