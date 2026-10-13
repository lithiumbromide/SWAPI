---
title: "Copy Document and Its Dependencies Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Document_and_Its_Dependencies_Example_VBNET.htm"
---

# Copy Document and Its Dependencies Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

	Sub main()

		Dim source As String
		Dim target As String
		Dim sourcefile As String
		Dim traverse As Boolean
		Dim search As Boolean
		Dim addreadonlyinfo As Boolean
		Dim depends As Object
		Dim sourcefiles() As String = Nothing
		Dim targetfiles() As String = Nothing
		Dim idx As Integer
		Dim sourcecount As Integer
		Dim copyopt As Integer
		Dim errors As Integer
		Dim doc As ModelDoc2

		doc = swApp.ActiveDoc

		source = swApp.GetCurrentWorkingDirectory
		sourcefile = doc.GetPathName

		target = swApp.GetCurrentMacroPathName
		target = Left(target, InStrRev(target, "\"))

		traverse = True
		search = True
		addreadonlyinfo = False
		depends = swApp.GetDocumentDependencies2(sourcefile, traverse, search, addreadonlyinfo)

		If IsNothing(depends) Then Exit Sub

	   	idx = 1
	   	While idx <= UBound(depends)
	       		ReDim Preserve sourcefiles(sourcecount)
	       		ReDim Preserve targetfiles(sourcecount)

	       		sourcefiles(sourcecount) = depends(idx)
	       		targetfiles(sourcecount) = target + Right(sourcefiles(sourcecount), Len(sourcefiles(sourcecount)) - InStrRev(sourcefiles(sourcecount), "\"))
	       		sourcecount = sourcecount + 1
	       		idx = idx + 2
	   	End While

	   	swApp.CloseAllDocuments(True)

	   	copyopt = swMoveCopyOptions_e.swMoveCopyOptionsOverwriteExistingDocs
	   	errors = swApp.CopyDocument(source + sourcefile, target + sourcefile, (sourcefiles), (targetfiles), copyopt)

	End Sub

	Public swApp As SldWorks

End Class
```
