---
title: "Create Save Bodies Feature and Create an Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Save_Bodies_Feature_and_Create_Assembly_Example_VB.htm"
---

# Create Save Bodies Feature and Create an Assembly Example (VBA)

This example shows how to create a save bodies feature, create part documents with the save bodies, and create an assembly with the parts.

```vb
  '--------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Part document is open and contains a feature split of two.
 ' 2. The Solid Bodies folder contains Split1[1] and Split2[2].
 ' 3. C:\temp\SaveBodies exists.
 '
 ' Postconditions:
 ' 1. C:\temp\SaveBodies\1.sldprt, C:\temp\SaveBodies\2.sldprt,
 '    and C:\temp\assem.sldasm are created.
 ' 2. In the original part, Save Bodies1 appears in the FeatureManager design tree.
  '-----------------------------------------------------------------------------------------

 Option Explicit

 Dim swApp As SldWorks.SldWorks

 Dim swModel As SldWorks.ModelDoc2

 Dim swSelMgr As SldWorks.SelectionMgr

 Dim swFeat As SldWorks.Feature

 Dim swFeatMgr As SldWorks.FeatureManager

 Dim swBodyFolder As SldWorks.BodyFolder

 Dim v1 As Variant

 Dim i As Long

 Dim fileNames(1) As String

 Dim fileNameVar As Variant

 Sub GetVariantOfBody(swFeature As SldWorks.Feature, bodyList As Variant)

     Dim tt As Variant

     Set swBodyFolder = swFeature.GetSpecificFeature2

     Dim count As Integer

     count = swBodyFolder.GetBodyCount

     If (count < 1) Then

         MsgBox ("There are no bodies. Please create a body.")

     Else

         bodyList = swBodyFolder.GetBodies

     End If

 End Sub

 Sub main()

     Set swApp = Application.SldWorks

     Set swModel = swApp.ActiveDoc

     Set swSelMgr = swModel.SelectionManager

     Set swFeat = swModel.FirstFeature

     Set swFeatMgr = swModel.FeatureManager

     Dim contLoop As Boolean

     contLoop = True

     While Not swFeat Is Nothing And contLoop = True

         Dim Name As String

         Name = swFeat.GetTypeName2

         If (Name = "SolidBodyFolder") Then

             GetVariantOfBody swFeat, v1

             contLoop = False

         End If

         If (contLoop = True) Then

             Set swFeat = swFeat.GetNextFeature

         End If

     Wend

     fileNames(0) = "C:\temp\SaveBodies\1.sldprt"
     fileNames(1) = "C:\temp\SaveBodies\2.sldprt"

     fileNameVar = fileNames

     swFeatMgr.CreateSaveBodyFeature v1, fileNameVar, "c:\temp\assem.sldasm", -1, -1

 End Sub
```
