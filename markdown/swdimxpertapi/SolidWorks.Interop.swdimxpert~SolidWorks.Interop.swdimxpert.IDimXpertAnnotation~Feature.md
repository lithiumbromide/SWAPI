---
title: "Feature Property (IDimXpertAnnotation)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: "Feature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~Feature.html"
---

# Feature Property (IDimXpertAnnotation)

Gets the DimXpert feature to which this DimXpert annotation is applied.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Feature As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
Dim value As DimXpertFeature

value = instance.Feature
```

### C#

```csharp
DimXpertFeature Feature {get;}
```

### C++/CLI

```cpp
property DimXpertFeature^ Feature {
   DimXpertFeature^ get();
}
```

### Property Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertAnnotation::Feature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAnnotation~Feature.html).

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
