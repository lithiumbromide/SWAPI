---
title: "Get Hyperlinks Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Hyperlinks_Example_VBNET.htm"
---

# Get Hyperlinks Example (VB.NET)

This example shows how to get the hyperlinks for a SOLIDWORKS document using the SOLIDWORKS Document Manager API.

'---------------------------------------------------------------------------
' Preconditions:
' 1. Read the SOLIDWORKS Document Manager API
' **Getting Started** topic and ensure that
' the required DLLs have been registered.
' 2. Copy and paste this module into a VB.NET
' console application in Microsoft Visual Studio.
' 3. Add the **SolidWorks.Interop.swdocumentmgr.dll** reference to the project:
' a. Right-click the solution in Solution Explorer.
' b. Click **Add Reference**.
' c. Click **Browse**.
' d. Click:
' `install_dir`**\api\redist\SolidWorks.Interop.swdocumentmgr.dll**
' 4. Substitute `your_license_code` with your
' SOLIDWORKS Document Manager license key.
' 5. Substitute `model_with_hyperlinks` with the path to a model that
' contains one or more hyperlinks.
' 6. Compile and run this program in Debug mode.
'
' Postconditions: Inspect the Output window and the
' code to see how the API is used.
'--------------------------------------------------------------------------

Imports SolidWorks.Interop.swdocumentmgr
Module Module1

Sub ProcessDocHyperlinks(ByVal swDoc As SwDMDocument)

```vb
          Dim i As Integer
         Dim count As Integer = swDoc.GetHyperLinksCount

         If count > 0 Then
             Debug.Print("  Hyperlinks: " & count)
             For i = 0 To count - 1
                 Debug.Print("    " & swDoc.GetHyperLinkAt(i))
             Next
         Else
             Debug.Print("No hyperlinks detected.")
         End If

         Debug.Print("")

     End Sub

     Sub main()

         Const sLicenseKey As String = "your_license_code" 'Specify your license key
         Const sDocFileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\EDraw\claw\claw-mechanism.sldasm"

         Dim swClassFact As SwDMClassFactory
         Dim swDocMgr As SwDMApplication
         Dim swDoc As SwDMDocument
         Dim swCfgMgr As SwDMConfigurationMgr
         Dim nDocType As Integer
         Dim nRetVal As Integer

         ' Determine type of SOLIDWORKS file based on file extension
         If InStr(LCase(sDocFileName), "sldprt") > 0 Then
             nDocType = SwDmDocumentType.swDmDocumentPart
         ElseIf InStr(LCase(sDocFileName), "sldasm") > 0 Then
             nDocType = SwDmDocumentType.swDmDocumentAssembly
         ElseIf InStr(LCase(sDocFileName), "slddrw") > 0 Then
             nDocType = SwDmDocumentType.swDmDocumentDrawing
         Else

             ' Probably not a SOLIDWORKS file
             nDocType = SwDmDocumentType.swDmDocumentUnknown

             ' so cannot open
             Exit Sub
         End If

         swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
         swDocMgr = swClassFact.GetApplication(sLicenseKey)
         swDoc = swDocMgr.GetDocument(sDocFileName, nDocType,  False, nRetVal)
         swCfgMgr = swDoc.ConfigurationManager

         Debug.Print("File = " & swDoc.FullName)

         ProcessDocHyperlinks(swDoc)

     End Sub

 End Module
```
