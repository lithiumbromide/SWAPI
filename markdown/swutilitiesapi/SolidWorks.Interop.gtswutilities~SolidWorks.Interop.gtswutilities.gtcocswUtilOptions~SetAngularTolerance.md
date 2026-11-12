---
title: "SetAngularTolerance Method (gtcocswUtilOptions)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilOptions"
member: "SetAngularTolerance"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions~SetAngularTolerance.html"
---

# SetAngularTolerance Method (gtcocswUtilOptions)

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
Dim instance As gtcocswUtilOptions
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

## Remarks

During face comparison, the parallelism of the edges of face pairs are compared. If the edges are curved, tangents to the curves are compared. The faces are identical if the angle between their corresponding edges is less than the specified angle tolerance.

## See Also

[gtcocswUtilOptions Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions.html)
[gtcocswUtilOptions Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
