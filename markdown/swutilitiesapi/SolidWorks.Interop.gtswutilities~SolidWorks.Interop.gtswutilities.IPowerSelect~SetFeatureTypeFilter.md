---
title: "SetFeatureTypeFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "SetFeatureTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFeatureTypeFilter.html"
---

# SetFeatureTypeFilter Method (IPowerSelect)

Sets the types of features for this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFeatureTypeFilter( _
   ByVal varFeatArr As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim varFeatArr As System.Object
Dim value As System.Integer

value = instance.SetFeatureTypeFilter(varFeatArr)
```

### C#

```csharp
System.int SetFeatureTypeFilter(
   System.object varFeatArr
)
```

### C++/CLI

```cpp
System.int SetFeatureTypeFilter(
   System.Object^ varFeatArr
)
```

### Parameters

- `varFeatArr`: Array of features as defined in [gtpslFeatureType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslFeatureType_e.html)

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SetFeatureTypeFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SetFeatureTypeFilter.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::ISetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~ISetFeatureTypeFilter.html)
[IPowerSelect::IGetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IGetFeatureTypeFilter.html)
[IPowerSelect::GetFeatureTypeFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureTypeFilter.html)
[IPowerSelect::GetFeatureTypeFilterCount Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureTypeFilterCount.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
