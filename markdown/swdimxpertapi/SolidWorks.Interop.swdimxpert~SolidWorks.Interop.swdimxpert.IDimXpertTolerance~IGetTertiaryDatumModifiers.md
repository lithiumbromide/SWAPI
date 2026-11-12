---
title: "IGetTertiaryDatumModifiers Method (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "IGetTertiaryDatumModifiers"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~IGetTertiaryDatumModifiers.html"
---

# IGetTertiaryDatumModifiers Method (IDimXpertTolerance)

Gets all of the tertiary datum modifiers in this DimXpert geometric tolerance annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTertiaryDatumModifiers( _
   ByVal Count As System.Integer _
) As swDimXpertMaterialConditionModifier_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim Count As System.Integer
Dim value As swDimXpertMaterialConditionModifier_e

value = instance.IGetTertiaryDatumModifiers(Count)
```

### C#

```csharp
swDimXpertMaterialConditionModifier_e IGetTertiaryDatumModifiers(
   System.int Count
)
```

### C++/CLI

```cpp
swDimXpertMaterialConditionModifier_e IGetTertiaryDatumModifiers(
   System.int Count
)
```

### Parameters

- `Count`: Number of tertiary datum modifiers

### Return Value

in-process, unmanaged C++: Pointer to an array of integers

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertTolerance::GetTertiaryDatumCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~GetTertiaryDatumCount.html) to get the value for the Count parameter.

The members of the array returned by this method map to the members of the array returned by [IGetDimXpertTolerance::IGetTertiaryDatums](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~IGetTertiaryDatums.html).

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
