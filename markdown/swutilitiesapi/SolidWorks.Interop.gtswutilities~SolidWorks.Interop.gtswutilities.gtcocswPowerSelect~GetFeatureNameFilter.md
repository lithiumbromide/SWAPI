---
title: "GetFeatureNameFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "GetFeatureNameFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~GetFeatureNameFilter.html"
---

# GetFeatureNameFilter Method (gtcocswPowerSelect)

Gets the Feature name filter set in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureNameFilter( _
   ByRef lErrorcode As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.String

value = instance.GetFeatureNameFilter(lErrorcode)
```

### C#

```csharp
System.string GetFeatureNameFilter(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.String^ GetFeatureNameFilter(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Name of feature

## VBA Syntax

See [IPowerSelect::GetFeatureNameFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetFeatureNameFilter.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
