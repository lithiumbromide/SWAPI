---
title: "SetAngularTolerance Method (IUtilOptions)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilOptions"
member: "SetAngularTolerance"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions~SetAngularTolerance.html"
---

# SetAngularTolerance Method (IUtilOptions)

Sets the angular tolerance for the face comparison.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAngularTolerance( _
   ByVal pTol As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilOptions
Dim pTol As System.Double
Dim value As System.Integer

value = instance.SetAngularTolerance(pTol)
```

### C#

```csharp
System.int SetAngularTolerance(
   System.double pTol
)
```

### C++/CLI

```cpp
System.int SetAngularTolerance(
   System.double pTol
)
```

### Parameters

- `pTol`: Angular tolerance

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IUtilOptions::SetAngularTolerance](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilOptions~SetAngularTolerance.html).

## Examples

[Set Tolerances and Compare Geometry (VBA)](Set_Tolerances_and_Compare_Geometry_VB6.htm)
[Set Tolerances and Compare Geometry (VB.NET)](Set_Tolerances_and_Compare_Geometry_VBNET.htm)
[Set Tolerances and Compare Geometry (C#)](Set_Tolerances_and_Compare_Geometry_CSharp.htm)

## Remarks

During face comparison, the parallelism of the edges of face pairs are compared. If the edges are curved, tangents to the curves are compared. The faces are identical if the angle between their corresponding edges is less than the specified angle tolerance.

## See Also

[IUtilOptions Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions.html)
[IUtilOptions Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
