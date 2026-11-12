---
title: "IGetAppliedFilters Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "IGetAppliedFilters"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetAppliedFilters.html"
---

# IGetAppliedFilters Method (IPowerSelect)

Gets a list of the filters applied in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAppliedFilters( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.IGetAppliedFilters(lErrorcode)
```

### C#

```csharp
System.int IGetAppliedFilters(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int IGetAppliedFilters(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Array of the applied filters as defined in [gtpslFilterType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslFilterType_e.html)

## VBA Syntax

See [IPowerSelect::IGetAppliedFilters](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~IGetAppliedFilters.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetAppliedFilters Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetAppliedFilters.html)
[IPowerSelect::GetAppliedFiltersCount Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetAppliedFiltersCount.html)
[IPowerSelect::RemoveFilters Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~RemoveFilters.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
