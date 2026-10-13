---
title: "GetPositionTolerance Method (gtcocswUtilOptions)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilOptions"
member: "GetPositionTolerance"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions~GetPositionTolerance.html"
---

# GetPositionTolerance Method (gtcocswUtilOptions)

Gets the position tolerance currently set in the registry.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPositionTolerance( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilOptions
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetPositionTolerance(lErrorcode)
```

### C#

```csharp
System.double GetPositionTolerance(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetPositionTolerance(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Position tolerance

## VBA Syntax

See [IUtilOptions::GetPositionTolerance](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilOptions~GetPositionTolerance.html).

## See Also

[gtcocswUtilOptions Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions.html)
[gtcocswUtilOptions Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
