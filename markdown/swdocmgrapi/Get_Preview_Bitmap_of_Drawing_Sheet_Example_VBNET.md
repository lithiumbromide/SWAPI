---
title: "Get Preview Bitmap of Drawing Sheet Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Preview_Bitmap_of_Drawing_Sheet_Example_VBNET.htm"
---

# Get Preview Bitmap of Drawing Sheet Example (VB.NET)

This example shows how to get a BMP preview bitmap of the sheet that was active when the drawing was last saved.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Read the SOLIDWORKS Document Manager API Getting Started topic
'    and verify that the required DLLs are registered.
' 2. Create a VB.NET application in Microsoft Visual Studio.
' 3. Copy Module1 into Module1.vb.
'    a. Specify your_license_key.
'    b. Verify that the specified file to open exists.
'    c. Add a reference to SolidWorks.Interop.swdocumentmgr.dll:
'       1. Right-click the solution in the Solution Explorer.
'       2. Click Add Reference.
'       3. Click Browse.
'       4. Click install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll.
'    d. Add references to System.Windows.Forms, System.Drawing, and stdole.
' 4. Create a class and copy Class1 into Class1.vb.
' 5. Verify that c:\temp exists.
' 6. Open the Immediate Window.
'
' Postconditions:
' 1. Creates a preview bitmap of the sheet active when the drawing was last saved.
' 2. Right-click c:\temp\foodprocessor.bmp and click Preview.
' 3. Examine the Immediate Window.
'---------------------------------------------------------------------------
'Module1
```

```
Imports SolidWorks.Interop.swdocumentmgr
Imports System.Drawing
Imports stdole
Imports System
Imports System.Diagnostics
Imports System.Windows.Forms

Module Module1

    Sub Main()

        Const sLicenseKey As String = "your_license_key"
        Const sDocFileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
        Const sExtractDir As String = "c:\temp\"
        Const sFilename As String = "foodprocessor"
        Dim swClassFact As SwDMClassFactory
        Dim swDocMgr As SwDMApplication
        Dim swDoc As SwDMDocument
        Dim swDoc10 As SwDMDocument10
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
            ' Probably not a SOLIDWORKS file,
            ' so cannot open
            nDocType = SwDmDocumentType.swDmDocumentUnknown
            Exit Sub
        End If

        swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
        swDocMgr = swClassFact.GetApplication(sLicenseKey)
        swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, True, nRetVal)
        Debug.Print("File = " & swDoc.FullName)
        Debug.Print("  Version          = " & swDoc.GetVersion)
        Debug.Print("  Author           = " & swDoc.Author)
        Debug.Print("  Comments         = " & swDoc.Comments)
        Debug.Print("  CreationDate     = " & swDoc.CreationDate)
        Debug.Print("  Keywords         = " & swDoc.Keywords)
        Debug.Print("  LastSavedBy      = " & swDoc.LastSavedBy)
        Debug.Print("  LastSavedDate    = " & swDoc.LastSavedDate)
        Debug.Print("  Subject          = " & swDoc.Subject)
        Debug.Print("  Title            = " & swDoc.Title)

        swDoc10 = swDoc
        Dim objBitMap As Object = swDoc10.GetPreviewBitmap(nRetVal)
        Dim imgPreview As System.Drawing.Image = PictureDispConverter.Convert(objBitMap)
        imgPreview.Save(sExtractDir + sFilename + ".bmp", Drawing.Imaging.ImageFormat.Bmp)
        imgPreview.Dispose()

        Debug.Print("    Preview stream   = " & swDoc10.PreviewStreamName)
    End Sub

End Module

'Class1
Public Class PictureDispConverter

    Inherits System.Windows.Forms.AxHost

    Public Sub New()
        MyBase.New("56174C86-1546-4778-8EE6-B6AC606875E7")
    End Sub

    Public Shared Function Convert(ByVal objIDispImage As Object) As System.Drawing.Image
        Dim objPicture As System.Drawing.Image
        objPicture = CType(System.Windows.Forms.AxHost.GetPictureFromIPicture(objIDispImage), System.Drawing.Image)
        Return objPicture
    End Function

End Class
```
