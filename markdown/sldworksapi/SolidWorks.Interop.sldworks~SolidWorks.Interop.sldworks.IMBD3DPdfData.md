---
title: "IMBD3DPdfData Interface"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html"
---

# IMBD3DPdfData Interface

Gains access to the details for publishing a SOLIDWORKS MBD 3D PDF.

**NOTE:**Click the**Members**link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMBD3DPdfData
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
```

### C#

```csharp
public interface IMBD3DPdfData
```

### C++/CLI

```cpp
public interface class IMBD3DPdfData
```

## VBA Syntax

See

[MBD3DPdfData](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData.html)

.

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)

[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)

[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

[Export BOM's Second Column to BOM Table Area (C#)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_CSharp.htm)

[Export BOM's Second Column to BOM Table Area (VB.NET)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VBNET.htm)

[Export BOM's Second Column to BOM Table Area (VBA)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VB.htm)

[Fire Notification When Publishing Part to MBD 3D PDF (VB.NET)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VBNET.htm)

[Fire Notification When Publishing Part to MBD 3D PDF (C#)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_CSharp.htm)

[Fire Notification When Publishing Part to MBD 3D PDF (VBA)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VB.htm)

## Remarks

SOLIDWORKS Model Based Definition (MBD) is an integrated drawingless manufacturing solution for SOLIDWORKS.

This interface and its methods and properties require that the SOLDWORKS MBD add-in be loaded. ([ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html))

The MBD3DPdfData object corresponds to the SOLIDWORKS MBD**Publish to 3D PDF**PropertyManager page.

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

  [IMBD3DPdfData::GetTextCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetTextAndCustomProperties.html)

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

## Accessors

[IModelDocExtension::GetMBD3DPdfData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMBD3DPdfData.html)

## Access Diagram

[MBD3DPdfData](SWObjectModel.pdf#MBD3DPdfData)

## See Also

[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[IModelDocExtension::PublishTo3DPDF Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.html)

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
