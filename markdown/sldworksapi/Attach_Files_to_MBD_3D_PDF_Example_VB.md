---
title: "Attach Files to MBD 3D PDF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Attach_Files_to_MBD_3D_PDF_Example_VB.htm"
---

# Attach Files to MBD 3D PDF Example (VBA)

This example shows how to attach files to a SOLIDWORKS MBD 3D PDF.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified SOLIDWORKS MBD 3D PDF theme,
'    files to attach, and C:\temp exist.
' 2. Open public_documents\samples\tutorial\api\block.sldprt.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the MBD3DPdfData object.
' 2. Sets the path and file name for the SOLIDWORKS MBD 3D PDF.
' 3. Sets the theme for the SOLIDWORKS MBD 3D PDF.
' 4. Sets the standard views for the SOLIDWORKS MBD 3D PDF.
' 5. Sets the level of accuracy for lossy compression, whether to
'    apply lossy compression to polygons in the model, and
'    whether to export SOLIDWORKS Design parts and assemblies with PMI
'    annotations to STEP 242 format.
' 6. Sets the files to attach to SOLIDWORKS MBD 3D PDF.
' 7. Creates the SOLIDWORKS MBD 3D PDF.
' 8. Examine the Immediate window.
' 9. Open C:\temp\block.PDF and click the paper clip (Attachments:
'    View file attachments) in the left-side panel.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMBDPdfData As SldWorks.MBD3DPdfData
Dim standardViews As Variant
Dim viewIDs(2) As Long
Dim filesToAttach(1) As String
Dim attachedFiles As Variant
Dim status As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    'Get MBD3DPdfData object
    Set swMBDPdfData = swModelDocExt.GetMBD3DPdfData
```

```
    'Set path and file name for SOLIDWORKS MBD 3D PDF
    swMBDPdfData.FilePath = "C:\temp\block.PDF"
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
    'Set SOLIDWORKS MBD 3D PDF theme
    swMBDPdfData.ThemeName = "C:\Program Files\SolidWorks Corp\SOLIDWORKS\data\themes\simple part (a4, portrait)\theme.xml"

    'Set the level of accuracy for lossy compression, whether to apply
    'lossy compression to polygons in the model, and whether to export
    'SOLIDWORKS Design parts and assemblies with PMI annotations to STEP 242
    'format
    swMBDPdfData.Accuracy = sw3DPDFAccuracy_e.swLow
    swMBDPdfData.CompressLossyTessellation = True
    swMBDPdfData.CreateAttachSTEP242 = True
```

```
    'Set the files to attach
    filesToAttach(0) = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.slddrw"
    filesToAttach(1) = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt"
    attachedFiles = filesToAttach
    swMBDPdfData.SetAttachments attachedFiles
```

```
    'Publish to PDF
    status = swModelDocExt.PublishTo3DPDF(swMBDPdfData)
    Debug.Print ("Status of publishing part to SOLIDWORKS MBD 3D PDF (0 = success): " & status)
```

```
End Sub
```
