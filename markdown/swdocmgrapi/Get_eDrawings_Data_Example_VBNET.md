---
title: "Get eDrawings Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_eDrawings_Data_Example_VBNET.htm"
---

# Get eDrawings Data Example (VB.NET)

This example shows how to get eDrawings data from a SOLIDWORKS document using the SOLIDWORKS Document Manager API.

**NOTE**: ISwDMDocument::GetEDrawingsData is obsolete as of SOLIDWORKS Document Manager API 2005 FCS and has not been superseded.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Read the SOLIDWORKS Document Manager API
**' Getting Started** topic and ensure that the
' required DLLs have been registered.
' 2. Copy and paste this module into a VB.NET
' console application in Microsoft Visual Studio.
' 3. Ensure that the specified document exists
' (or point to another document that contains
' eDrawings data).
' 4. Add the **SolidWorks.Interop.swdocumentmgr.dll**
' reference to the project:
' a. Right-click the solution in Solution
' Explorer.
' b. Click **Add Reference**.
' c. Click **Browse**.
' d. Click:
' `install_dir`**\api\redist\SolidWorks.Interop.swdocumentmgr.dll**
' 5. Substitute `your_license_code` with your
' SOLIDWORKS Document Manager license key.
' 6. Compile and run this program in Debug mode.
'
' Postconditions:
' 1. Inspect the error code in the Output window.
' 2. The eDrawings data is extracted to a temp file in **c:\temp**.
'----------------------------------------------------------------------------

Imports SolidWorks.Interop.swdocumentmgr
Module Module1

Sub main()

Const sLicenseKey As String = "`your_license_code`" 'Specify your license key
Const sDocFileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\EDraw\claw\claw-mechanism.sldasm"

Dim swClassFact As SwDMClassFactory
Dim swDocMgr As SwDMApplication
Dim swDoc As SwDMDocument
Dim nDocType As Integer
Dim sEdrawExt As String
Dim nRetVal As SwDmEDwgDataError

' Determine type of SOLIDWORKS file based on file extension
If InStr(LCase(sDocFileName), "sldprt") > 0 Then
nDocType = SwDmDocumentType.swDmDocumentPart
sEdrawExt = "eprt"
ElseIf InStr(LCase(sDocFileName), "sldasm") > 0 Then
nDocType = SwDmDocumentType.swDmDocumentAssembly
sEdrawExt = "easm"
ElseIf InStr(LCase(sDocFileName), "slddrw") > 0 Then
nDocType = SwDmDocumentType.swDmDocumentDrawing
sEdrawExt = "edrw"
Else

' Probably not a SOLIDWORKS file
nDocType = SwDmDocumentType.swDmDocumentUnknown
sEdrawExt = ""

' so cannot open
Exit Sub
End If

swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
swDocMgr = swClassFact.GetApplication(sLicenseKey)
swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, False, nRetVal) : Debug.Assert(SwDmDocumentOpenError.swDmDocumentOpenErrorNone = nRetVal)

' Copy eDrawings data to file with eDrawings extension
nRetVal = swDoc.**GetEDrawingsData**("c:\temp\temp." & sEdrawExt)
Debug.Print("EDrawing error code: " & nRetVal)

End Sub
End Module
