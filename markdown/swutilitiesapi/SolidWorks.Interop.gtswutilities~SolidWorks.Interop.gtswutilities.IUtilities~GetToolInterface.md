---
title: "GetToolInterface Method (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "GetToolInterface"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~GetToolInterface.html"
---

# GetToolInterface Method (IUtilities)

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
Dim instance As IUtilities
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

## Examples

[Analyze Geometry (VBA)](Analyze_Geometry_VB6.htm)
[Compare Documents (VBA)](Compare_Documents_VB6.htm)
[Compare Features (VBA)](Compare_Features_VB6.htm)
[Compare Geometry (VBA)](Compare_Geometry_VB6.htm)
[Paint Features (VBA)](Paint_Features_VB6.htm)
[Compare Geometry (VB.NET)](Compare_Geometry_VBNET.htm)
[Compare Geometry (C#)](Compare_Geometry_CSharp.htm)

## See Also

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
