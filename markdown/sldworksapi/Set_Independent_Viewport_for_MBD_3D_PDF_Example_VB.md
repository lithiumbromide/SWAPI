---
title: "Set Independent Viewport for MBD 3D PDF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Independent_Viewport_for_MBD_3D_PDF_Example_VB.htm"
---

# Set Independent Viewport for MBD 3D PDF Example (VBA)

This example shows how to set a view for an independent viewport for a SOLIDWORKS MBD 3D PDF.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Copy install_dir\data\themes\simple assembly (letter, landscape) to
'    C:\test\simple assembly (letter, landscape).
' 3. In SOLIDWORKS Design, click the SOLIDWORKS MBD toolbar > 3D PDF Template Editor.
'    a. Click Independent Viewport.
'    b. Click Save As.
'    c. Ensure that Theme Directory is C:\test\simple assembly (letter, landscape).
'    d. Type AllViews in Name.
'    e. Click Save.
'    f. Close the 3D PDF Template Editor.
'
' Postconditions:
' 1. Gets the MBD3DPdfData object.
' 2. Sets the path and file name for the SOLIDWORKS MBD 3D PDF.
' 3. Sets to display SOLIDWORKS MBD 3D PDF after publishing.
' 4. Sets the theme for the SOLIDWORKS MBD 3D PDF.
' 5. Sets the view to display in the independent viewport
'    for the SOLIDWORKS MBD 3D PDF.
' 6. Creates and displays MBDPart1.PDF.
' 7. Examine MBDPart1.PDF.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMBDPdfData As SldWorks.MBD3DPdfData

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
    swMBDPdfData.FilePath = "C:\temp\MBDPart1.PDF"
```

```
    'Display SOLIDWORKS MBD 3D PDF
    swMBDPdfData.ViewPdfAfterSaving = True
```

```
    'Set SOLIDWORKS MBD 3D PDF theme
    swMBDPdfData.ThemeName = "C:\test\simple assembly (letter, landscape)\AllViews\theme.xml"
```

```
    'Set view for AllViews
    swMBDPdfData.SetIndependentViewPort "*Top"
```

```
    'Create SOLIDWORKS MBD 3D PDF
    swModelDocExt.PublishTo3DPDF swMBDPdfData
```

```
End Sub
```
