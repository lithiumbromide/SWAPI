---
title: "Open Document Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Document_Example_VBNET.htm"
---

# Open Document Example (VB.NET)

This example shows how to programmatically open a document and set the SOLIDWORKS Design working directory.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified document.
' 2. Sets the SOLIDWORKS Design working directory to the document directory.
' 3. Examine the Immediate window.
'---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim doc As ModelDoc2

	    Dim fileerror As Integer

	    Dim filewarning As Integer

	    Sub main()

	        swApp.Visible = True

	        '
	Get the current working directory before opening the document

	        Debug.Print("Current working directory is " & swApp.GetCurrentWorkingDirectory)

	        doc = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\chair.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", fileerror, filewarning)

	        ' Opening a document with SldWorks::OpenDoc6
	does not set the working directory

	        Debug.Print("Current working directory is still " & swApp.GetCurrentWorkingDirectory)

	        ' Set the working directory to the
	document directory

	        swApp.SetCurrentWorkingDirectory(Left(doc.GetPathName, InStrRev(doc.GetPathName, "\")))

	        Debug.Print("Current working
	directory is now " & swApp.GetCurrentWorkingDirectory)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
