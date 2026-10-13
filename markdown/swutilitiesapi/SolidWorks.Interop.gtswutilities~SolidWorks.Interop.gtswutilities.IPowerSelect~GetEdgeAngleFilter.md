---
title: "GetEdgeAngleFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "GetEdgeAngleFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetEdgeAngleFilter.html"
---

# GetEdgeAngleFilter Method (IPowerSelect)

Gets the Edge angle filter set in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeAngleFilter( _
   ByRef lCmpOperator As System.Integer, _
   ByRef dAngle As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lCmpOperator As System.Integer
Dim dAngle As System.Double
Dim value As System.Integer

value = instance.GetEdgeAngleFilter(lCmpOperator, dAngle)
```

### C#

```csharp
System.int GetEdgeAngleFilter(
   out System.int lCmpOperator,
   out System.double dAngle
)
```

### C++/CLI

```cpp
System.int GetEdgeAngleFilter(
   [Out] System.int lCmpOperator,
   [Out] System.double dAngle
)
```

### Parameters

- `lCmpOperator`: Comparison operator as defined in [gtpslEdgeAngleOperator_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslEdgeAngleOperator_e.html)
- `dAngle`: Angle in radians

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::GetEdgeAngleFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetEdgeAngleFilter.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::SetEdgeAngleFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetEdgeAngleFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
