---
title: "GetToolInterface Method (gtcocswUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilities"
member: "GetToolInterface"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities~GetToolInterface.html"
---

# GetToolInterface Method (gtcocswUtilities)

Gets a pointer to the SOLIDWORKS Utilities tool.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetToolInterface( _
   ByVal toolname As System.Integer, _
   ByRef lErrorcode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilities
Dim toolname As System.Integer
Dim lErrorcode As System.Integer
Dim value As System.Object

value = instance.GetToolInterface(toolname, lErrorcode)
```

### C#

```csharp
System.object GetToolInterface(
   System.int toolname,
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.Object^ GetToolInterface(
   System.int toolname,
   [Out] System.int lErrorcode
)
```

### Parameters

- `toolname`: Tool ID as defined by [gtSwTools_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtSwTools_e.html)
- `lErrorcode`: Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Pointer to the SOLIDWORKS Utilities tool interface

## VBA Syntax

See [IUtilities::GetToolInterface](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~GetToolInterface.html).

## See Also

[gtcocswUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities.html)
[gtcocswUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
