---
title: "Modifier Property (IDimXpertStraightnessTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertStraightnessTolerance"
member: "Modifier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance~Modifier.html"
---

# Modifier Property (IDimXpertStraightnessTolerance)

Gets the material condition modifier for this DimXpert straightness tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Modifier As swDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertStraightnessTolerance
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

See [DimXpertStraightnessTolerance::Modifier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertStraightnessTolerance~Modifier.html).

## Examples

[Get DimXpert Tolerance4 Example (VBA)](Get_DimXpert_Tolerance4_Example_VB.htm)
[Get DimXpert Tolerance4 Example (VB.NET)](Get_DimXpert_Tolerance4_Example_VBNET.htm)

## See Also

[IDimXpertStraightnessTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance.html)
[IDimXpertStraightnessTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
