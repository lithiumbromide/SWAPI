---
title: "Type Property (IDimXpertBlockTolerances)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertBlockTolerances"
member: "Type"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBlockTolerances~Type.html"
---

# Type Property (IDimXpertBlockTolerances)

Gets the type of this DimXpert block tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As swDimXpertBlockToleranceType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertBlockTolerances
Dim value As swDimXpertBlockToleranceType_e

value = instance.Type
```

### C#

```csharp
swDimXpertBlockToleranceType_e Type {get;}
```

### C++/CLI

```cpp
property swDimXpertBlockToleranceType_e Type {
   swDimXpertBlockToleranceType_e get();
}
```

### Property Value

Type of this DimXpert block tolerance as defined in [swDimXpertBlockToleranceType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertBlockToleranceType_e.html)

## VBA Syntax

See [DimXpertBlockTolerances::Type](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertBlockTolerances~Type.html).

## See Also

[IDimXpertBlockTolerances Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBlockTolerances.html)
[IDimXpertBlockTolerances Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBlockTolerances_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
