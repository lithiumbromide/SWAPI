---
title: "Modifier Property (IDimXpertConcentricityTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertConcentricityTolerance"
member: "Modifier"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConcentricityTolerance~Modifier.html"
---

# Modifier Property (IDimXpertConcentricityTolerance)

Gets the material condition modifier for this DimXpert concentricity tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Modifier As swDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertConcentricityTolerance
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

See [DimXpertConcentricityTolerance::Modifier](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertConcentricityTolerance~Modifier.html).

## Examples

[Get DimXpert Tolerance5 Example (VBA)](Get_DimXpert_Tolerance5_Example_VB.htm)
[Get DimXpert Tolerance5 Example (VB.NET)](Get_DimXpert_Tolerance5_Example_VBNET.htm)

## See Also

[IDimXpertConcentricityTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConcentricityTolerance.html)
[IDimXpertConcentricityTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConcentricityTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
