---
title: "ViewPdfAfterSaving Property (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "ViewPdfAfterSaving"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ViewPdfAfterSaving.html"
---

# ViewPdfAfterSaving Property (IMBD3DPdfData)

Gets or sets whether to display this SOLIDWORKS MBD 3D PDF after [publishing it](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ViewPdfAfterSaving As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Boolean

instance.ViewPdfAfterSaving = value

value = instance.ViewPdfAfterSaving
```

### C#

```csharp
System.bool ViewPdfAfterSaving {get; set;}
```

### C++/CLI

```cpp
property System.bool ViewPdfAfterSaving {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the SOLIDWORKS MBD 3D PDF after publishing it, false to not

## VBA Syntax

See [MBD3DPdfData::ViewPdfAfterSaving](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~ViewPdfAfterSaving.html).

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
