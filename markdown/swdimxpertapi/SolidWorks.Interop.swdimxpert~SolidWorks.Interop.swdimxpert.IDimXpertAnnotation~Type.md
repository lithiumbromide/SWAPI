---
title: "Type Property (IDimXpertAnnotation)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: "Type"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~Type.html"
---

# Type Property (IDimXpertAnnotation)

Gets the type of this DimXpert annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As swDimXpertAnnotationType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
Dim value As swDimXpertAnnotationType_e

value = instance.Type
```

### C#

```csharp
swDimXpertAnnotationType_e Type {get;}
```

### C++/CLI

```cpp
property swDimXpertAnnotationType_e Type {
   swDimXpertAnnotationType_e get();
}
```

### Property Value

Type of this DimXpert annotation as defined in [swDimXpertAnnotationType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertAnnotationType_e.html)

## VBA Syntax

See [DimXpertAnnotation::Type](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAnnotation~Type.html).

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
