---
title: "SetStandardViews Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "SetStandardViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetStandardViews.html"
---

# SetStandardViews Method (IMBD3DPdfData)

Sets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetStandardViews( _
   ByVal Values As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim Values As System.Object

instance.SetStandardViews(Values)
```

### C#

```csharp
void SetStandardViews(
   System.object Values
)
```

### C++/CLI

```cpp
void SetStandardViews(
   System.Object^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Values`: Array of the types of standard views as defined in [swStandardViews_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStandardViews_e.html)

## VBA Syntax

See [MBD3DPdfData::SetStandardViews](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~SetStandardViews.html).

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::GetStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetStandardViews.html)
[IMBD3DPdfData::GetMoreViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetMoreViews.html)
[IMBD3DPdfData::SetMoreViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetMoreViews.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
