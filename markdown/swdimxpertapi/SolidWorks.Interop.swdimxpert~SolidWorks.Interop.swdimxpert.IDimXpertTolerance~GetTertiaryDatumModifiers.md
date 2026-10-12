---
title: "GetTertiaryDatumModifiers Method (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "GetTertiaryDatumModifiers"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~GetTertiaryDatumModifiers.html"
---

# GetTertiaryDatumModifiers Method (IDimXpertTolerance)

Gets all of the tertiary datum modifiers in this DimXpert geometric tolerance annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTertiaryDatumModifiers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim value As System.Object

value = instance.GetTertiaryDatumModifiers()
```

### C#

```csharp
System.object GetTertiaryDatumModifiers()
```

### C++/CLI

```cpp
System.Object^ GetTertiaryDatumModifiers();
```

### Return Value

Array of integers as defined in [swDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertMaterialConditionModifier_e.html)

## VBA Syntax

See [DimXpertTolerance::GetTertiaryDatumModifiers](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertTolerance~GetTertiaryDatumModifiers.html).

## Remarks

The members of the array returned by this method map to the members of the array returned by [IGetDimXpertTolerance::GetTertiaryDatums](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~GetTertiaryDatums.html).

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
