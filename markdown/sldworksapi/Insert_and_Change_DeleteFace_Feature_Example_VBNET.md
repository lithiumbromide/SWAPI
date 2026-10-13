---
title: "Insert and Change DeleteFace Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm"
---

# Insert and Change DeleteFace Feature Example (VB.NET)

This example shows how to insert a DeleteFace feature and how to then modify that feature.

```vb
' ------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\fillets\knob.sldprt.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Creates and modifies a DeleteFace feature.
 ' 2. Examine the Immediate window.
 '
 ' NOTE: Because this part document is used elsewhere, do not save changes.
 ' ------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics
 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swFeature As Feature
         Dim swDeleteFaceFeature As DeleteFaceFeatureData
         Dim featureName As String
         Dim boolstatus As Boolean
         Dim opt As Integer

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension

        ' Select a face for the
         ' DeleteFace feature
         boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.002251015125069, -0.001872569429423, 0.02015405789763, False, 0, Nothing, 0)

         ' Create a DeleteFace feature
         boolstatus = swModelDocExt.InsertDeleteFace(swFaceDeleteOption_e.swFaceDelete_Default)
         ' Get the DeleteFace feature
         swFeature = swModel.FirstFeature
         While Not swFeature Is Nothing
             featureName = swFeature.Name
             While featureName <> "DeleteFace1"
                 swFeature = swFeature.GetNextFeature
                 featureName = swFeature.Name
             End While
             Debug.Print("Feature name: " & featureName)
             swDeleteFaceFeature = swFeature.GetDefinition
             boolstatus = swDeleteFaceFeature.AccessSelections(swModel, Nothing)
             Debug.Print("  Number of deleted faces: " & swDeleteFaceFeature.GetDeletedFacesCount)

             ' Get the DeleteFace feature's option
             opt = swDeleteFaceFeature.Options
             Debug.Print("  Before changing the option...")
             DeleteFaceOptions(opt)

             ' Change the DeleteFace feature's option
             swDeleteFaceFeature.Options = swFaceDeleteOption_e.swFaceDelete_Patch
             opt = swDeleteFaceFeature.Options
             Debug.Print("  After changing the option...")
             DeleteFaceOptions(opt)

             ' Save modification made to DeleteFace feature
             boolstatus = swFeature.ModifyDefinition(swDeleteFaceFeature, swModel, Nothing)
             ' Get next feature until no more features

             swFeature = swFeature.GetNextFeature
         End While

     End Sub

    Sub DeleteFaceOptions(ByVal options As Long)
         Select Case options
             Case 0
                Debug.Print("    Option = swFaceDelete_Default")
             Case 1
                 Debug.Print("    Option = swFaceDelete_Patch")
             Case 2
                 Debug.Print("    Option = swFaceDelete_Fill")
             Case 3
                 Debug.Print("    Option = swFaceDelete_FillWithTangent")
         End Select
     End Sub
    ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks
End Class
```
