---
title: "GetFeatureTypeFilterCount Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "GetFeatureTypeFilterCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~GetFeatureTypeFilterCount.html"
---

# GetFeatureTypeFilterCount Method (gtcocswPowerSelect)

Gets the number of types of features set in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureTypeFilterCount( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.GetFeatureTypeFilterCount(lErrorcode)
```

### C#

```csharp
System.int GetFeatureTypeFilterCount(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int GetFeatureTypeFilterCount(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error code as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of types of features

## VBA Syntax

See [IPowerSelect::GetFeatureTypeFilterCount](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetFeatureTypeFilterCount.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
