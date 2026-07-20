---
title: "PublishTo3DPDF Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "PublishTo3DPDF"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.html"
---

# PublishTo3DPDF Method (IModelDocExtension)

Creates a 3D PDF for SOLIDWORKS MBD.

## Syntax

### Visual Basic (Declaration)

```vb
Function PublishTo3DPDF( _
   ByVal MBDPdfData As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim MBDPdfData As System.Object
Dim value As System.Integer

value = instance.PublishTo3DPDF(MBDPdfData)
```

### C#

```csharp
System.int PublishTo3DPDF(
   System.object MBDPdfData
)
```

### C++/CLI

```cpp
System.int PublishTo3DPDF(
   System.Object^ MBDPdfData
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `MBDPdfData`: [SOLIDWORKS MBD 3D PDF data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)

### Return Value

Status as defined in

[swPublishTo3DPDFError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPublishTo3DPDFError_e.html)

## VBA Syntax

See

[ModelDocExtension::PublishTo3DPDF](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~PublishTo3DPDF.html)

.

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)

[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)

[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

[Fire Notification When Publishing Part to MBD 3D PDF (C#)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_CSharp.htm)

[Fire Notification When Publishing Part to MBD 3D PDF (VB.NET)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VBNET.htm)

[Fire Notification When Publishing Part to MBD 3D PDF (VBA)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VB.htm)

## Remarks

SOLIDWORKS Model Based Definition (MBD) is an integrated drawingless manufacturing solution for SOLIDWORKS.

This method:

- requires the that the SOLDWORKS MBD add-in be loaded. (

  [ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html)

  )

- corresponds to the

  Publish to 3D PDF

  button on the SOLIDWORKS MBD toolbar.

Typical steps for generating a SOLIDWORKS MBD 3D PDF using the SOLIDWORKS API are:

1. Get the MBD3DPdfData object using

  [IModelDocExtension::GetMBD3DPdfData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMBD3DPdfData.html)

  .
2. Set the path and file name of the SOLIDWORKS MBD 3D PDF theme using

  [IMBD3DPdfData::ThemeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html)

  .
3. Get standard and custom views using

  [IMBD3DPdfData::GetStandardViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetStandardViews.html)

  and

  [IMBD3DPdfData::GetMoreViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetMoreViews.html)

  .
4. Set standard and custom views using

  [IMBD3DPdfData::SetStandardViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetStandardViews.html)

  and

  [IMBD3DPdfData::SetMoreViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetMoreViews.html)

  .
5. Get and set text and custom properties in the theme using

  [IMBD3DPdfData::GetTextAndCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetTextAndCustomProperties.html)

  and

  [ITextAndCustomProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty.html)

  .
6. Set the path for the SOLIDWORKS MBD 3D PDF using

  [IMBD3DPdfData::FilePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~FilePath.html)

  .
7. Generate the SOLIDWORKS MBD 3D PDF using this method.

See the SOLIDWORKS Help for details about MBD.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)

[IModelDocExtension::PublishSTEP242File Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
