---
title: "Fire Application and Document Events Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Fire_Application_and_Document_Events_Example_VBNET.htm"
---

# Fire Application and Document Events Example (VB.NET)

This example shows how to fire application and document events.

```
'------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Change the path and file name of the image file to insert.
'    NOTE: The image file must be a PNG file.
' 5. Start DraftSight, create, save, and close a drawing
'    named c:\test\circle.dwg.
' 6. Set a breakpoint in the project where the project connects to
'    DraftSight.
' 7. Press F10 to step through the project.
'
' Postconditions: Message boxes pop up for all events,
' regardless if fired. Read the text in each message box before
' clicking OK to close it.
'--------------------------------------------------------------
```

```
Imports System.IO
Imports DraftSight.Interop.dsAutomation
```

```
Module Module_DocEvents
```

```
    Dim WithEvents dsApp As Application
    Dim WithEvents dsDoc As Document
    Dim filePreOpenNotify As Boolean
    Dim filePostOpenNotify As Boolean
    Dim docDestroyNotify As Boolean
    Dim fileSavePreNotify As Boolean
    Dim fileSavePostNotify As Boolean
    Dim fileModifyNotify As Boolean
```

```
    Public docName As String = "c:\test\circle.dwg"
    Public imageFileName As String = "c:\test\note.png"
```

```
    Sub Main()
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Open document
        TestFileOpenEvents()
```

```
        'Modify document
        TestFileModifyEvents()
```

```
        'Save document as a different document
        TestFileSaveEvents()
```

```
        'Close open document
        CloseAllDocuments()
```

```
    End Sub
```

```
    Private Sub TestFileOpenEvents()
```

```
        filePreOpenNotify = False
        filePostOpenNotify = False
```

```
        'Open document
        dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default)
```

```
)
        If Not dsDoc Is Nothing Then
            If False = filePreOpenNotify Then
                MsgBox("FileOpenPreNotify event wasn't fired while opening a document.")
            End If
            If False = filePostOpenNotify Then
                MsgBox("FileOpenPostNotify event wasn't fired while opening a document.")
            End If
        Else
            MsgBox("OpenDocument method returns Nothing for '" & docName & "' document.")
        End If
    End Sub
```

```
    Private Sub TestFileModifyEvents()
```

```
        Dim dsPicture As ReferenceImage = Nothing
```

```
        Dim dsModel As Model
        Dim dsSketchMgr As DraftSight.Interop.dsAutomation.SketchManager
```

```
        If Not dsDoc Is Nothing Then
            'Get model space
            dsModel = dsDoc.GetModel
            If Not dsModel Is Nothing Then
                'Get sketch manager
                dsSketchMgr = dsModel.GetSketchManager
                If Not dsSketchMgr Is Nothing Then
                    fileModifyNotify = False
```

```
                    'Insert a picture in the model
                    dsPicture = dsSketchMgr.InsertPicture(imageFileName, 0.0, 0.0, 0.0, 1.0, 0.0)
```

```
                    If Not dsPicture Is Nothing Then
```

```
                        'Check if ModifyNotify event is fired
                        If False = fileModifyNotify Then
                            MsgBox("ModifyNotify event wasn't fired while inserting a picture in the document.")
                        End If
                    Else
                        MsgBox("ISketchManager::InsertPicture method returns Nothing for the '" & dsDoc.GetPathName & "' document")
                    End If
                Else
                    MsgBox("IModel.GetSketchManager method returns Nothing for the '" & dsDoc.GetPathName & "' document.")
                End If
            Else
                MsgBox("IDocument.GetModel method returns Nothing for the '" & dsDoc.GetPathName & "' document.")
            End If
        Else
            MsgBox("IApplication.OpenDocument method returns Nothing for the '" & docName & "' document.")
        End If
    End Sub
    Private Sub TestFileSaveEvents()
```

```
        Dim savedDocName As String
        Dim saveError As dsDocumentSaveError_e
```

```
        If Not dsDoc Is Nothing Then
            fileSavePreNotify = False
            fileSavePostNotify = False
            'Save document
            savedDocName = docName & "_saved.dwg"
            dsDoc.SaveAs2(savedDocName, dsDocumentSaveAsOption_e.dsDocumentSaveAs_R2010_DWG, True, saveError)
            If saveError <> dsDocumentSaveError_e.dsDocumentSave_Succeeded Then
                MsgBox("SaveAs method returns '" & saveError & "' error.")
            Else
                'Check FileSavePreNotify and FileSavePostNotify events
                If False = fileSavePreNotify Then
                    MsgBox("FileSavePreNotify event wasn't fired after saving the '" & docName & "' document")
                End If
                If False = fileSavePostNotify Then
                    MsgBox("FileSavePostNotify event wasn't fired after saving the '" & docName & "' document")
                End If
            End If
        Else
            MsgBox("OpenDocument method returns Nothing for the '" & docName & "' document.")
        End If
    End Sub
```

```
    Private Sub CloseAllDocuments()
        Dim dsDocs As Object
        Dim index As Integer
        'Get documents
        dsDocs = dsApp.GetDocuments
        If IsArray(dsDocs) Then
            For index = LBound(dsDocs) To UBound(dsDocs)
                dsDoc = dsDocs(index)
                dsApp.CloseDocument(dsDoc.GetPathName(), False)
                If False = docDestroyNotify Then
                    MsgBox("DestroyNotify event wasn't fired after closing a document.")
                End If
            Next
        End If
    End Sub
    Private Sub dsApp_FileOpenPostNotify(ByVal Document As Document) Handles dsApp.FileOpenPostNotify
        filePostOpenNotify = True
        MsgBox("FileOpenPostNotify event was fired while opening a document.")
    End Sub
    Private Sub dsApp_FileOpenPreNotify(ByVal FileName As String, ByVal [Option] As dsDocumentOpenOption_e) Handles dsApp.FileOpenPreNotify
        filePreOpenNotify = True
        MsgBox("FileOpenPreNotify event was fired while opening a document.")
    End Sub
    Private Sub dsDoc_DestroyNotify() Handles dsDoc.DestroyNotify
        docDestroyNotify = True
        MsgBox("DestroyNotify event was fired after closing a document.")
    End Sub
    Private Sub dsDoc_FileSavePostNotify() Handles dsDoc.FileSavePostNotify
        fileSavePostNotify = True
        MsgBox("FileSavePostNotify event was fired after saving the '" & docName & "' document")
    End Sub
    Private Sub dsDoc_FileSavePreNotify(ByVal FileName As String, ByVal SaveOption As dsDocumentSaveAsOption_e) Handles dsDoc.FileSavePreNotify
        fileSavePreNotify = True
        MsgBox("FileSavePreNotify event was fired after saving the '" & FileName & "' document")
    End Sub
    Private Sub dsDoc_ModifyNotify() Handles dsDoc.ModifyNotify
        fileModifyNotify = True
        MsgBox("ModifyNotify event was fired while inserting a picture in document.")
    End Sub
End Module
```
