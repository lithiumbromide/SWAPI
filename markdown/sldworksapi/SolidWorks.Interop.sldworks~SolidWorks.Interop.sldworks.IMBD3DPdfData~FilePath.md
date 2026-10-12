---
title: "FilePath Property (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "FilePath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~FilePath.html"
---

# FilePath Property (IMBD3DPdfData)

Gets or sets the path and file name to which to save this SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Property FilePath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.String

instance.FilePath = value

value = instance.FilePath
```

### C#

```csharp
System.string FilePath {get; set;}
```

### C++/CLI

```cpp
property System.String^ FilePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and file name

## VBA Syntax

See [MBD3DPdfData::FilePath](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~FilePath.html).

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::ViewPdfAfterSaving Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ViewPdfAfterSaving.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
