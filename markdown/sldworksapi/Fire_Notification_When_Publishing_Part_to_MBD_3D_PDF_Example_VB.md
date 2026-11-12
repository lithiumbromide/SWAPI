---
title: "Fire Notification When Publishing Part to MBD 3D PDF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VB.htm"
---

# Fire Notification When Publishing Part to MBD 3D PDF Example (VBA)

This example shows how to fire a notification when publishing a part document to SOLIDWORKS MBD 3D PDF.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that:
'    * specified part,
'    * SOLIDWORKS MBD 3D PDF theme, and
'    * c:\temp exist.
' 2. Copy this code to the main module.
' 3. Click Insert > Class Module and copy this code to the
'    Class1 module.
' 4. Open the Immediate window.
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
'main module
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As ModelDocExtension
Dim swMBDPdfData As SldWorks.MBD3DPdfData
Dim fileName As String
Dim standardViews As Variant
Dim viewIDs(2) As Long
Dim status As Long
Dim errors As Long
Dim warnings As Long
Dim swPart As SldWorks.PartDoc
Dim swPartEvents As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    ' Event notification
    Set swPart = swModel
    Set swPartEvents = New Class1
    Set swPartEvents.swPart = swApp.ActiveDoc
```

```
    'Get MBD3DPdfData object
    Set swMBDPdfData = swModelDocExt.GetMBD3DPdfData
```

```
    'Specify path and file name for SOLIDWORKS MBD 3D PDF
    swMBDPdfData.filePath = "c:\temp\MBDPart1.PDF"
```

```
    'Set SOLIDWORKS MBD 3D PDF theme
    swMBDPdfData.ThemeName = "C:\Program Files\SolidWorks Corp\SOLIDWORKS\data\themes\simple part (a4, portrait)\theme.xml"
```

```
    'Set standard views for SOLIDWORKS MBD 3D PDF
    viewIDs(0) = swStandardViews_e.swFrontView
    viewIDs(1) = swStandardViews_e.swTopView
    viewIDs(2) = swStandardViews_e.swDimetricView
    standardViews = viewIDs
    swMBDPdfData.SetStandardViews (standardViews)
```

```
    'Publish part document to SOLIDWORKS MBD 3D PDF
    status = swModelDocExt.PublishTo3DPDF(swMBDPdfData)
    Debug.Print ("Status of publishing part to SOLIDWORKS MBD 3D PDF (0 = success): " & status)
```

```
End Sub
```

```
Back to top
```

```
'Class1 module
Option Explicit
```

```
Public WithEvents swPart As SldWorks.PartDoc
```

```
Private Function swPart_PublishTo3DPDFNotify(ByVal path As String) As Long
    MsgBox "Part document published to SOLIDWORKS MBD 3D PDF: " & path
End Function
```

```
Back to top
```
