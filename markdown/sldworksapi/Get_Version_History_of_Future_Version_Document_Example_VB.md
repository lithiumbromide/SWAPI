---
title: "Get Version History of Future Version Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Version_History_of_Future_Version_Document_Example_VB.htm"
---

# Get Version History of Future Version Document Example (VBA)

This example shows how to get the version history of a future version document.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Copy a future version part document to this macro's directory.
 ' 2. Replace Part1.sldprt in the macro with the name
 '    of your future version part.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Does not throw swFileLoadError_e.swFutureVersion.
 ' 2. Inspect the Immediate window for the version history of the document.
 ' ---------------------------------------------------------------------------
Option Explicit
Sub Main()
    Dim swApp As SldWorks.SldWorks
     Dim swDocument As SldWorks.ModelDoc2
     Dim swExtension As SldWorks.ModelDocExtension
     Dim lErrors As Long
     Dim lWarnings As Long
     Dim lOptions As Long
     Dim strFileName As String
     Dim vVersionHistory As Variant
     Dim strBaseVersion As String
     Dim strCurrentVersion As String
     Dim strHotFixes As String
     Dim strRevisionNumber As String
     Dim lDateCode As Long
     Dim strDateCode As String
     Dim strDateCodeYear As String
     Dim strDateCodeDay As String
     Dim strFormatVersion As String

    Set swApp = Application.SldWorks

    strFormatVersion = swApp.GetLatestSupportedFileVersion

    strRevisionNumber = swApp.RevisionNumber
     swApp.GetBuildNumbers2 strBaseVersion, strCurrentVersion, strHotFixes
     lDateCode = swApp.DateCode

    strDateCode = CStr(lDateCode)
     strDateCodeYear = Left$(strDateCode, 4)
     strDateCodeDay = Mid$(strDateCode, Len(strDateCodeYear) + 1)

    strDateCode = strDateCodeYear & "/" & strDateCodeDay

    Debug.Print "Format version = " & strFormatVersion
     Debug.Print "RevisionNumber = " & strRevisionNumber
     Debug.Print "BaseVersion    = " & strBaseVersion
     Debug.Print "CurrentVersion = " & strCurrentVersion
     Debug.Print "HotFixes       = " & strHotFixes
     Debug.Print "DateCode       = " & lDateCode
     Debug.Print "  DateCode     = " & strDateCode

    Set swDocument = swApp.ActiveDoc

    If (swDocument Is Nothing) Then
         strFileName = swApp.GetCurrentMacroPathFolder & "\Part1.sldprt"
         lOptions = 0
         lOptions = lOptions Or swOpenDocOptions_e.swOpenDocOptions_Silent
         Set swDocument = swApp.OpenDoc6(strFileName, swDocPART, lOptions, "", lErrors, lWarnings)
         Debug.Print "lErrors = " & lErrors

         ' Starting with SW2012 SP5, loading future file versions is supported,
         ' so the future version error no longer occurs.
         Debug.Print "  future version error = " & ((lErrors And swFileLoadError_e.swFutureVersion) = swFileLoadError_e.swFutureVersion)
         Debug.Print "lWarnings = " & lWarnings
     End If

    If (swDocument Is Nothing) Then
         Debug.Print "No model"
         Exit Sub
     End If

    strFileName = swDocument.GetPathName
     Debug.Print "File = " & strFileName
     Set swExtension = swDocument.Extension

    ' The version history of a future version document is the same as
     ' that of the part/assembly template that is used to load it
     ' into the older version of SOLIDWORKS Design. IModelDoc2::VersionHistory
     ' returns the version history of the part template,
     ' not the version history of the future version document. Get the version
     ' history of a future version document from its file on disk
     ' using SldWorks::VersionHistory.

    Debug.Print "Is future version = " & swExtension.IsFutureVersion

    If (Not (swExtension.IsFutureVersion = False)) Then
         vVersionHistory = swApp.VersionHistory(strFileName)
         If (Not IsEmpty(vVersionHistory)) Then
             Debug.Print "Version history from file:"
             PrintVersionHistory vVersionHistory
         End If
     End If

    vVersionHistory = swDocument.VersionHistory

    If (Not IsEmpty(vVersionHistory)) Then
         Debug.Print "Version history from document:"
         PrintVersionHistory vVersionHistory
     End If

    Debug.Print "view-only      = " & swDocument.IsOpenedViewOnly
     Debug.Print "read-only      = " & swDocument.IsOpenedReadOnly
     Debug.Print "blocking state = " & BlockingState2String(swDocument.GetBlockingState)

End Sub
Private Sub PrintVersionHistory(ByVal vVersionHistory As Variant)
    Dim vSplitResults           As Variant
     Dim strFormatVersion        As String
     Dim strDateCodes            As String
     Dim vDateCode               As Variant
     Dim vHistoryEntry           As Variant
    For Each vHistoryEntry In vVersionHistory

        Debug.Print "  " & vHistoryEntry
         vSplitResults = Split(vHistoryEntry, "[")
         strFormatVersion = vSplitResults(0)
         strDateCodes = Replace(vSplitResults(1), "]", "")
         vSplitResults = Split(strDateCodes, ",")
         Debug.Print "    format version = " & strFormatVersion

        For Each vDateCode In vSplitResults
             Debug.Print "       datecode = " & vDateCode
         Next vDateCode

    Next vHistoryEntry
End Sub
Private Function BlockingState2String(ByVal nBlockingState As SwConst.swBlockingStates_e) As String
    Select Case (nBlockingState)
         Case swBlockingStates_e.swEditorBlock
             BlockingState2String = "editor block"

        Case swBlockingStates_e.swEditSketchBlock
             BlockingState2String = "edit sketch block"

        Case swBlockingStates_e.swFullBlock
             BlockingState2String = "full block"

        Case swBlockingStates_e.swModifyBlock
             BlockingState2String = "modify block"

        Case swBlockingStates_e.swNoBlock
             BlockingState2String = "no block"

        Case swBlockingStates_e.swPartialModifyBlock
             BlockingState2String = "partial modify block"

        Case swBlockingStates_e.swSystemBlock
             BlockingState2String = "system block"

        Case swBlockingStates_e.swViewOnlyBlock
             BlockingState2String = "view only block"

        Case Else
             BlockingState2String = "<unknown blocking state>"

    End Select

End Function
```
