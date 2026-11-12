---
title: "Modifier Property (IDimXpertSymmetryTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertSymmetryTolerance"
member: "Modifier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance~Modifier.html"
---

# Modifier Property (IDimXpertSymmetryTolerance)

Gets the material condition modifier for this Dimxpert symmetry tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Modifier As swDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertSymmetryTolerance
Dim value As swDimXpertMaterialConditionModifier_e

value = instance.Modifier
```

### C#

```csharp
swDimXpertMaterialConditionModifier_e Modifier {get;}
```

### C++/CLI

```cpp
property swDimXpertMaterialConditionModifier_e Modifier {
   swDimXpertMaterialConditionModifier_e get();
}
```

### Property Value

Material condition modifier as defined in [swDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertMaterialConditionModifier_e.html)

## VBA Syntax

See [DimXpertSymmetryTolerance::Modifier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertSymmetryTolerance~Modifier.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)

## See Also

[IDimXpertSymmetryTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance.html)
[IDimXpertSymmetryTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
