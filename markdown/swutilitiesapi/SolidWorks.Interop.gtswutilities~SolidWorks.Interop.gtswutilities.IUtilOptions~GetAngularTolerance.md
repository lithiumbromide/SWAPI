---
title: "GetAngularTolerance Method (IUtilOptions)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilOptions"
member: "GetAngularTolerance"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions~GetAngularTolerance.html"
---

# GetAngularTolerance Method (IUtilOptions)

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
Dim instance As IUtilOptions
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

[IUtilOptions Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions.html)
[IUtilOptions Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilOptions_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
