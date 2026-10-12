---
title: "IGetFeatureTypeFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "IGetFeatureTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetFeatureTypeFilter.html"
---

# IGetFeatureTypeFilter Method (IPowerSelect)

Gets the types of features set in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatureTypeFilter( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.IGetFeatureTypeFilter(lErrorcode)
```

### C#

```csharp
System.int IGetFeatureTypeFilter(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int IGetFeatureTypeFilter(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Array of features as defined in [gtpslFeatureType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslFeatureType_e.html)

## VBA Syntax

See [IPowerSelect::IGetFeatureTypeFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~IGetFeatureTypeFilter.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureTypeFilter.html)
[IPowerSelect::GetFeatureTypeFilterCount Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureTypeFilterCount.html)
[IPowerSelect::ISetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~ISetFeatureTypeFilter.html)
[IPowerSelect::SetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFeatureTypeFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
