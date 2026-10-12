---
title: "Save Solid Body to File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Solid_Body_to_File_Example_VBNET.htm"
---

# Save Solid Body to File Example (VB.NET)

This example shows how to save a weldment member to another part document.

```vb
'----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 '
 ' Postconditions:
 ' 1. Updates the cut list in the weldment part.
 ' 2. Saves the first weldment member in the FeatureManager design tree to
 '    RefWeldment1.sldprt, and saves the cut list properties in the parent part
 '    to the cut list of the new part.
 ' 3. Opens RefWeldment1.sldprt and updates its cut list. (This step could
 '    take a few minutes to complete.)
 ' 4. At Stop, press F5.
 ' 5. Closes RefWeldment1.sldprt.
 ' 6. To verify steps 2 and 3, open and inspect RefWeldment1.sldprt, which resides
 '    in the same folder as this macro.
 '
 ' NOTE: Because weldment_box3.sldprt is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim swFeat As Feature
     Dim swBodyFolder As BodyFolder
     Dim updateBoolstatus As Boolean
     Dim boolstatus As Boolean
     Dim longstatus As Integer
     Dim longWarnings As Integer
     Dim currentModel As ModelDoc2
     Dim swModel As ModelDoc2
     Dim modelType As Integer
     Dim modelTitle As String

     Sub main()

         currentModel = swApp.ActiveDoc

         modelTitle = currentModel.GetTitle
         modelType = currentModel.GetType

         swFeat = currentModel.FirstFeature
         If swFeat Is Nothing Then ErrorMsg(swApp, "Failed to get first feature")

         Do While Not swFeat Is  Nothing
             If swFeat.GetTypeName2 = "SolidBodyFolder" Then
                 swBodyFolder = swFeat.GetSpecificFeature2
                 If swBodyFolder Is Nothing Then ErrorMsg(swApp, "Failed to get body folder")

                 boolstatus = swBodyFolder.SetAutomaticCutList(True)

                 boolstatus = swBodyFolder.UpdateCutList()

                 Exit Do
             End If
             swFeat = swFeat.GetNextFeature
         Loop

         updateBoolstatus =  False

         swFeat = currentModel.FirstFeature
         If swFeat Is Nothing Then ErrorMsg(swApp, "Failed to get first feature")

         Do While Not swFeat Is  Nothing
             If swFeat.GetTypeName2 = "WeldMemberFeat" Then
                 boolstatus = swFeat.Select2(False, 0)
                 If boolstatus = False Then ErrorMsg(swApp, "Failed to select feature")

                 ' Save the selected solid body weldment member to another part,
                 ' transferring the solid body's cut list properties to the new part's cut list;
                 ' automatically creates a weldment and cut list folder
                 boolstatus = currentModel.SaveToFile3(swApp.GetCurrentMacroPathFolder + "\RefWeldment1" + ".sldprt", 1, swCutListTransferOptions_e.swCutListTransferOptions_CutListProperties, False, "", longstatus, longWarnings)

                 Stop

                 If boolstatus = False Then ErrorMsg(swApp, "Failed to insert weldment member into new part")

                 swModel = swApp.ActiveDoc
                 If swModel Is Nothing Then ErrorMsg(swApp, "Failed to set open model as active document")

                 updateBoolstatus = True
                 Exit Do
             End If
             swFeat = swFeat.GetNextFeature
         Loop

         If updateBoolstatus = True Then
             swFeat = currentModel.FirstFeature
             If swFeat Is Nothing Then ErrorMsg(swApp, "Failed to get first feature")

             Do While Not swFeat Is  Nothing
                 If swFeat.GetTypeName2 = "SolidBodyFolder" Then
                     swBodyFolder = swFeat.GetSpecificFeature2
                     If swBodyFolder Is Nothing Then ErrorMsg(swApp, "Failed to get body folder")

                     boolstatus = swBodyFolder.SetAutomaticCutList(True)
                     If boolstatus = False Then ErrorMsg(swApp, "Failed to set cut list to automatic")

                     boolstatus = swBodyFolder.UpdateCutList()
                     If boolstatus = False Then ErrorMsg(swApp, "Failed to update cut list")

                     swApp.CloseDoc(swModel.GetTitle)
                     Exit Do
                 End If
                 swFeat = swFeat.GetNextFeature
             Loop
         End If

     End Sub

     Sub ErrorMsg(ByVal Swapp As Object, ByVal Message As String)
         Swapp.SendMsgToUser2(Message, 0, 0)
         Swapp.RecordLine("'*** WARNING - General")
         Swapp.RecordLine("'*** " & Message)
         Swapp.RecordLine("")
     End Sub

     Public swApp As SldWorks

 End  Class
```
