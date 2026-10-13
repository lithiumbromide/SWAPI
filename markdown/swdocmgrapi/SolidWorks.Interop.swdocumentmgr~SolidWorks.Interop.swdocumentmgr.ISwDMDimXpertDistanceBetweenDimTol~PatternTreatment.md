---
title: "PatternTreatment Property (ISwDMDimXpertDistanceBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDistanceBetweenDimTol"
member: "PatternTreatment"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol~PatternTreatment.html"
---

# PatternTreatment Property (ISwDMDimXpertDistanceBetweenDimTol)

Gets the pattern treatment for this DimXpert distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternTreatment As swDmDimXpertPatternTreatmentType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDistanceBetweenDimTol
Dim value As swDmDimXpertPatternTreatmentType_e

value = instance.PatternTreatment
```

### C#

```csharp
swDmDimXpertPatternTreatmentType_e PatternTreatment {get;}
```

### C++/CLI

```cpp
property swDmDimXpertPatternTreatmentType_e PatternTreatment {
   swDmDimXpertPatternTreatmentType_e get();
}
```

### Property Value

Pattern treatment for the diameter dimension tolerance as defined in [swDmDimXpertPatternTreatmentType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertPatternTreatmentType_e.html)

## VBA Syntax

See [SwDMDimXpertDistanceBetweenDimTol::PatternTreatment](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDistanceBetweenDimTol~PatternTreatment.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol.html)
[ISwDMDimXpertDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
