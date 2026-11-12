---
title: "Save Solid Body to File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Solid_Body_to_File_Example_VB.htm"
---

# Save Solid Body to File Example (VBA)

This example shows how to save a weldment member to another part document.

```
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
' 6. To verify steps 2 and 3, open and inspect RefWeldment1.sldprt, which resides in
'    the same folder as this macro.
'
' NOTE: Because weldment_box3.sldprt is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Dim Swapp As SldWorks.SldWorks

Dim swFeat As SldWorks.Feature

Dim swBodyFolder As SldWorks.BodyFolder

Dim updateBoolstatus As Boolean

Dim boolstatus As Boolean

Dim longstatus As Long

Dim longWarnings As Long

Dim currentModel As SldWorks.ModelDoc2

Dim swModel As SldWorks.ModelDoc2

Dim modelType As Long

Dim modelTitle As String
```

```vb
Option Explicit
 Sub main()
    Set Swapp = Application.SldWorks
     Set currentModel = Swapp.ActiveDoc

    modelTitle = currentModel.GetTitle
     modelType = currentModel.GetType

    Set swFeat = currentModel.FirstFeature
     If swFeat Is Nothing Then ErrorMsg Swapp, "Failed to get first feature"

    Do While Not swFeat Is Nothing
         If swFeat.GetTypeName2 = "SolidBodyFolder" Then
             Set swBodyFolder = swFeat.GetSpecificFeature2
             If swBodyFolder Is Nothing Then ErrorMsg Swapp, "Failed to get body folder"

            boolstatus = swBodyFolder.SetAutomaticCutList(True)

            boolstatus = swBodyFolder.UpdateCutList()

            Exit Do
         End If
         Set swFeat = swFeat.GetNextFeature
     Loop

    updateBoolstatus = False

    Set swFeat = currentModel.FirstFeature
     If swFeat Is Nothing Then ErrorMsg Swapp, "Failed to get first feature"

    Do While Not swFeat Is Nothing
         If swFeat.GetTypeName2 = "WeldMemberFeat" Then
             boolstatus = swFeat.Select2(False, 0)
             If boolstatus = False Then ErrorMsg Swapp, "Failed to select feature"

            ' Save the selected solid body weldment member to another part,
             ' transferring the solid body's cut list properties to the new part's cut list;
             ' automatically creates a weldment and cut list folder
             boolstatus = currentModel.SaveToFile3(Swapp.GetCurrentMacroPathFolder + "\RefWeldment1" + ".sldprt", 1,  swCutListTransferOptions_CutListProperties, False, "", longstatus, longWarnings)
             Stop
             If boolstatus = False Then ErrorMsg Swapp, "Failed to insert weldment member into new part"

            Set swModel = Swapp.ActiveDoc
             If swModel Is Nothing Then ErrorMsg Swapp, "Failed to set open model as active document"

           updateBoolstatus = True
             Exit Do
         End If
         Set swFeat = swFeat.GetNextFeature
     Loop

    If updateBoolstatus = True Then
         Set swFeat = currentModel.FirstFeature
         If swFeat Is Nothing Then ErrorMsg Swapp, "Failed to get first feature"

        Do While Not swFeat Is Nothing
             If swFeat.GetTypeName2 = "SolidBodyFolder" Then
                 Set swBodyFolder = swFeat.GetSpecificFeature2
                 If swBodyFolder Is Nothing Then ErrorMsg Swapp, "Failed to get body folder"

                boolstatus = swBodyFolder.SetAutomaticCutList(True)
                 If boolstatus = False Then ErrorMsg Swapp, "Failed to set cut list to automatic"

                boolstatus = swBodyFolder.UpdateCutList()
                 If boolstatus = False Then ErrorMsg Swapp, "Failed to update cut list"

             Swapp.CloseDoc swModel.GetTitle
                 Exit Do
             End If
             Set swFeat = swFeat.GetNextFeature
         Loop
     End If
End Sub
Function ErrorMsg(Swapp As Object, Message As String)
     Swapp.SendMsgToUser2 Message, 0, 0
     Swapp.RecordLine "'*** WARNING - General"
     Swapp.RecordLine "'*** " & Message
     Swapp.RecordLine ""
 End Function
```
