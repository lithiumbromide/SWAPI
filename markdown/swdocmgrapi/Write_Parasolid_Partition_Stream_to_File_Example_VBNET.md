---
title: "Write Parasolid Partition Stream to File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Write_Parasolid_Partition_Stream_to_File_Example_VBNET.htm"
---

# Write Parasolid Partition Stream to File Example (VB.NET)

This example shows how to write a Parasolid partition stream to a file for a part.

**NOTE:** To get the name of the stream and a preview bitmap of the sheet active when the drawing was last saved, use ISwDMDocument10::GetPreviewBitmap and ISwDMDocument10::PreviewStreamName. To get the name of the streams and the preview bitmaps for all sheets in a drawing, use ISwDMSheet2::GetPreviewPNGBitmap and ISwDMSheet2::PreviewPNGStreamName.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Read the SOLIDWORKS Document Manager API Getting Started
'    topic and verify that the required DLLs are registered.
' 2. Create a VB.NET console application in Microsoft Visual Studio.
' 3. Copy and paste Module1 into Module1.vb.
'    a. Specify your_license_key.
'    b. Verify that the specified part to open exists.
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
' 1. Creates c:\temp\multi-inter.bmp and c:\temp\Default.xmp_bin.
' 2. Examine the c:\temp and the Immediate Window.
'---------------------------------------------------------------------------
'Module1
Imports System
Imports System.Diagnostics
Imports SolidWorks.Interop.swdocumentmgr
Imports System.Drawing
Imports stdole
Imports System.Windows.Forms

