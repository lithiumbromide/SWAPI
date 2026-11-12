---
title: "Copy Document and Its Dependencies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Document_and_Its_Dependencies_Example_VB.htm"
---

# Copy Document and Its Dependencies Example (VBA)

This example shows how to copy a document and its dependencies to this macro's folder.

```
'---------------------------------------------------------------------------
' Preconditions: Open an assembly document.
'
' Postconditions:
' 1. Closes the assembly document.
' 2. Copies the assembly document and its dependencies to the macro folder.
' 3. Examine the macro folder.
'---------------------------------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim source As String
     Dim target As String
     Dim sourcefile As String
     Dim traverse As Boolean
     Dim search As Boolean
     Dim addreadonlyinfo As Boolean
     Dim depends As Variant
     Dim sourcefiles() As String
     Dim targetfiles() As String
     Dim idx As Integer
     Dim sourcecount As Integer
     Dim copyopt As Long
     Dim errors As Long
     Dim doc As SldWorks.ModelDoc2

    Set swApp = Application.SldWorks
     Set doc = swApp.ActiveDoc

    source = swApp.GetCurrentWorkingDirectory
     sourcefile = doc.GetPathName

    target = swApp.GetCurrentMacroPathName
     target = Left(target, InStrRev(target, "\"))

    traverse = True
     search = True
     addreadonlyinfo = False

    depends = swApp.GetDocumentDependencies2(sourcefile, traverse, search, addreadonlyinfo)
    If IsEmpty(depends) Then Exit Sub

    idx = 1
     While idx <= UBound(depends)

        ReDim Preserve sourcefiles(sourcecount)
         ReDim Preserve targetfiles(sourcecount)

        sourcefiles(sourcecount) = depends(idx)
         targetfiles(sourcecount) = target + Right(sourcefiles(sourcecount), Len(sourcefiles(sourcecount)) - InStrRev(sourcefiles(sourcecount), "\"))

        sourcecount = sourcecount + 1
         idx = idx + 2
     Wend

    swApp.CloseAllDocuments True

    copyopt = SwConst.swMoveCopyOptions_e.swMoveCopyOptionsOverwriteExistingDocs
     errors = swApp.CopyDocument(source + sourcefile, target + sourcefile, (sourcefiles), (targetfiles), copyopt)
End Sub
```
