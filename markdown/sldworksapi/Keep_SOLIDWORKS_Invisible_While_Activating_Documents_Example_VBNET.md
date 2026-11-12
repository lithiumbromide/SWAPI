---
title: "Keep SOLIDWORKS Design Invisible While Activating Documents Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VBNET.htm"
---

# Keep SOLIDWORKS Design Invisible While Activating Documents Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
 Partial Class SolidWorksMacro

     Public swModel As ModelDoc2
     Public swExtension As ModelDocExtension

     Public Sub main()

         Dim pFrame As Frame
         Dim Document As String
         Dim Output As String

         On Error GoTo Fail

         ' Allow SOLIDWORKS Design to run in the background
         ' and be invisible
         swApp.UserControl = False

         ' If the following property is true, then the
         ' SOLIDWORKS Design frame will be visible on a call to
         ' ISldWorks::ActivateDoc2; so, set it to false
         swApp.Visible = False

         ' Keep SOLIDWORKS Design frame invisible when
         ' ISldWorks::ActivateDoc2 is called
         pFrame = swApp.Frame
         pFrame.KeepInvisible = True

         Document = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\blade shaft.sldasm"
         Output = "c:\temp\"

         Debug.Print("--- Save files as PDF ---")
         SaveToPDF(Document, Output)
         swApp.CloseAllDocuments(True)
         Debug.Print("--- Done ---")

         ' Show SOLIDWORKS Design frame and SOLIDWORKS Design
         pFrame.KeepInvisible = False
         swApp.Visible = True
         Exit Sub
 Fail:
         Debug.Print("Execution failed with error " & Err.Number & ": '" & Err.Description & "'")

     End Sub

     Private Sub SaveToPDF(ByVal docFileName As String, ByVal outputpath As String)
         Dim swAssembly As AssemblyDoc
         Dim doctype As Integer
         Dim errors As Integer
         Dim warnings As Integer
         Dim modelpath As String = ""
         Dim modelFileName As String = ""
         Dim convFileName As String = ""
         Dim Success As Boolean
         Dim vComponents As Object
         Dim i As Integer

         ' Determine the type of SOLIDWORKS Design file based on
         ' its filename extension
         If LCase(Right(docFileName, 7)) = ".sldprt" Then
             doctype = swDocumentTypes_e.swDocPART
         ElseIf LCase(Right(docFileName, 7)) = ".sldasm" Then
             doctype = swDocumentTypes_e.swDocASSEMBLY
         ElseIf LCase(Right(docFileName, 7)) = ".slddrw" Then
             doctype = swDocumentTypes_e.swDocDRAWING
         Else
             doctype = swDocumentTypes_e.swDocNONE
         End If

         ' Open document
         swModel = swApp.OpenDoc6(docFileName, doctype, swOpenDocOptions_e.swOpenDocOptions_Silent Or swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", errors, warnings)
         If swModel Is Nothing Then
             Debug.Print("Failed to open document " + modelpath + ". Errors: " & errors)
         End If

         ' Activate the document, which should remain invisible
         ' due to earlier call to IFrame::KeepInvisible
         swModel = swApp.ActivateDoc2(docFileName, True, errors)

         ' Build destination filename
         modelpath = swModel.GetPathName()
         modelFileName = Mid(modelpath, InStrRev(modelpath, "\") + 1)
         modelFileName = Left(modelFileName, InStrRev(modelFileName, ".") - 1)
         convFileName = outputpath + modelFileName + ".pdf"

         ' Save document as PDF
         swExtension = swModel.Extension
         Success = swExtension.SaveAs(convFileName, swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)
         If Success Then
             Debug.Print("Document, " + modelpath + ", saved as " + convFileName + ". ")
         Else
             Debug.Print("Document not saved: ")
             Debug.Print("  Errors: " & errors + modelpath + " as " + convFileName + ". ")
         End If

         ' Process all components
         If doctype = swDocumentTypes_e.swDocASSEMBLY Then
             swAssembly = swModel
             vComponents = swAssembly.GetComponents(True)
             For i = 0 To UBound(vComponents)
                 Dim swComponent As Component2
                 swComponent = vComponents(i)
                 SaveToPDF(swComponent.GetPathName(), outputpath)
             Next i
         End If

     End Sub

    ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

End Class
```
