---
title: "GetProjectedZone Method (IDimXpertOrientationTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertOrientationTolerance"
member: "GetProjectedZone"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance~GetProjectedZone.html"
---

# GetProjectedZone Method (IDimXpertOrientationTolerance)

Gets the projected zone value of this DimXpert orientation tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProjectedZone( _
   ByRef Enabled As System.Boolean, _
   ByRef Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertOrientationTolerance
Dim Enabled As System.Boolean
Dim Value As System.Double
Dim value As System.Boolean

value = instance.GetProjectedZone(Enabled, Value)
```

### C#

```csharp
System.bool GetProjectedZone(
   out System.bool Enabled,
   out System.double Value
)
```

### C++/CLI

```cpp
System.bool GetProjectedZone(
   [Out] System.bool Enabled,
   [Out] System.double Value
)
```

### Parameters

- `Enabled`: True if enabled; false otherwise
- `Value`: Projected zone value

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertOrientationTolerance::GetProjectedZone](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertOrientationTolerance~GetProjectedZone.html).

## Examples

[Get DimXpert Tolerance3 Example (VBA)](Get_DimXpert_Tolerance3_Example_VB.htm)
[Get DimXpert Tolerance3 Example (VB.NET)](Get_DimXpert_Tolerance3_Example_VBNET.htm)

## See Also

[IDimXpertOrientationTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance.html)
[IDimXpertOrientationTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
