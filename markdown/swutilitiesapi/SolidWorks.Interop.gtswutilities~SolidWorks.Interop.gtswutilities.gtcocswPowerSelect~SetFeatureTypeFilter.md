---
title: "SetFeatureTypeFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "SetFeatureTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~SetFeatureTypeFilter.html"
---

# SetFeatureTypeFilter Method (gtcocswPowerSelect)

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
Dim instance As gtcocswPowerSelect
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

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
