Attribute VB_Name = "Macro"
Option Explicit
Dim swApp As SldWorks.SldWorks
Sub main()
    Set swApp = Application.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then
        Report "Open a part or an assembly first."
        Exit Sub
    End If
    If swModel.GetType <> swDocPART And swModel.GetType <> swDocASSEMBLY Then
        Report "The active document must be a part or an assembly."
        Exit Sub
    End If
    If swModel.GetPathName = "" Then
        Report "Save the document before running this macro."
        Exit Sub
    End If
    Dim originalConfig As String
    originalConfig = swModel.ConfigurationManager.ActiveConfiguration.Name
    On Error GoTo Failed
    Process swModel
Cleanup:
    On Error Resume Next
    swModel.ShowConfiguration2 originalConfig
    Exit Sub
Failed:
    Report "Error " & Err.Number & ": " & Err.Description
    Resume Cleanup
End Sub
Private Sub Process(ByVal swModel As SldWorks.ModelDoc2)
    Dim sourcePath As String
    Dim dot As Long
    sourcePath = swModel.GetPathName
    dot = InStrRev(sourcePath, ".")
    Dim target As String
    target = Left$(sourcePath, dot - 1) & "_copy" & Mid$(sourcePath, dot)
    If SaveCopy(swModel, target) Then Debug.Print "Saved " & target
End Sub
Private Function SaveCopy(ByVal swModel As SldWorks.ModelDoc2, ByVal target As String) As Boolean
    Dim errors As Long
    Dim warnings As Long
    swModel.ClearSelection2 True
    SaveCopy = swModel.Extension.SaveAs3(target, swSaveAsCurrentVersion, swSaveAsOptions_Silent Or swSaveAsOptions_Copy, Nothing, Nothing, errors, warnings)
    If Not SaveCopy Then
        Report "Save failed for " & target & ", swFileSaveError_e flags " & errors
    ElseIf warnings <> 0 Then
        Debug.Print "Saved " & target & " with swFileSaveWarning_e flags " & warnings
    End If
End Function
Private Sub Report(ByVal message As String)
    swApp.SendMsgToUser2 message, swMbWarning, swMbOk
End Sub
