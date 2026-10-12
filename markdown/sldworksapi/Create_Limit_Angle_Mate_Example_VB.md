---
title: "Create and Edit Limit Angle Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Limit_Angle_Mate_Example_VB.htm"
---

# Create and Edit Limit Angle Mate Example (VBA)

This example shows how to create and edit a limit angle mate.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Open:
' `public_documents`**\samples\tutorial\api\AdvancedMates\AdvancedMateDemo1.sldasm**
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Creates a limit angle mate.
' 2. Press F5 to continue.
' 3. Modifies the mate alignment of the limit angle mate.
' 4. Inspect the Immediate window and graphics area.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'----------------------------------------------------------------------------

```vb
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swAssy As SldWorks.AssemblyDoc
 Dim swAngleMateData As SldWorks.AngleMateFeatureData
 Dim swMateData As SldWorks.MateFeatureData
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean
 Dim feat As SldWorks.Feature
 Dim facesDist(1) As SldWorks.Face2
 Dim vFacesDist As Variant
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swAssy = swModel
     Set swSelMgr = swModel.SelectionManager

    Set swMateData = swAssy.CreateMateData(6) 'Angle mate

     Debug.Print "Type of mate as defined in swMateType_e: " & swMateData.TypeName

    Set swAngleMateData = swMateData
     swAngleMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignALIGNED
     swAngleMateData.FlipDimension = False
     swAngleMateData.Angle = 0.523599
     swAngleMateData.MaximumAngle = 0.523599
     swAngleMateData.MinimumAngle = 0.506145

    boolstatus = swModel.Extension.SelectByRay(8.68857956595548E-03, 4.14144214960288E-02, 6.33435410960033E-02, -0.520148774728431, -0.59141018013918, -0.616181183562315, 4.68381592786756E-04, 2, True, 1, 0)
     boolstatus = swModel.Extension.SelectByRay(3.13565896258297E-02, 2.96508617577445E-02, 4.42099188854286E-02, 0.340524666870961, -0.380278973953885, -0.859901653226112, 4.31713609895031E-04, 2, True, 1, 0)

    Set facesDist(0) = swSelMgr.GetSelectedObject6(1, -1)
     Set facesDist(1) = swSelMgr.GetSelectedObject6(2, -1)

    vFacesDist = facesDist
     swAngleMateData.EntitiesToMate = vFacesDist

    Set feat = swAssy.CreateMate(swAngleMateData)

     swModel.GraphicsRedraw2

    Stop

    Set feat = swModel.Extension.GetLastFeatureAdded
     Debug.Print "Feature type created is " & feat.GetTypeName2

    Set swMateData = feat.GetDefinition
     Set swAngleMateData = swMateData

    'Change alignment of limit angle mate
     If (swMateData.TypeName = SwConst.swMateType_e.swMateANGLE) Then

        Debug.Print "Angle mate alignment is " & swAngleMateData.MateAlignment

        If (swAngleMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignALIGNED) Then
             swAngleMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignANTI_ALIGNED
         Else
             swAngleMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignALIGNED
         End If

        Debug.Print "Angle mate alignment changed to " & swAngleMateData.MateAlignment
         Debug.Print "Angle: " & swAngleMateData.Angle
         Debug.Print "Minimum angle: " & swAngleMateData.MinimumAngle
         Debug.Print "Maximum angle: " & swAngleMateData.MaximumAngle
         Debug.Print "Move entities to opposite sides of the dimension? " & swAngleMateData.FlipDimension

        boolstatus = feat.ModifyDefinition(swAngleMateData, swAssy, Nothing)
    End If
End Sub
```
