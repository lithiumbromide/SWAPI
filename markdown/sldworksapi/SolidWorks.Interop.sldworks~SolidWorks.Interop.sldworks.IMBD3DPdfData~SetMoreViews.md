---
title: "SetMoreViews Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "SetMoreViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetMoreViews.html"
---

# SetMoreViews Method (IMBD3DPdfData)

Sets the names of the custom views (i.e., [named views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.html) and [3D views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)) in the model for this SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMoreViews( _
   ByVal Values As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim Values As System.Object

instance.SetMoreViews(Values)
```

### C#

```csharp
void SetMoreViews(
   System.object Values
)
```

### C++/CLI

```cpp
void SetMoreViews(
   System.Object^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Values`: Array of strings of the names of the custom views

## VBA Syntax

See [MBD3DPdfData::SetMoreViews](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~SetMoreViews.html).

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::GetMoreViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetMoreViews.html)
[IMBD3DPdfData::SetStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetStandardViews.html)
[IMBD3DPdfData::GetStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetStandardViews.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
