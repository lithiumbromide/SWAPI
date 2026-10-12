---
title: "GetAppliedFiltersCount Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "GetAppliedFiltersCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~GetAppliedFiltersCount.html"
---

# GetAppliedFiltersCount Method (gtcocswPowerSelect)

Gets the number of filters applied in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAppliedFiltersCount( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.GetAppliedFiltersCount(lErrorcode)
```

### C#

```csharp
System.int GetAppliedFiltersCount(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int GetAppliedFiltersCount(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of applied filters

## VBA Syntax

See [IPowerSelect::GetAppliedFiltersCount](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetAppliedFiltersCount.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
