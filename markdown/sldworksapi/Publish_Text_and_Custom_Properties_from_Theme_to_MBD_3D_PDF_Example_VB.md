---
title: "Publish Text and Custom Properties from Theme to MBD 3D PDF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm"
---

# Publish Text and Custom Properties from Theme to MBD 3D PDF Example (VBA)

This example shows how to publish text and custom properties from a theme to SOLIDWORKS MBD 3D PDF.

```
'--------------------------------------------------------------
' Preconditions:
'  1. Verify that:
'     * specified part,
'     * SOLIDWORKS MBD 3D PDF theme, and
'     * c:\temp exist.
'  2. Open the Immediate window.
'
' Postconditions:
'  1. Opens the specified part.
'  2. Gets the MBD3DPdfData object.
'  3. Sets the path and file name for the SOLIDWORKS MBD 3D PDF.
'  4. Sets to display SOLIDWORKS MBD 3D PDF after publishing.
'  5. Sets the theme for the SOLIDWORKS MBD 3D PDF.
'  6. Sets standard views for the SOLIDWORKS MBD 3D PDF.
'  7. Creates and sets custom views for the SOLIDWORKS MBD 3D PDF.
'  8. Gets the text and custom properties from the specified
'     theme for the SOLIDWORKS MBD 3D PDF and sets the custom
'     property names.
'  9. Creates the SOLIDWORKS MBD 3D PDF.
' 10. Examine the Immediate window and c:\temp\MBDPart1.PDF.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMBDPdfData As SldWorks.MBD3DPdfData
Dim swTextAndCustomProperty As SldWorks.TextAndCustomProperty
Dim fileName As String
Dim standardViews As Variant
Dim viewIDs(2) As Long
Dim viewNames(1) As String
Dim textAndCustomProperties As Variant
Dim nbrTextAndCustomProperties As Long
Dim status As Long
Dim errors As Long
Dim warnings As Long
Dim custProp As String
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\temp\box.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Get MBD3DPdfData object
    Set swMBDPdfData = swModelDocExt.GetMBD3DPdfData
```

```
    'Set path and file name for SOLIDWORKS MBD 3D PDF
    swMBDPdfData.filePath = "c:\temp\MBDPart1.PDF"
```

```
    'Display SOLIDWORKS MBD 3D PDF
    swMBDPdfData.ViewPdfAfterSaving = True
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
    'Create and set custom views for SOLIDWORKS MBD 3D PDF
    swModel.NameView ("CustomView1")
    swModel.NameView ("CustomView2")
    viewNames(0) = "CustomView1"
    viewNames(1) = "CustomView2"
    swMBDPdfData.SetMoreViews (viewNames)
```

```
    'Get text and custom properties from theme for SOLIDWORKS MBD
    '3D PDF
    textAndCustomProperties = swMBDPdfData.GetTextAndCustomProperties
    If Not IsEmpty(textAndCustomProperties) Then
        nbrTextAndCustomProperties = UBound(textAndCustomProperties)
            Debug.Print "Text and custom properties from theme:"
            For i = 0 To nbrTextAndCustomProperties
                Set swTextAndCustomProperty = textAndCustomProperties(i)
                If swTextAndCustomProperty.IsCustomProperty = False Then
                    Debug.Print (" Text:")
                    Debug.Print ("  Description: " & swTextAndCustomProperty.Description)
                    Debug.Print ("  Field name: " & swTextAndCustomProperty.Name)
                Else
                    Debug.Print (" Custom property:")
                    custProp = "CustomProperty " + CStr(i)
                    swTextAndCustomProperty.CustomPropertyName = custProp
                    Debug.Print ("  Custom property name: " & swTextAndCustomProperty.CustomPropertyName)
                    Debug.Print ("  Description: " & swTextAndCustomProperty.Description)
                    Debug.Print ("  Field name: " & swTextAndCustomProperty.Name)
                    Debug.Print ("  Value: " & swTextAndCustomProperty.Value)
                End If
            Next i
    Else
       Debug.Print "No text or custom properties in theme."
    End If
```

```
    'Create SOLIDWORKS MBD 3D PDF
    status = swModelDocExt.PublishTo3DPDF(swMBDPdfData)
    Debug.Print ("Status of publishing part to SOLIDWORKS MBD 3D PDF (0 = success): " & status)
```

```
End Sub
```
