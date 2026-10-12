---
title: "Modifier Property (IDimXpertPositionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPositionTolerance"
member: "Modifier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance~Modifier.html"
---

# Modifier Property (IDimXpertPositionTolerance)

Gets the material condition modifier for this DimXpert position tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Modifier As swDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPositionTolerance
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

See [DimXpertPositionTolerance::Modifier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPositionTolerance~Modifier.html).

## Examples

[Get DimXpert Tolerance3 Example (VBA)](Get_DimXpert_Tolerance3_Example_VB.htm)
[Get DimXpert Tolerance3 Example (VB.NET)](Get_DimXpert_Tolerance3_Example_VBNET.htm)

## See Also

[IDimXpertPositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance.html)
[IDimXpertPositionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
