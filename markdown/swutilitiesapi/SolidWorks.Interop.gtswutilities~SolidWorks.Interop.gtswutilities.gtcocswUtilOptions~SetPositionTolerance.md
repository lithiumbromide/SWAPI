---
title: "SetPositionTolerance Method (gtcocswUtilOptions)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilOptions"
member: "SetPositionTolerance"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions~SetPositionTolerance.html"
---

# SetPositionTolerance Method (gtcocswUtilOptions)

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
Dim instance As gtcocswUtilOptions
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

## Remarks

During face comparison, the position of vertex coordinates and some surface points of face pairs are compared. Vertices or points that lie within a specified position tolerance are considered identical.

## See Also

[gtcocswUtilOptions Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions.html)
[gtcocswUtilOptions Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
