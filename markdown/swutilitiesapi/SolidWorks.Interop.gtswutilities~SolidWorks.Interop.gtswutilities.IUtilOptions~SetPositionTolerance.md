---
title: "SetPositionTolerance Method (IUtilOptions)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilOptions"
member: "SetPositionTolerance"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions~SetPositionTolerance.html"
---

# SetPositionTolerance Method (IUtilOptions)

Sets the position tolerance for the face comparison.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPositionTolerance( _
   ByVal pTol As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilOptions
Dim pTol As System.Double
Dim value As System.Integer

value = instance.SetPositionTolerance(pTol)
```

### C#

```csharp
System.int SetPositionTolerance(
   System.double pTol
)
```

### C++/CLI

```cpp
System.int SetPositionTolerance(
   System.double pTol
)
```

### Parameters

- `pTol`: Position tolerance

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IUtilOptions::SetPositionTolerance](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilOptions~SetPositionTolerance.html).

## Examples

[Set Tolerances and Compare Geometry (VBA)](Set_Tolerances_and_Compare_Geometry_VB6.htm)
[Set Tolerances and Compare Geometry (VB.NET)](Set_Tolerances_and_Compare_Geometry_VBNET.htm)
[Set Tolerances and Compare Geometry (C#)](Set_Tolerances_and_Compare_Geometry_CSharp.htm)

## Remarks

During face comparison, the position of vertex coordinates and some surface points of face pairs are compared. Vertices or points that lie within a specified position tolerance are considered identical.

## See Also

[IUtilOptions Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions.html)
[IUtilOptions Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
