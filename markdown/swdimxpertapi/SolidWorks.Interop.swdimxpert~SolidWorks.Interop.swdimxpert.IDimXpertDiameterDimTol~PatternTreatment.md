---
title: "PatternTreatment Property (IDimXpertDiameterDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDiameterDimTol"
member: "PatternTreatment"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDiameterDimTol~PatternTreatment.html"
---

# PatternTreatment Property (IDimXpertDiameterDimTol)

Gets the pattern treatment for this DimXpert diameter dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternTreatment As swDimXpertPatternTreatmentType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDiameterDimTol
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

See [DimXpertDiameterDimTol::PatternTreatment](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDiameterDimTol~PatternTreatment.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)
[Get DimXpert Features and Annotations in a Model Example (C#)](Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm)

## See Also

[IDimXpertDiameterDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDiameterDimTol.html)
[IDimXpertDiameterDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDiameterDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
