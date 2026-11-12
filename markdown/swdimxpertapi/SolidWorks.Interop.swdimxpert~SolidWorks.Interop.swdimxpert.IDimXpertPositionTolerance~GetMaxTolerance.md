---
title: "GetMaxTolerance Method (IDimXpertPositionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPositionTolerance"
member: "GetMaxTolerance"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance~GetMaxTolerance.html"
---

# GetMaxTolerance Method (IDimXpertPositionTolerance)

Gets the maximum tolerance for this DimXpert position tolerance.

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
Dim instance As IDimXpertPositionTolerance
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

See [DimXpertPositionTolerance::GetMaxTolerance](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPositionTolerance~GetMaxTolerance.html).

## Examples

[Get DimXpert Tolerance3 Example (VBA)](Get_DimXpert_Tolerance3_Example_VB.htm)
[Get DimXpert Tolerance3 Example (VB.NET)](Get_DimXpert_Tolerance3_Example_VBNET.htm)

## See Also

[IDimXpertPositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance.html)
[IDimXpertPositionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
