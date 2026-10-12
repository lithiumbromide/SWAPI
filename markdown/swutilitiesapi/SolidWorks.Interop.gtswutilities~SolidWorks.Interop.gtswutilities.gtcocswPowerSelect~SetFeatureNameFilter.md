---
title: "SetFeatureNameFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "SetFeatureNameFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~SetFeatureNameFilter.html"
---

# SetFeatureNameFilter Method (gtcocswPowerSelect)

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
Dim instance As gtcocswPowerSelect
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

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
