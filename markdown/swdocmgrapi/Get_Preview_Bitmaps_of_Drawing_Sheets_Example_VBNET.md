---
title: "Get Preview Bitmaps of Drawing Sheets Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Preview_Bitmaps_of_Drawing_Sheets_Example_VBNET.htm"
---

# Get Preview Bitmaps of Drawing Sheets Example (VB.NET)

This example shows how to get PNG preview bitmaps of the sheets in a drawing document.

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
' 5. Verify that c:\temp exists.
' 6. Open the Immediate Window.
'
' Postconditions:
' 1. Creates preview bitmaps of the sheets in the drawing document.
' 2. Right-click each c:\temp\Sheetn.png and click Preview.
' 3. Examine the Immediate Window.
'---------------------------------------------------------------------------
'Module1
```

```
Imports System
Imports System.Diagnostics
Imports SolidWorks.Interop.swdocumentmgr
Imports System.Drawing
Imports stdole
Imports System.Windows.Forms

Module Module1

    Sub Main()

        Dim swClassFact As SwDMClassFactory
        Dim swDocMgr As SwDMApplication
        Dim swDoc As SwDMDocument10
        Dim sDocFileName As String
        Dim nDocType As SwDmDocumentType
        Dim nRetVal As SwDmDocumentOpenError
        Dim sLicenseKey As String

        ' Specify your license key
        sLicenseKey = "your_license_key"

        ' If the following drawing document does not exist,
        ' then substitute the name of a drawing document that does
        sDocFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
        nDocType = SwDmDocumentType.swDmDocumentDrawing

        swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
        swDocMgr = swClassFact.GetApplication(sLicenseKey)
        swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, True, nRetVal)
        If (swDoc Is Nothing) Then
            MsgBox("Unable to open document.")
        End If

        Dim Sheets As Object
        Dim Sheet As SwDMSheet2
        Dim nError As Integer
        Dim PreviewPNGByteArray As Object

        ' Get the sheets in the drawing document
        Sheets = swDoc.GetSheets
        Dim nbrSheets As Integer
        nbrSheets = CLng(UBound(Sheets)) + 1
        Dim snbrSheets As String = Convert.ToString(nbrSheets)
        Debug.Print("Number of sheets: " + snbrSheets)
        Debug.Print(" ")

        Dim i As Integer
        For i = 0 To UBound(Sheets)
            Sheet = Sheets(i)
            Debug.Print("Name of sheet: " + (Sheet.Name))
            Debug.Print("Name of preview PNG's stream: " + (Sheet.PreviewPNGStreamName))
            Dim objBitMap As Object = Sheet.GetPreviewPNGBitmap(nError)
            If nError = 0 Then
                ' For each sheet, convert the picture to an
                ' image and save it as .png file
                Dim imgPreview As System.Drawing.Image = PictureDispConverter.Convert(objBitMap)
                imgPreview.Save("c:\temp\" + Sheet.Name + ".png", Drawing.Imaging.ImageFormat.Png)
                imgPreview.Dispose()

                ' Get the preview's PNG byte array
                PreviewPNGByteArray = Sheet.GetPreviewPNGBitmapBytes(nError)
                Dim nbrPreviewPNGBitmapBytes As Integer
                nbrPreviewPNGBitmapBytes = CLng(UBound(PreviewPNGByteArray))
                nbrPreviewPNGBitmapBytes = nbrPreviewPNGBitmapBytes + 1
                Dim snbrPreviewPNGBitmapBytes As String = Convert.ToString(nbrPreviewPNGBitmapBytes)
                Debug.Print("Number of bytes in preview's PNG byte array: " + snbrPreviewPNGBitmapBytes)
                Debug.Print("")
            Else
                Select Case nError
                    Case 2
                        Debug.Print("Error: No preview data stored with document.")
                    Case 4
                        Debug.Print("Error: Failed to make the bitmap.")
                End Select
            End If
        Next

        swDoc.CloseDoc()

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
