---
title: "GetAppliedFilters Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "GetAppliedFilters"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~GetAppliedFilters.html"
---

# GetAppliedFilters Method (gtcocswPowerSelect)

Gets a list of the filters applied in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAppliedFilters( _
   ByRef lErrorcode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Object

value = instance.GetAppliedFilters(lErrorcode)
```

### C#

```csharp
System.object GetAppliedFilters(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.Object^ GetAppliedFilters(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Array of the applied filters as defined in [gtpslFilterType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslFilterType_e.html)

## VBA Syntax

See [IPowerSelect::GetAppliedFilters](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetAppliedFilters.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
