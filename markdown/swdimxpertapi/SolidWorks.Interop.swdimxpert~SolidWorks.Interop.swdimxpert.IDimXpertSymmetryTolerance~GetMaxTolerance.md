---
title: "GetMaxTolerance Method (IDimXpertSymmetryTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertSymmetryTolerance"
member: "GetMaxTolerance"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance~GetMaxTolerance.html"
---

# GetMaxTolerance Method (IDimXpertSymmetryTolerance)

Gets the maximum tolerance for this DimXpert symmetry tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaxTolerance( _
   ByRef IsMax As System.Boolean, _
   ByRef Tolerance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertSymmetryTolerance
Dim IsMax As System.Boolean
Dim Tolerance As System.Double
Dim value As System.Boolean

value = instance.GetMaxTolerance(IsMax, Tolerance)
```

### C#

```csharp
System.bool GetMaxTolerance(
   out System.bool IsMax,
   out System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool GetMaxTolerance(
   [Out] System.bool IsMax,
   [Out] System.double Tolerance
)
```

### Parameters

- `IsMax`: True if maximum tolerance is set; false otherwise
- `Tolerance`: Maximum tolerance value

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertSymmetryTolerance::GetMaxTolerance](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertSymmetryTolerance~GetMaxTolerance.html).

## See Also

[IDimXpertSymmetryTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance.html)
[IDimXpertSymmetryTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSymmetryTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
