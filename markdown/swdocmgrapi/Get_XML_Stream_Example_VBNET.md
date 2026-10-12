---
title: "Get XML Stream Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_XML_Stream_Example_VBNET.htm"
---

# Get XML Stream Example (VB.NET)

This example shows how to get an embedded XML stream in a SOLIDWORKS document using the SOLIDWORKS Document Manager API.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API
 '    Getting Started topic and ensure that the required
 '    DLLs have been registered.
 ' 2. Copy and paste this module into a VB.NET console
 '    application in Microsoft Visual Studio.
 ' 3. Ensure that the specified document exists
 '    (or point to another document).
 ' 4. Add the SolidWorks.Interop.swdocumentmgr.dll
 '    reference to the project:
 '    a. Right-click the solution in Solution Explorer.
 '    b. Click Add Reference.
 '    c. Click Browse.
 '    d. Click:
 '       install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 ' 5. Substitute your_license_code with your
 '    SOLIDWORKS Document Manager license key.
 '
 ' Postconditions: Locate the XML stream in the current directory.
 '----------------------------------------------------------------------------

 Imports SolidWorks.Interop.swdocumentmgr
 Module Module1

     Sub main()

         Const sLicenseKey As String = "your_license_code" 'Specify your license key
         Const sDocFileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\EDraw\claw\claw-mechanism.sldasm"

         Dim swClassFact As SwDMClassFactory
         Dim swDocMgr As SwDMApplication
         Dim swDoc As SwDMDocument
         Dim nDocType As Integer
         Dim sPathName As String
         Dim nRetVal As Integer
         Dim nRetVal2 As Integer

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

         ' Strip off SOLIDWORKS file extension (sldxxx)
         ' and add XML extension (xml)

         sPathName = Left(sDocFileName, Len(sDocFileName) - 6)
         sPathName = sPathName + "xml"

         swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
         swDocMgr = swClassFact.GetApplication(sLicenseKey)
         swDoc = swDocMgr.GetDocument(sDocFileName, nDocType,  False, nRetVal)

         swDoc.GetXmlStream(sPathName, nRetVal)

     End Sub

 End Module
```
