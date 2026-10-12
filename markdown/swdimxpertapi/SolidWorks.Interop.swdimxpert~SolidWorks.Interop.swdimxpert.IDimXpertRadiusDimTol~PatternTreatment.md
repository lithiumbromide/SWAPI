---
title: "PatternTreatment Property (IDimXpertRadiusDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertRadiusDimTol"
member: "PatternTreatment"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertRadiusDimTol~PatternTreatment.html"
---

# PatternTreatment Property (IDimXpertRadiusDimTol)

Gets the pattern treatment for this DimXpert radius dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternTreatment As swDimXpertPatternTreatmentType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertRadiusDimTol
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

See [DimXpertRadiusDimTol::PatternTreatment](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertRadiusDimTol~PatternTreatment.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)
[Get DimXpert Features and Annotations in a Model Example (C#)](Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm)

## See Also

[IDimXpertRadiusDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertRadiusDimTol.html)
[IDimXpertRadiusDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertRadiusDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
