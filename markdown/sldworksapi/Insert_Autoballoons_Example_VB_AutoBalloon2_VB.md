---
title: "Insert Autoballoons Example (VBA) (AutoBalloon2)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm"
---

# Insert Autoballoons Example (VBA) (AutoBalloon2)

## Insert Autoballoons Example (VBA)

This example shows how to insert autoballoons in a drawing document using the now obsolete method IDrawingDoc::AutoBalloon2.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Selects a drawing view.
' 3. Inserts autoballoons for each resolved component in
'    the selected drawing view.
' 4. Examine the drawing and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'------------------------------------------------------------------
```

```
Sub main()
```

```
    Const swDetailingBalloonLayout_Default As Long = -1
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim vNoteArr As Variant
    Dim vNote As Variant
    Dim swNote As SldWorks.Note
    Dim swAnn As SldWorks.Annotation
    Dim vAttachPos As Variant
    Dim vAnnPos As Variant
    Dim bRet  As Boolean
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open drawing
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    bRet = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
```

```
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
```

```
    bRet = swDraw.ActivateView(swView.Name): Debug.Assert bRet
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    ' Get autoballoon settings
    Debug.Print "  DetailingBalloonsDisplayWithBentLeader = " & swModel.GetUserPreferenceToggle(swDetailingBalloonsDisplayWithBentLeader)
    Debug.Print "  DetailingBOMBalloonStyle = " & swModel.GetUserPreferenceIntegerValue(swDetailingBOMBalloonStyle)
    Debug.Print "  DetailingBOMBalloonFit = " & swModel.GetUserPreferenceIntegerValue(swDetailingBOMBalloonFit)
    Debug.Print "  DetailingAutoBalloonLayout = " & swModel.GetUserPreferenceIntegerValue(swDetailingAutoBalloonLayout)
    Debug.Print "  DetailingBalloonBentLeaderLength = " & swModel.GetUserPreferenceDoubleValue(swDetailingBalloonBentLeaderLength) * 1000# & " mm"
```

```
    Debug.Print ""
    Debug.Print "  " & swView.Name
```

```
    vNoteArr = swDraw.AutoBalloon2(swDetailingBalloonLayout_Default, False)
```

```
    ' Returns an empty array if:
    ' *  Balloons already exist in any drawing view on any on sheet in
    '    the drawing document.
    ' *  Drawing document is lightweight.
    ' Returns a note for each resolved component in the selected drawing view.
    If IsEmpty(vNoteArr) Then
        Debug.Print "    No balloons added."
        Exit Sub
    End If
```

```
    For Each vNote In vNoteArr
        Set swNote = vNote
        Set swAnn = swNote.GetAnnotation
        vAttachPos = swNote.GetAttachPos
        vAnnPos = swAnn.GetPosition
```

```
        Debug.Print "    Autoballon text = " & swNote.GetText
        If swAnn.Layer = "" Then
            Debug.Print "      No layers defined."
        Else
            Debug.Print "      Layer = " & swAnn.Layer
        End If
        Debug.Print "      Note attachment point = (" & vAttachPos(0) * 1000# & ", " & vAttachPos(1) * 1000# & ", " & vAttachPos(2) * 1000# & ") mm"
        Debug.Print "      Origin of annotation = (" & vAnnPos(0) * 1000# & ", " & vAnnPos(1) * 1000# & ", " & vAnnPos(2) * 1000# & ") mm"
    Next
```

```
End Sub
```
