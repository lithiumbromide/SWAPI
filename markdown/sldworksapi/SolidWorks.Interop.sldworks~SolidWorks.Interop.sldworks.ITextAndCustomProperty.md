---
title: "ITextAndCustomProperty Interface"
project: "SOLIDWORKS API Help"
interface: "ITextAndCustomProperty"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty.html"
---

# ITextAndCustomProperty Interface

Gains access to the text and custom properties in a [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html) of a [SOLIDWORKS MBD 3D PDF](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ITextAndCustomProperty
```

### Visual Basic (Usage)

```vb
Dim instance As ITextAndCustomProperty
```

### C#

```csharp
public interface ITextAndCustomProperty
```

### C++/CLI

```cpp
public interface class ITextAndCustomProperty
```

## VBA Syntax

See [TextAndCustomProperty](ms-its:sldworksapivb6.chm::/sldworks~TextAndCustomProperty.html).

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## Remarks

SOLIDWORKS Model Based Definition (MBD) is an integrated drawingless manufacturing solution for SOLIDWORKS.

Typical steps for generating a SOLIDWORKS MBD 3D PDF using the SOLIDWORKS API are:

1. Get the [MBD3DPdfData object](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html) using [IModelDocExtension::GetMBD3DPdfData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMBD3DPdfData.html).
2. Set the path and file name of the SOLIDWORKS MBD 3D PDF theme using [IMBD3DPdfData::ThemeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html).
3. Get standard and custom views using [IMBD3DPdfData::GetStandardViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetStandardViews.html) and [IMBD3DPdfData::GetMoreViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetMoreViews.html).
4. Set standard and custom views using [IMBD3DPdfData::SetStandardViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetStandardViews.html) and [IMBD3DPdfData::SetMoreViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetMoreViews.html).
5. Get and set text and custom properties in the theme using the array of objects returned by this interface's accessor. See the **Accessors** section.
6. Set the path for the SOLIDWORKS MBD 3D PDF using [IMBD3DPdfData::FilePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~FilePath.html).
7. Generate the SOLIDWORKS MBD 3D PDF using [IModelDocExtension::PublishTo3DPDF](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.html).

See the SOLIDWORKS Help for details about MBD.

## Accessors

[IMBD3DPdfData::GetTextAndCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetTextAndCustomProperties.html)

## Access Diagram

[TextAndCustomProperty](SWObjectModel.pdf#TextAndCustomProperty)

## See Also

[ITextAndCustomProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
