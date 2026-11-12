---
title: "GetAutoPartSimplification Method (gtcocswUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilities"
member: "GetAutoPartSimplification"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities~GetAutoPartSimplification.html"
---

# GetAutoPartSimplification Method (gtcocswUtilities)

Gets a pointer the simplified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutoPartSimplification( _
   ByRef lErrorcode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilities
Dim lErrorcode As System.Integer
Dim value As System.Object

value = instance.GetAutoPartSimplification(lErrorcode)
```

### C#

```csharp
System.object GetAutoPartSimplification(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.Object^ GetAutoPartSimplification(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Pointer to the simplified configuration

## VBA Syntax

See [IUtilities::GetAutoPartSimplification](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~GetAutoPartSimplification.html).

## See Also

[gtcocswUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities.html)
[gtcocswUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
