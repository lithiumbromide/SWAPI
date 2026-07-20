---
title: "GetMBD3DPdfData Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetMBD3DPdfData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMBD3DPdfData.html"
---

# GetMBD3DPdfData Method (IModelDocExtension)

Gets the SOLIDWORKS MBD 3D PDF data object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMBD3DPdfData() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetMBD3DPdfData()
```

### C#

```csharp
System.object GetMBD3DPdfData()
```

### C++/CLI

```cpp
System.Object^ GetMBD3DPdfData();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

[IMBD3DPdfData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)

object

## VBA Syntax

See

[ModelDocExtension::GetMBD3DPdfData](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetMBD3DPdfData.html)

.

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)

[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)

[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## Remarks

SOLIDWORKS Model Based Definition (MBD) is an integrated drawingless manufacturing solution for SOLIDWORKS.

This method requires that the SOLDWORKS MBD add-in be loaded. ([ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html))

Typical steps for generating a SOLIDWORKS MBD 3D PDF using the SOLIDWORKS API are:

1. Get the MBD3DPdfData object using this method.
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
7. Generate the SOLIDWORKS MBD 3D PDF using

  [IModelDocExtension::PublishTo3DPDF](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.html)

  .

See the SOLIDWORKS Help for details about MBD.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
