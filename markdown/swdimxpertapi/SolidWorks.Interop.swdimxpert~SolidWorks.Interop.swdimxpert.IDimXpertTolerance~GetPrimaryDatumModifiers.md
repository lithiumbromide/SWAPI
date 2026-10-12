---
title: "GetPrimaryDatumModifiers Method (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "GetPrimaryDatumModifiers"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~GetPrimaryDatumModifiers.html"
---

# GetPrimaryDatumModifiers Method (IDimXpertTolerance)

Gets all of the primary datum modifiers in this DimXpert geometric tolerance annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrimaryDatumModifiers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim value As System.Object

value = instance.GetPrimaryDatumModifiers()
```

### C#

```csharp
System.object GetPrimaryDatumModifiers()
```

### C++/CLI

```cpp
System.Object^ GetPrimaryDatumModifiers();
```

### Return Value

Array of integers as defined in [swDimXpertMaterialConditionModifier_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertMaterialConditionModifier_e.html)

## VBA Syntax

See [DimXpertTolerance::GetPrimaryDatumModifiers](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertTolerance~GetPrimaryDatumModifiers.html).

## Remarks

The members of the array returned by this method map to the members of the array returned by [IGetDimXpertTolerance::GetPrimaryDatums](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~GetPrimaryDatums.html).

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
