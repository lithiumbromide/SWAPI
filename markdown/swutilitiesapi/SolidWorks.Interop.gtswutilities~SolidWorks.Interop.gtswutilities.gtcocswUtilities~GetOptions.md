---
title: "GetOptions Method (gtcocswUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilities"
member: "GetOptions"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities~GetOptions.html"
---

# GetOptions Method (gtcocswUtilities)

Gets the SOLIDWORKS Utilities options.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOptions( _
   ByRef lErrorcode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilities
Dim lErrorcode As System.Integer
Dim value As System.Object

value = instance.GetOptions(lErrorcode)
```

### C#

```csharp
System.object GetOptions(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.Object^ GetOptions(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Pointer to an array of options

## VBA Syntax

See [IUtilities::GetOptions](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~GetOptions.html).

## See Also

[gtcocswUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities.html)
[gtcocswUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
