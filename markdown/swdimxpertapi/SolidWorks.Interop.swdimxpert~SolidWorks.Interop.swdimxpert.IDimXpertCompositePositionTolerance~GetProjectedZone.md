---
title: "GetProjectedZone Method (IDimXpertCompositePositionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositePositionTolerance"
member: "GetProjectedZone"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance~GetProjectedZone.html"
---

# GetProjectedZone Method (IDimXpertCompositePositionTolerance)

Gets the projected zone value of this DimXpert composite position tolerance.

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
Dim instance As IDimXpertCompositePositionTolerance
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

- `Enabled`: True if projected zone is in effect; false otherwise
- `Value`: Projected zone value

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompositePositionTolerance::GetProjectedZone](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositePositionTolerance~GetProjectedZone.html).

## Examples

[Get DimXpert Tolerance3 Example (VBA)](Get_DimXpert_Tolerance3_Example_VB.htm)
[Get DimXpert Tolerance3 Example (VB.NET)](Get_DimXpert_Tolerance3_Example_VBNET.htm)

## See Also

[IDimXpertCompositePositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance.html)
[IDimXpertCompositePositionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
