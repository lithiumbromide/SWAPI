---
title: "IGetPrimaryDatumModifiers Method (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "IGetPrimaryDatumModifiers"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~IGetPrimaryDatumModifiers.html"
---

# IGetPrimaryDatumModifiers Method (IDimXpertTolerance)

Gets all of the primary datum modifiers in this DimXpert geometric tolerance annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPrimaryDatumModifiers( _
   ByVal Count As System.Integer _
) As swDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim Count As System.Integer
Dim value As swDimXpertMaterialConditionModifier_e

value = instance.IGetPrimaryDatumModifiers(Count)
```

### C#

```csharp
swDimXpertMaterialConditionModifier_e IGetPrimaryDatumModifiers(
   System.int Count
)
```

### C++/CLI

```cpp
swDimXpertMaterialConditionModifier_e IGetPrimaryDatumModifiers(
   System.int Count
)
```

### Parameters

- `Count`: Number of primary datum modifiers

### Return Value

in-process, unmanaged C++: Pointer to an array of integers

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertTolerance::GetPrimaryDatumCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~GetPrimaryDatumCount.html) to get the value for the Count parameter.

The members of the array returned by this method map to the members of the array returned by [IGetDimXpertTolerance::IGetPrimaryDatums](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~IGetPrimaryDatums.html).

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
