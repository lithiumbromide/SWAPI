---
title: "SetEdgeAngleFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "SetEdgeAngleFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~SetEdgeAngleFilter.html"
---

# SetEdgeAngleFilter Method (gtcocswPowerSelect)

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
Dim instance As gtcocswPowerSelect
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

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
