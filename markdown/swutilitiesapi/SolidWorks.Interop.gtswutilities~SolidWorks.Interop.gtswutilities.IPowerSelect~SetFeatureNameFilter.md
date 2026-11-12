---
title: "SetFeatureNameFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "SetFeatureNameFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFeatureNameFilter.html"
---

# SetFeatureNameFilter Method (IPowerSelect)

Sets the Feature name filter for this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFeatureNameFilter( _
   ByVal bstrSearchString As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim bstrSearchString As System.String
Dim value As System.Integer

value = instance.SetFeatureNameFilter(bstrSearchString)
```

### C#

```csharp
System.int SetFeatureNameFilter(
   System.string bstrSearchString
)
```

### C++/CLI

```cpp
System.int SetFeatureNameFilter(
   System.String^ bstrSearchString
)
```

### Parameters

- `bstrSearchString`: Name of feature

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SetFeatureNameFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SetFeatureNameFilter.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetFeatureNameFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureNameFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
