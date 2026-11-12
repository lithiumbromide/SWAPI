---
title: "Open Document Silently Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Document_Silently_Example_VB.htm"
---

# Open Document Silently Example (VBA)

This example shows how to open a document silently; that is, without dialog boxes.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the document specified to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified document silently (i.e., no dialogs
'    are displayed).
' 2. Examine the Immediate window.
'-----------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Const sDocFileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt"
     Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.modelDoc
     Dim nDocType As Long
     Dim nErrors As Long
     Dim nWarnings As Long
    Set swApp = CreateObject("SldWorks.Application")
    ' Determine type of SOLIDWORKS Design file based on file extension
     If InStr(LCase(sDocFileName), "sldprt") > 0 Then
         nDocType = swDocPART
     ElseIf InStr(LCase(sDocFileName), "sldasm") > 0 Then
         nDocType = swDocASSEMBLY
     ElseIf InStr(LCase(sDocFileName), "slddrw") > 0 Then
         nDocType = swDocDRAWING
     Else
         ' Probably not a SOLIDWORKS file
         nDocType = swDocNONE
         ' So cannot open the file
         Exit Sub
     End If
    Set swModel = swApp.OpenDoc6(sDocFileName, nDocType, swOpenDocOptions_Silent, "", nErrors, nWarnings)
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Error  (0 = no errors)  = " & nErrors
    Debug.Print "  Warnings (2 = document is read-only) = " & nWarnings
End Sub
```
