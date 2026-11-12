---
title: "PatternTreatment Property (IDimXpertDistanceBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDistanceBetweenDimTol"
member: "PatternTreatment"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol~PatternTreatment.html"
---

# PatternTreatment Property (IDimXpertDistanceBetweenDimTol)

Gets the pattern treatment for this DimXpert distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternTreatment As swDimXpertPatternTreatmentType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDistanceBetweenDimTol
Dim value As swDimXpertPatternTreatmentType_e

value = instance.PatternTreatment
```

### C#

```csharp
swDimXpertPatternTreatmentType_e PatternTreatment {get;}
```

### C++/CLI

```cpp
property swDimXpertPatternTreatmentType_e PatternTreatment {
   swDimXpertPatternTreatmentType_e get();
}
```

### Property Value

Pattern treatment type as defined in [swDimXpertPatternTreatmentType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertPatternTreatmentType_e.html)

## VBA Syntax

See [DimXpertDistanceBetweenDimTol::PatternTreatment](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDistanceBetweenDimTol~PatternTreatment.html).

## See Also

[IDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol.html)
[IDimXpertDistanceBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
