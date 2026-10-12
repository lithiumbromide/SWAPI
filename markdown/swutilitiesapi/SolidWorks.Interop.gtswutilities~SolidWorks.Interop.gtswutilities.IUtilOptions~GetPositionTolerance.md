---
title: "GetPositionTolerance Method (IUtilOptions)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilOptions"
member: "GetPositionTolerance"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions~GetPositionTolerance.html"
---

# GetPositionTolerance Method (IUtilOptions)

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
Dim instance As IUtilOptions
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

[IUtilOptions Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions.html)
[IUtilOptions Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
