---
title: "SetEdgeAngleFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "SetEdgeAngleFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetEdgeAngleFilter.html"
---

# SetEdgeAngleFilter Method (IPowerSelect)

Sets the Edge angle filter for this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEdgeAngleFilter( _
   ByVal lCmpOperator As System.Integer, _
   ByVal dAngle As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lCmpOperator As System.Integer
Dim dAngle As System.Double
Dim value As System.Integer

value = instance.SetEdgeAngleFilter(lCmpOperator, dAngle)
```

### C#

```csharp
System.int SetEdgeAngleFilter(
   System.int lCmpOperator,
   System.double dAngle
)
```

### C++/CLI

```cpp
System.int SetEdgeAngleFilter(
   System.int lCmpOperator,
   System.double dAngle
)
```

### Parameters

- `lCmpOperator`: Comparison operator as defined in [gtpslEdgeAngleOperator_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslEdgeAngleOperator_e.html)
- `dAngle`: Angle in radians

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SetEdgeAngleFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SetEdgeAngleFilter.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetEdgeAngleFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetEdgeAngleFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
