---
title: "Fire Notification When Publishing Part to MBD 3D PDF Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VBNET.htm"
---

# Fire Notification When Publishing Part to MBD 3D PDF Example (VB.NET)

This example shows how to fire a notification when publishing a part document to SOLIDWORKS MBD 3D PDF.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that:
'    * specified part,
'    * SOLIDWORKS MBD 3D PDF theme, and
'    * c:\temp exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part.
' 2. Gets the MBD3DPdfData object.
' 3. Sets the path and file name for the SOLIDWORKS MBD 3D PDF.
' 4. Sets the theme for the SOLIDWORKS MBD 3D PDF.
' 5. Sets standard views for the SOLIDWORKS MBD 3D PDF.
' 6. Publishes the part document to SOLIDWORKS MBD 3D PDF.
' 7. Displays a message saying that the part document
'    was published to SOLIDWORKS MBD 3D PDF.
' 8. Click OK to close the message box.
' 9. Examine the Immediate window and c:\temp\MBDPart1.PDF.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public WithEvents swPart As PartDoc

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swMBDPdfData As MBD3DPdfData
        Dim fileName As String
        Dim standardViews As Object
        Dim viewIDs(2) As Integer
        Dim status As Integer
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Set up events
        swPart = swModel
        AttachEventHandlers()

        'Get MBD3DPdfData object
        swMBDPdfData = swModelDocExt.GetMBD3DPdfData

        'Set path and file name for SOLIDWORKS MBD 3D PDF
        swMBDPdfData.FilePath = "c:\temp\MBDPart1.PDF"

        'Set SOLIDWORKS MBD 3D PDF theme
        swMBDPdfData.ThemeName = "C:\Program Files\SolidWorks Corp\SOLIDWORKS\data\themes\simple part (a4, portrait)\theme.xml"

        'Set standard views for SOLIDWORKS MBD 3D PDF
        viewIDs(0) = swStandardViews_e.swFrontView
        viewIDs(1) = swStandardViews_e.swTopView
        viewIDs(2) = swStandardViews_e.swDimetricView
        standardViews = viewIDs
        swMBDPdfData.SetStandardViews(standardViews)

        'Publish part document to SOLIDWORKS MBD 3D PDF
        status = swModelDocExt.PublishTo3DPDF(swMBDPdfData)
        Debug.Print("Status of publishing part to SOLIDWORKS MBD 3D PDF (0 = success): " & status)

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swPart.PublishTo3DPDFNotify, AddressOf Me.swPart_PublishTo3DPDFNotify
    End Sub

    Private Function swPart_PublishTo3DPDFNotify(ByVal path As String) As Integer
        MsgBox("Part document published to SOLIDWORKS MBD 3D PDF: " & path)
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