Module Module1

    Public Enum SwDmDocumentVersion_e
        SwDmDocumentVersionSOLIDWORKS_2000 = 1500
        SwDmDocumentVersionSOLIDWORKS_2001 = 1750
        SwDmDocumentVersionSOLIDWORKS_2001Plus = 1950
        SwDmDocumentVersionSOLIDWORKS_2003 = 2200
        SwDmDocumentVersionSOLIDWORKS_2004 = 2500
        SwDmDocumentVersionSOLIDWORKS_2005 = 2800
        SwDmDocumentVersionSOLIDWORKS_2006 = 3100
        SwDmDocumentVersionSOLIDWORKS_2007 = 3400
        SwDmDocumentVersionSOLIDWORKS_2008 = 3800
        SwDmDocumentVersionSOLIDWORKS_2009 = 4100
        SwDmDocumentVersionSOLIDWORKS_2010 = 4400
        SwDmDocumentVersionSOLIDWORKS_2011 = 4700
        SwDmDocumentVersionSOLIDWORKS_2012 = 5000
        SwDmDocumentVersionSOLIDWORKS_2013 = 6000
        SwDmDocumentVersionSOLIDWORKS_2014 = 7000
        SwDmDocumentVersionSOLIDWORKS_2015 = 8000
        SwDmDocumentVersionSOLIDWORKS_2016 = 9000
        SwDmDocumentVersionSOLIDWORKS_2017 = 10000
        SwDmDocumentVersionSOLIDWORKS_2018 = 11000
        SwDmDocumentVersionSOLIDWORKS_2019 = 12000
        SwDmDocumentVersionSOLIDWORKS_2020 = 13000
        SwDmDocumentVersionSOLIDWORKS_2021 = 14000
        SwDmDocumentVersionSOLIDWORKS_2022 = 15000
	SwDmDocumentVersionSOLIDWORKS_2023 = 16000
	SwDmDocumentVersionSOLIDWORKS_2024 = 17000
        SwDmDocumentVersionSOLIDWORKS_2025 = 18000
        SwDmDocumentVersionSOLIDWORKS_2026 = 19000
    End Enum

    Sub main()

        Const sLicenseKey As String = "your_license_key"
        Const sDocFileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\multibody\multi_inter.sldprt"
        Const sExtractDir As String = "c:\temp\"

        Dim swClassFact As SwDMClassFactory
        Dim swDocMgr As SwDMApplication
        Dim swDoc As SwDMDocument
        Dim swDoc10 As SwDMDocument10
        Dim swCfgMgr As SwDMConfigurationMgr
        Dim vCfgNameArr As Object
        Dim vCfgName As String
        Dim swCfg As SwDMConfiguration2
        Dim nDocType As Integer
        Dim nRetVal As Integer
        Dim i As Integer
        Dim sFileName As String = "multi_inter"

        ' Determine type of SOLIDWORKS file based on file extension
        If InStr(LCase(sDocFileName), "sldprt") > 0 Then
            nDocType = SwDmDocumentType.swDmDocumentPart
        ElseIf InStr(LCase(sDocFileName), "sldasm") > 0 Then
            nDocType = SwDmDocumentType.swDmDocumentAssembly
        ElseIf InStr(LCase(sDocFileName), "slddrw") > 0 Then
            nDocType = SwDmDocumentType.swDmDocumentDrawing
        Else
            ' Probably not a SOLIDWORKS file, so cannot open
            nDocType = SwDmDocumentType.swDmDocumentUnknown
            Exit Sub
        End If

        ' Because drawing documents do not have configurations,
        ' only continue running the macro if the document
        ' is a part or assembly document
        If (nDocType <> SwDmDocumentType.swDmDocumentDrawing) Then
            swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
            swDocMgr = swClassFact.GetApplication(sLicenseKey)
            swDoc = swDocMgr.GetDocument(sDocFileName, nDocType, True, nRetVal)

            swCfgMgr = swDoc.ConfigurationManager

            Debug.Print("File = " & swDoc.FullName)
            Debug.Print("  Active Configuration Name = " & swCfgMgr.GetActiveConfigurationName)
            Debug.Print("")
            Debug.Print("  Version = " & swDoc.GetVersion)
            Debug.Print("  Author = " & swDoc.Author)
            Debug.Print("  Comments = " & swDoc.Comments)
            Debug.Print("  Creation Date = " & swDoc.CreationDate)
            Debug.Print("  Keywords = " & swDoc.Keywords)
            Debug.Print("  Last Saved By = " & swDoc.LastSavedBy)
            Debug.Print("  Last Saved Date = " & swDoc.LastSavedDate)
            Debug.Print("  Subject = " & swDoc.Subject)
            Debug.Print("  Title = " & swDoc.Title)

            vCfgNameArr = swCfgMgr.GetConfigurationNames

            For Each vCfgName In vCfgNameArr
                swCfg = swCfgMgr.GetConfigurationByName(vCfgName)
                swDoc10 = swDoc
                Dim objBitMap As Object = swDoc10.GetPreviewBitmap(nRetVal)
                Dim imgPreview As Drawing.Image = PictureDispConverter.Convert(objBitMap)
                imgPreview.Save(sExtractDir + sFilename + ".bmp", Drawing.Imaging.ImageFormat.Bmp)
                imgPreview.Dispose()

                Debug.Print("  " & vCfgName)
                Debug.Print("    Description = " & swCfg.Description)
                Debug.Print("    Parent Configuration Name = " & swCfg.GetParentConfigurationName)
                Debug.Print("    Preview stream = " & swCfg.PreviewStreamName)

                Select Case swDoc.GetVersion

                    Case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2000, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2001, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2001Plus, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2003
                        Debug.Print("    Body stream = " & swCfg.StreamName)
                        Debug.Print("      Body count = " & swCfg.GetBodiesCount - 1)

                        For i = 0 To swCfg.GetBodiesCount - 1
                            nRetVal = swCfg.GetBody(i, sExtractDir & vCfgName & "_" & i & ".x_b")
                        Next i

                    Case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2004, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2005, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2006, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2007, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2008, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2009, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2010, SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2011,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2012,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2013,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2014,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2015,
		    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2016,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2017,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2018,
		    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2019,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2020,
		    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2021,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2022,
		    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2023,
		    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2024,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2025,
                    SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2026
                        Debug.Print("    Partition stream = " & swCfg.StreamName)

                        ' SwDMConfiguration2::GetPartitionStream takes file name as an input and writes
                        ' to it. The extensions .xmp_bin (for NTFS) and .p_b (for FAT) are the valid
                        ' extensions of a partition file. PK_PARTITION_receive_u takes this file name as
                        ' input to get partitions and bodies in it.
                        ' Refer to Parasolid documentation for details.

                        nRetVal = swCfg.GetPartitionStream(sExtractDir & vCfgName & ".xmp_bin")

                    Case Else

                End Select
            Next
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

    Public Shared Function Convert(ByVal objIDispImage As Object) As Drawing.Image

        Dim objPicture As Drawing.Image
        objPicture = CType(System.Windows.Forms.AxHost.GetPictureFromIPicture(objIDispImage), Drawing.Image)
        Return objPicture
    End Function

End Class
```
