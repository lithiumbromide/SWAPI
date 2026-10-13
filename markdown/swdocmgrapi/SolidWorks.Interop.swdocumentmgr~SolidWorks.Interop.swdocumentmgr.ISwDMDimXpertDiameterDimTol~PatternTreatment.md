---
title: "PatternTreatment Property (ISwDMDimXpertDiameterDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDiameterDimTol"
member: "PatternTreatment"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDiameterDimTol~PatternTreatment.html"
---

# PatternTreatment Property (ISwDMDimXpertDiameterDimTol)

Gets the pattern treatment for this DimXpert diameter dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternTreatment As swDmDimXpertPatternTreatmentType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDiameterDimTol
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

See [SwDMDimXpertDiameterDimTol::PatternTreatment](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDiameterDimTol~PatternTreatment.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDiameterDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDiameterDimTol.html)
[ISwDMDimXpertDiameterDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDiameterDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
