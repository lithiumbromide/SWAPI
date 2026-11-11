Attribute VB_Name = "Macro"
Option Explicit
Dim dsApp As DraftSight.Application
Sub main()
    On Error Resume Next
    Set dsApp = GetObject(, "DraftSight.Application")
    On Error GoTo 0
    If dsApp Is Nothing Then
        MsgBox "Start DraftSight and open a drawing, then run the macro again.", vbExclamation, "DraftSight macro"
        Exit Sub
    End If
    dsApp.AbortRunningCommand
    Dim dsDoc As DraftSight.Document
    Set dsDoc = dsApp.GetActiveDocument()
    If dsDoc Is Nothing Then
        Report "Open a drawing first."
        Exit Sub
    End If
    If dsDoc.IsReadOnly() Then
        Report "The active drawing is read-only."
        Exit Sub
    End If
    Dim dsSketchManager As DraftSight.SketchManager
    Set dsSketchManager = dsDoc.GetModel().GetSketchManager()
    On Error GoTo Failed
    dsSketchManager.StartUndoRecord
    Process dsDoc, dsSketchManager
Cleanup:
    On Error Resume Next
    dsSketchManager.StopUndoRecord
    Exit Sub
Failed:
    Report "Error " & Err.Number & ": " & Err.Description
    Resume Cleanup
End Sub
Private Sub Process(ByVal dsDoc As DraftSight.Document, ByVal dsSketchManager As DraftSight.SketchManager)
    Const layerName As String = "API_GEOMETRY"
    If EnsureLayer(dsDoc, layerName) Is Nothing Then Exit Sub
    Dim dsLine As DraftSight.Line
    Set dsLine = dsSketchManager.InsertLine(0#, 0#, 0#, 100#, 50#, 0#)
    If dsLine Is Nothing Then
        Report "InsertLine failed."
        Exit Sub
    End If
    dsLine.Layer = layerName
    Dim dsCircle As DraftSight.Circle
    Set dsCircle = dsSketchManager.InsertCircle(50#, 25#, 0#, 10#)
    If dsCircle Is Nothing Then
        Report "InsertCircle failed."
        Exit Sub
    End If
    dsCircle.Layer = layerName
    Dim dsColor As DraftSight.Color
    Set dsColor = dsApp.GetNamedColor(dsNamedColor_Red)
    dsCircle.Color = dsColor
    dsApp.GetCommandMessage().PrintLine "Macro: added a line and a circle on layer " & layerName
End Sub
Private Function EnsureLayer(ByVal dsDoc As DraftSight.Document, ByVal layerName As String) As DraftSight.Layer
    Dim dsLayerManager As DraftSight.LayerManager
    Set dsLayerManager = dsDoc.GetLayerManager()
    Dim dsLayer As DraftSight.Layer
    Dim result As dsCreateObjectResult_e
    dsLayerManager.CreateLayer layerName, dsLayer, result
    If result = dsCreateObjectResult_AlreadyExists Then
        Set dsLayer = dsLayerManager.GetLayer(layerName)
    ElseIf result <> dsCreateObjectResult_Success Then
        Set dsLayer = Nothing
    End If
    If dsLayer Is Nothing Then Report "Could not create or find layer " & layerName
    Set EnsureLayer = dsLayer
End Function
Private Sub Report(ByVal message As String)
    MsgBox message, vbExclamation, "DraftSight macro"
End Sub
