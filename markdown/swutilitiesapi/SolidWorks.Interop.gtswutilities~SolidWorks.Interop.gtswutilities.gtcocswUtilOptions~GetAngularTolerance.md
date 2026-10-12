---
title: "GetAngularTolerance Method (gtcocswUtilOptions)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilOptions"
member: "GetAngularTolerance"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions~GetAngularTolerance.html"
---

# GetAngularTolerance Method (gtcocswUtilOptions)

Gets the angular tolerance value currently set in the registry.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAngularTolerance( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilOptions
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetAngularTolerance(lErrorcode)
```

### C#

```csharp
System.double GetAngularTolerance(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetAngularTolerance(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Angular tolerance

## VBA Syntax

See [IUtilOptions::GetAngularTolerance](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilOptions~GetAngularTolerance.html).

## See Also

[gtcocswUtilOptions Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions.html)
[gtcocswUtilOptions Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilOptions_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
