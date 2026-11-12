---
title: "GetAppliedFiltersCount Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "GetAppliedFiltersCount"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetAppliedFiltersCount.html"
---

# GetAppliedFiltersCount Method (IPowerSelect)

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
Dim instance As IPowerSelect
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

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetAppliedFilters Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetAppliedFilters.html)
[IPowerSelect::IGetAppliedFilters Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetAppliedFilters.html)
[IPowerSelect::RemoveFilters Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~RemoveFilters.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
