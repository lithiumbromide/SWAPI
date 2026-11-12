---
title: "CompressLossyTessellation Property (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "CompressLossyTessellation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CompressLossyTessellation.html"
---

# CompressLossyTessellation Property (IMBD3DPdfData)

Gets or sets whether to apply lossy compression to polygons in the model when publishing to SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Property CompressLossyTessellation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Boolean

instance.CompressLossyTessellation = value

value = instance.CompressLossyTessellation
```

### C#

```csharp
System.bool CompressLossyTessellation {get; set;}
```

### C++/CLI

```cpp
property System.bool CompressLossyTessellation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to apply lossy compression to polygons in the model, false to not

## VBA Syntax

See [MBD3DPdfData::CompressLossyTessellation](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~CompressLossyTessellation.html).

## Examples

[Attach Files to MBD 3D PDF (C#)](Attach_Files_to_MBD_3D_PDF_Example_CSharp.htm)
[Attach Files to MBD 3D PDF (VB.NET)](Attach_Files_to_MBD_3D_PDF_Example_VBNET.htm)
[Attach Files to MBD 3D PDF (VBA)](Attach_Files_to_MBD_3D_PDF_Example_VB.htm)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::Accuracy Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~Accuracy.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
