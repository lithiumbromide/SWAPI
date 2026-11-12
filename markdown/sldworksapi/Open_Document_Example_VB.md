---
title: "Open Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Document_Example_VB.htm"
---

# Open Document Example (VBA)

This example shows how to programmatically open a document and set the SOLIDWORKS Design working directory.

```vb
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
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim doc As SldWorks.ModelDoc2
 Dim fileerror As Long
 Dim filewarning As Long
Sub main()
    Set swApp = Application.SldWorks
     swApp.Visible = True

    ' Get the current working directory before opening the document
     Debug.Print "Current working directory is " & swApp.GetCurrentWorkingDirectory

    Set doc = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\chair.sldprt", swDocPART, swOpenDocOptions_Silent, "", fileerror, filewarning)

    ' Opening a document with SldWorks::OpenDoc6 does not set the working directory
     Debug.Print "Current working directory is still " & swApp.GetCurrentWorkingDirectory

    ' Set the working directory to the document directory
     swApp.SetCurrentWorkingDirectory (Left(doc.GetPathName, InStrRev(doc.GetPathName, "\")))

    Debug.Print "Current working directory is now " & swApp.GetCurrentWorkingDirectory
End Sub
```
