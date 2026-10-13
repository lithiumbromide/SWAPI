---
title: "Get Version History of Future Version Document Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Version_History_of_Future_Version_Document_Example_VBNET.htm"
---

# Get Version History of Future Version Document Example (VB.NET)

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
 ' 1. Does no throw swFileLoadError_e.swFutureVersion.
 ' 2. Inspect the Immediate window for the version history of the document.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub Main()

         Dim swDocument As ModelDoc2
         Dim swExtension As ModelDocExtension
         Dim lErrors As Integer
         Dim lWarnings As Integer
         Dim lOptions As Integer
         Dim strFileName As String
         Dim vVersionHistory As Object
         Dim strBaseVersion As String = Nothing
         Dim strCurrentVersion As String = Nothing
         Dim strHotFixes As String = Nothing
         Dim strRevisionNumber As String
         Dim lDateCode As Integer
         Dim strDateCode As String
         Dim strDateCodeYear As String
         Dim strDateCodeDay As String
         Dim strFormatVersion As String

         strFormatVersion = swApp.GetLatestSupportedFileVersion

         strRevisionNumber = swApp.RevisionNumber
         swApp.GetBuildNumbers2(strBaseVersion, strCurrentVersion, strHotFixes)
         lDateCode = swApp.DateCode

         strDateCode = CStr(lDateCode)
         strDateCodeYear = Left$(strDateCode, 4)
         strDateCodeDay = Mid$(strDateCode, Len(strDateCodeYear) + 1)

         strDateCode = strDateCodeYear   "/" & strDateCodeDay

         Debug.Print("Format version = " & strFormatVersion)
         Debug.Print("RevisionNumber = " & strRevisionNumber)
         Debug.Print("BaseVersion    = " & strBaseVersion)
         Debug.Print("CurrentVersion = " & strCurrentVersion)
         Debug.Print("HotFixes       = " & strHotFixes)
         Debug.Print("DateCode       = " & lDateCode)
         Debug.Print("  DateCode     = " & strDateCode)

         swDocument = swApp.ActiveDoc

         If (swDocument Is Nothing) Then
             strFileName = swApp.GetCurrentMacroPathFolder & "\Part1.sldprt"
             lOptions = 0
             lOptions = lOptions Or swOpenDocOptions_e.swOpenDocOptions_Silent
             swDocument = swApp.OpenDoc6(strFileName, swDocumentTypes_e.swDocPART, lOptions, "", lErrors, lWarnings)
             Debug.Print("lErrors = " & lErrors)

             ' Starting with SW2012 SP5, loading future file versions
             ' is supported, so the future version error no longer occurs.
             Debug.Print("  future version error = " & ((lErrors  And swFileLoadError_e.swFutureVersion) = swFileLoadError_e.swFutureVersion))
             Debug.Print("lWarnings = " & lWarnings)
         End If

         If (swDocument Is Nothing) Then
             Debug.Print("No model")
             Exit Sub
         End If

         strFileName = swDocument.GetPathName
         Debug.Print("File = " & strFileName)
         swExtension = swDocument.Extension

         ' The version history of a future version document is the same
         ' as that of the part/assembly template that is used to load it
         ' into the older version of SOLIDWORKS Design. IModelDoc2::VersionHistory
         ' returns the version history of the part template,
         ' not the version history of the future version document.
         ' Get the version history of a future version document from its file
         ' on disk using SldWorks::VersionHistory.

         Debug.Print("Is future version = " & swExtension.IsFutureVersion)

         If (Not (swExtension.IsFutureVersion = False)) Then
             vVersionHistory = swApp.VersionHistory(strFileName)
             If (Not IsNothing(vVersionHistory)) Then
                 Debug.Print("Version history from file:")
                 PrintVersionHistory(vVersionHistory)
             End If
         End If

         vVersionHistory = swDocument.VersionHistory

         If (Not IsNothing(vVersionHistory)) Then
             Debug.Print("Version history from document:")
             PrintVersionHistory(vVersionHistory)
         End If

         Debug.Print("view-only      = " & swDocument.IsOpenedViewOnly)
         Debug.Print("read-only      = " & swDocument.IsOpenedReadOnly)
         Debug.Print("blocking state = " & BlockingState2String(swDocument.GetBlockingState))

     End Sub

     Private Sub PrintVersionHistory(ByVal vVersionHistory As Object)

         Dim vSplitResults As Object
         Dim strFormatVersion As String
         Dim strDateCodes As String
         Dim vDateCode As Object
         Dim vHistoryEntry As Object

         For Each vHistoryEntry In vVersionHistory

             Debug.Print("  " & vHistoryEntry)
             vSplitResults = Split(vHistoryEntry,  "[")
             strFormatVersion = vSplitResults(0)
             strDateCodes = Replace(vSplitResults(1),  "]",  "")
             vSplitResults = Split(strDateCodes,  ",")
             Debug.Print("    format version = " & strFormatVersion)

             For Each vDateCode In vSplitResults
                 Debug.Print("       datecode = " & vDateCode)
             Next vDateCode

         Next vHistoryEntry

     End Sub

     Private Function BlockingState2String(ByVal nBlockingState As swBlockingStates_e) As String

         Select Case (nBlockingState)
             Case swBlockingStates_e.swEditorBlock
                 BlockingState2String =  "editor block"

             Case swBlockingStates_e.swEditSketchBlock
                 BlockingState2String =  "edit sketch block"

             Case swBlockingStates_e.swFullBlock
                 BlockingState2String =  "full block"

             Case swBlockingStates_e.swModifyBlock
                 BlockingState2String =  "modify block"

             Case swBlockingStates_e.swNoBlock
                 BlockingState2String =  "no block"

             Case swBlockingStates_e.swPartialModifyBlock
                 BlockingState2String =  "partial modify block"

             Case swBlockingStates_e.swSystemBlock
                 BlockingState2String =  "system block"

             Case swBlockingStates_e.swViewOnlyBlock
                 BlockingState2String =  "view only block"

             Case Else
                 BlockingState2String = "<unknown blocking state>"

         End Select

     End Function

     Public swApp As SldWorks

 End  Class
```
