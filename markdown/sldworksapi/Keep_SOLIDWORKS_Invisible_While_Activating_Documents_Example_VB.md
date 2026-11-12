---
title: "Keep SOLIDWORKS Design Invisible While Activating Documents Example VB"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VB.htm"
---

# Keep SOLIDWORKS Design Invisible While Activating Documents Example VB

## Keep SOLIDWORKS Design Invisible While Activating Documents Example (VBA)

This example shows how to keep SOLIDWORKS Design invisible while activating SOLIDWORKS Design documents, including assembly component files, and saving those documents as PDF files.

```
'------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly file exists.
' 2. Verify that c:\temp exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Saves the specified assembly file and its
'    component files as PDF files to the c:\temp.
' 2. Examine the Immediate window and c:\temp.
'--------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swExtension As SldWorks.ModelDocExtension
 Dim swAssembly As SldWorks.AssemblyDoc
 Dim doctype As Long
 Dim errors As Long
 Dim warnings As Long
 Dim modelpath As String
 Dim modelFileName As String
 Dim convFileName As String
 Dim Success As Boolean
 Dim vComponents As Variant
 Dim i As Long
 Dim outputpath As String

Sub SaveToPDF(docFileName As String, outputpath As String)
     ' Determine the type of SOLIDWORKS Design file based on
     ' its filename extension
     If LCase(Right(docFileName, 7)) = ".sldprt" Then
         doctype = swDocPART
     ElseIf LCase(Right(docFileName, 7)) = ".sldasm" Then
         doctype = swDocASSEMBLY
     ElseIf LCase(Right(docFileName, 7)) = ".slddrw" Then
         doctype = swDocDRAWING
     Else
         doctype = swDocNONE
     End If

    ' Open document
     Set swModel = swApp.OpenDoc6(docFileName, doctype, swOpenDocOptions_Silent Or swOpenDocOptions_ReadOnly, "", errors, warnings)
     If swModel Is Nothing Then
         Debug.Print "Failed to open document " + modelpath + ". Errors: " & errors
     End If

    ' Activate the document, which should remain invisible
     ' due to earlier call to IFrame::KeepInvisible
     Set swModel = swApp.ActivateDoc2(docFileName, True, errors)

    ' Build destination file name
     modelpath = swModel.GetPathName()
     modelFileName = Mid(modelpath, InStrRev(modelpath, "\") + 1)
     modelFileName = Left(modelFileName, InStrRev(modelFileName, ".") - 1)
     convFileName = outputpath + modelFileName + ".pdf"

     ' Save document as PDF
     Set swExtension = swModel.Extension
     Success = swExtension.SaveAs(convFileName, swSaveAsCurrentVersion, swSaveAsOptions_Silent, Nothing, errors, warnings)

    If Success Then
        Debug.Print "Document, " + modelpath + ", saved as " + convFileName + ". "
     Else
        Debug.Print "Document not saved: "
        Debug.Print "  Errors: " & errors + modelpath + " as " + convFileName + ". "
     End If

    ' Process all components
     If doctype = swDocASSEMBLY Then
         Set swAssembly = swModel
         vComponents = swAssembly.GetComponents(True)
         For i = 0 To UBound(vComponents)
             Dim swComponent As SldWorks.Component2
             Set swComponent = vComponents(i)
             SaveToPDF swComponent.GetPathName(), outputpath
         Next i
     End If
End Sub

Sub main()
    On Error GoTo Fail:

     ' Get SOLIDWORKS Design
     Set swApp = Application.SldWorks

     ' Allow SOLIDWORKS Design to run in the background
     ' and be invisible
     swApp.UserControl = False

     ' If the following property is true, then the
     ' SOLIDWORKS Design frame will be visible on a call to
     ' ISldWorks::ActivateDoc2; so set it to false
     swApp.visible = False

    ' Keep SOLIDWORKS Design frame invisible when
     ' ISldWorks::ActivateDoc2 is called
     Dim pFrame As Frame
     Set pFrame = swApp.Frame
     pFrame.KeepInvisible = True

     Dim Document As String
     Dim Output As String
     Document = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\blade shaft.sldasm"
     Output = "c:\temp\"

    Debug.Print "--- Save files as PDF ---"
     SaveToPDF Document, Output
     swApp.CloseAllDocuments True
     Debug.Print "--- Done ---"

     ' Show SOLIDWORKS Design frame and SOLIDWORKS Design
     pFrame.KeepInvisible = False
     swApp.visible = True
     Exit Sub

Fail:
     Debug.Print "Execution failed with error " & Err.Number & ": '" & Err.Description & "'"

End Sub
```
