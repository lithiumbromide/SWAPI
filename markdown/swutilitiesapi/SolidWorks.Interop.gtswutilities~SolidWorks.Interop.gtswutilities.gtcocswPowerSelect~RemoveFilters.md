---
title: "RemoveFilters Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "RemoveFilters"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~RemoveFilters.html"
---

# RemoveFilters Method (gtcocswPowerSelect)

Removes the specified filters, if they are set, in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveFilters( _
   ByVal lFilterEnums As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lFilterEnums As System.Integer
Dim value As System.Integer

value = instance.RemoveFilters(lFilterEnums)
```

### C#

```csharp
System.int RemoveFilters(
   System.int lFilterEnums
)
```

### C++/CLI

```cpp
System.int RemoveFilters(
   System.int lFilterEnums
)
```

### Parameters

- `lFilterEnums`: Filters to remove as defined in [gtpslFilterType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslFilterType_e.html)

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::RemoveFilters](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~RemoveFilters.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
