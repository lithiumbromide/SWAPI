---
title: "Get PNG Preview Bitmap and Stream for Configuration Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_PNG_Preview_Bitmap_and_Stream_for_Configuration_Example_VBNET.htm"
---

# Get PNG Preview Bitmap and Stream for Configuration Example (VB.NET)

This example shows how to get the name of the stream and the PNG preview bitmap for a configuration.

**NOTE**: To get the name of the stream and a preview bitmap of the sheet active when the drawing was last saved, use ISwDMDocument10::GetPreviewBitmap and ISwDMDocument10::PreviewStreamName. To get the name of the streams and the preview bitmaps for all sheets in a drawing, use ISwDMSheet2::GetPreviewPNGBitmap and ISwDMSheet2::PreviewPNGStreamName.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Read the SOLIDWORKS Document Manager API Getting Started topic
'    and verify that the required DLLs are registered.
' 2. Create a VB.NET console application in Microsoft Visual Studio.
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
' 5. Verify that C:\temp exists.
' 6. Open the Immediate Window.
'
' Postconditions:
' 1. Creates a preview bitmap of the Default configuration.
' 2. Right-click C:\temp\Default.PNG and click Preview.
' 3. Examine the Immediate Window.
'---------------------------------------------------------------------------
'Module1
Imports SolidWorks.Interop.swdocumentmgr
Imports System.Drawing.Image
Imports stdole
Imports System
Imports System.Diagnostics
```

```
Module Module1

    Sub Main()
        Const sDocFileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
        Dim swClassFact As SwDMClassFactory
        Dim swDocMgr As SwDMApplication
        Dim swDoc As SwDMDocument
        Dim swCfgMgr As SwDMConfigurationMgr
        Dim vCfgNameArr As Object
        Dim vCfgName As Object
        Dim swCfg As SwDMConfiguration7
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

        ' Because drawing documents do not have configurations,
        ' only continue running the macro if the document
        ' is a part or assembly document
        If (nDocType <> SwDmDocumentType.swDmDocumentDrawing) Then

            swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
            swDocMgr = swClassFact.GetApplication("your_license_key")
            swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, True, nRetVal)
            swCfgMgr = swDoc.ConfigurationManager

            Debug.Print("File = " & swDoc.FullName)
            Debug.Print("Active configuration name = " & swCfgMgr.GetActiveConfigurationName)
            vCfgNameArr = swCfgMgr.GetConfigurationNames

            For Each vCfgName In vCfgNameArr
                swCfg = swCfgMgr.GetConfigurationByName(vCfgName)
                Dim objBitMap As Object = swCfg.GetPreviewBitmap(nRetVal)
                Dim imgPreview As System.Drawing.Image = PictureDispConverter.Convert(objBitMap)
                imgPreview.Save("C:\\temp\\" + vCfgName + ".PNG", Drawing.Imaging.ImageFormat.Bmp)
                imgPreview.Dispose()

                Debug.Print("  " & vCfgName)
                Debug.Print("    PNG preview stream = " & swCfg.PreviewPNGStreamName)
                Debug.Print("  ")

            Next
            swDoc.CloseDoc()
        End If

    End Sub

End Module
```

```
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
