---
title: "Accuracy Property (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "Accuracy"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~Accuracy.html"
---

# Accuracy Property (IMBD3DPdfData)

Gets or sets the level of accuracy for lossy compression when publishing to SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Property Accuracy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Integer

instance.Accuracy = value

value = instance.Accuracy
```

### C#

```csharp
System.int Accuracy {get; set;}
```

### C++/CLI

```cpp
property System.int Accuracy {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Level of accuracy for lossy compression as defined in [sw3DPDFAccuracy_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DPDFAccuracy_e.html)

## VBA Syntax

See [MBD3DPdfData::Accuracy](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~Accuracy.html).

## Examples

[Attach Files to MBD 3D PDF (C#)](Attach_Files_to_MBD_3D_PDF_Example_CSharp.htm)
[Attach Files to MBD 3D PDF (VB.NET)](Attach_Files_to_MBD_3D_PDF_Example_VBNET.htm)
[Attach Files to MBD 3D PDF (VBA)](Attach_Files_to_MBD_3D_PDF_Example_VB.htm)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::CompressLossyTessellation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CompressLossyTessellation.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
