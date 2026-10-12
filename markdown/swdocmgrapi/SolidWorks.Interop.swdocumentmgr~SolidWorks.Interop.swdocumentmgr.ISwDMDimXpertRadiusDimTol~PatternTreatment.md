---
title: "PatternTreatment Property (ISwDMDimXpertRadiusDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertRadiusDimTol"
member: "PatternTreatment"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertRadiusDimTol~PatternTreatment.html"
---

# PatternTreatment Property (ISwDMDimXpertRadiusDimTol)

Gets the pattern treatment for this DimXpert radius dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternTreatment As swDmDimXpertPatternTreatmentType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertRadiusDimTol
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

Pattern treatment for the radius dimension tolerance as defined in [swDmDimXpertPatternTreatmentType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertPatternTreatmentType_e.html)

## VBA Syntax

See [SwDMDimXpertRadiusDimTol::PatternTreatment](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertRadiusDimTol~PatternTreatment.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertRadiusDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertRadiusDimTol.html)
[ISwDMDimXpertRadiusDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertRadiusDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
