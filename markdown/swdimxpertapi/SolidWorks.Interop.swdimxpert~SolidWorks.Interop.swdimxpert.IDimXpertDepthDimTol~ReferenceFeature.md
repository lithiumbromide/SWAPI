---
title: "ReferenceFeature Property (IDimXpertDepthDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDepthDimTol"
member: "ReferenceFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDepthDimTol~ReferenceFeature.html"
---

# ReferenceFeature Property (IDimXpertDepthDimTol)

Gets the reference feature for this DimXpert depth dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceFeature As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDepthDimTol
Dim value As DimXpertFeature

value = instance.ReferenceFeature
```

### C#

```csharp
DimXpertFeature ReferenceFeature {get;}
```

### C++/CLI

```cpp
property DimXpertFeature^ ReferenceFeature {
   DimXpertFeature^ get();
}
```

### Property Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertDepthDimTol::ReferenceFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDepthDimTol~ReferenceFeature.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertDepthDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDepthDimTol.html)
[IDimXpertDepthDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDepthDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
