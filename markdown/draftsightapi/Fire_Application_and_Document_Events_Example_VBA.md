---
title: "Fire Application and Document Events Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Fire_Application_and_Document_Events_Example_VBA.htm"
---

# Fire Application and Document Events Example (VBA)

This example shows how to fire application and document events.

'-----------------------------------------------------------------

' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
' embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' a. In Modules, copy and paste the [Main module](#Main_module).
' b. Insert a class called Class1, and paste the [Class1 module](#Class1_module).
' c. Insert a class called Class2, and paste the [Class2 module](#Class2_module).
' 3. Add a reference to the DraftSight type library, ' `install_dir`\**bin\dsAutomation.dll**.
' 4. Change the path and file name of the image file to insert.
' **NOTE**: The image file must be a PNG file.
' 5. Start DraftSight, create, save, and close a drawing
' named **c:\test\circle.dwg**.
' 6. Set a breakpoint in the project where the project connects to
' DraftSight.
' 7. Press F8 to step through the project.
'
' Postconditions: Message boxes pop up for all events,
' regardless if fired. Read the text in each message box
' before clicking OK to close it.

'------------------------------------------------------------------

```
'Main module
Option Explicit
```

```
Public dsAppEvents As Class1
Public dsDocEvents As Class2
```

```
Public dsApp As DraftSight.Application
Public dsDoc As DraftSight.Document
Public docName As String
```

```
Public filePreOpenNotify As Boolean
Public filePostOpenNotify As Boolean
Public fileModifyNotify As Boolean
Public fileSavePreNotify As Boolean
Public fileSavePostNotify As Boolean
Public docDestroyNotify As Boolean
```

```
Sub main()
```

```
        'Connect to DraftSight
        Set dsApp = GetObject(, "DraftSight.Application")
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Document to open
        docName = "c:\test\circle.dwg"
```

```
        'Set up events
        Set dsAppEvents = New Class1
        Set dsDocEvents = New Class2
        Set dsAppEvents = New Class1
        Set dsAppEvents.app = dsApp
```

```
        'Open document
        TestFileOpenEvents
```

```
        'Modify document
        TestFileModifyEvents
```

```
        'Save document as a different document
        TestFileSaveEvents
```

```
        'Close open document
        CloseAllDocuments
```

```
End Sub
```

```
Public Sub TestFileOpenEvents()
```

```
        'Open document
        Set dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default)
```

```
        Set dsDocEvents = New Class2
        Set dsDocEvents.doc = dsDoc
```

```
        If Not dsDoc Is Nothing Then
            If False = filePreOpenNotify Then
                MsgBox ("FileOpenPreNotify event wasn't fired while opening a document.")
            End If
            If False = filePostOpenNotify Then
                MsgBox ("FileOpenPostNotify event wasn't fired while opening a document.")
            End If
        Else
            MsgBox ("OpenDocument method returns Nothing for '" & docName & "' document.")
        End If
```

```
End Sub
```

```
    Public Sub TestFileModifyEvents()
```

```
        Dim imageFileName As String
        imageFileName = "c:\test\note.png"
```

```
        Dim dsPicture As DraftSight.ReferenceImage
        Dim dsModel As DraftSight.Model
        Dim dsSketchMgr As DraftSight.SketchManager
```

```
        If Not dsDoc Is Nothing Then
            'Get model space
            Set dsModel = dsDoc.GetModel
            If Not dsModel Is Nothing Then
                'Get sketch manager
                Set dsSketchMgr = dsModel.GetSketchManager
                If Not dsSketchMgr Is Nothing Then
                    fileModifyNotify = False
                    'Insert a picture in the model
                    Set dsPicture = dsSketchMgr.InsertPicture(imageFileName, 0#, 0#, 0#, 1#, 0#)
                    If Not dsPicture Is Nothing Then
                        'Check if ModifyNotify event is fired
                        If False = fileModifyNotify Then
                            MsgBox ("ModifyNotify event wasn't fired while inserting a picture in the document.")
                        End If
                    Else
                        MsgBox ("ISketchManager::InsertPicture method returns Nothing for the '" & dsDoc.GetPathName & "' document")
                    End If
                Else
                    MsgBox ("IModel.GetSketchManager method returns Nothing for the '" & dsDoc.GetPathName & "' document.")
                End If
            Else
                MsgBox ("IDocument.GetModel method returns Nothing for the " & dsDoc.GetPathName & " document.")
            End If
        Else
            MsgBox ("IApplication.OpenDocument method returns Nothing for the " & docName & " document.")
        End If
    End Sub
    Public Sub TestFileSaveEvents()
```

```
        Dim savedDocName As String
        Dim saveError As Long
```

```
        If Not dsDoc Is Nothing Then
            fileSavePreNotify = False
            fileSavePostNotify = False
            'Save document
            savedDocName = docName & "_saved.dwg"
            dsDoc.SaveAs2 savedDocName, dsDocumentSaveAs_R2010_DWG, True, saveError
            If saveError <> dsDocumentSave_Succeeded Then
                MsgBox ("SaveAs method returns '" & saveError & "' error.")
            Else
                'Check FileSavePreNotify and FileSavePostNotify events
                If False = fileSavePreNotify Then
                    MsgBox ("FileSavePreNotify event wasn't fired after saving the '" & docName & "' document")
                End If
                If False = fileSavePostNotify Then
                    MsgBox ("FileSavePostNotify event wasn't fired after saving the '" & docName & "' document")
                End If
            End If
        Else
            MsgBox ("OpenDocument method returns Nothing for the '" & docName & "' document.")
        End If
    End Sub
    Public Sub CloseAllDocuments()
```

```
        Dim dsDocs As Variant
        Dim index As Long
        Dim pathName As String
```

```
        'Get documents
        dsDocs = dsApp.GetDocuments
        If IsArray(dsDocs) Then
            For index = LBound(dsDocs) To UBound(dsDocs)
                Set dsDoc = dsDocs(index)
                pathName = dsDoc.GetPathName
                dsApp.CloseDocument pathName, False
                If False = docDestroyNotify Then
                    MsgBox ("DestroyNotify event wasn't fired after closing a document.")
                End If
            Next
        End If
    End Sub
```

```
'Class1 module
Option Explicit
```

```
Public WithEvents app As DraftSight.Application
```

```
    Public Sub app_FileOpenPostNotify(ByVal doc As DraftSight.Document)
        filePostOpenNotify = True
        MsgBox ("FileOpenPostNotify event was fired while opening a document.")
    End Sub
```

```
    Public Sub app_FileOpenPreNotify(ByVal fileName As String, ByVal appOption As dsDocumentOpenOption_e)
        filePreOpenNotify = True
        MsgBox ("FileOpenPreNotify event was fired while opening a document.")
    End Sub
```

```
'Class2 module
Option Explicit
```

```
Public WithEvents doc As DraftSight.Document

    Public Sub doc_DestroyNotify()
        docDestroyNotify = True
        MsgBox ("DestroyNotify event was fired after closing a document.")
    End Sub
    Public Sub doc_FileSavePostNotify()
        fileSavePostNotify = True
        MsgBox ("FileSavePostNotify event was fired after saving the '" & docName & "' document")
    End Sub
    Public Sub doc_FileSavePreNotify(ByVal fileName As String, ByVal saveOption As dsDocumentSaveAsOption_e)
        fileSavePreNotify = True
        MsgBox ("FileSavePreNotify event was fired after saving the '" & fileName & "' document")
    End Sub
    Public Sub doc_ModifyNotify()
        fileModifyNotify = True
        MsgBox ("ModifyNotify event was fired while inserting a picture in document.")
    End Sub
```
