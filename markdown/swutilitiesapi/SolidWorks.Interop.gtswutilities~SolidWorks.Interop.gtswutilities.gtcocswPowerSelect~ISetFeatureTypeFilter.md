---
title: "ISetFeatureTypeFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "ISetFeatureTypeFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~ISetFeatureTypeFilter.html"
---

# ISetFeatureTypeFilter Method (gtcocswPowerSelect)

Sets the types of features for this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetFeatureTypeFilter( _
   ByVal lFeatCount As System.Integer, _
   ByRef pFeatArr As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lFeatCount As System.Integer
Dim pFeatArr As System.Integer
Dim value As System.Integer

value = instance.ISetFeatureTypeFilter(lFeatCount, pFeatArr)
```

### C#

```csharp
System.int ISetFeatureTypeFilter(
   System.int lFeatCount,
   ref System.int pFeatArr
)
```

### C++/CLI

```cpp
System.int ISetFeatureTypeFilter(
   System.int lFeatCount,
   System.int% pFeatArr
)
```

### Parameters

- `lFeatCount`: Number of features
- `pFeatArr`: Array of features as defined in [gtpslFeatureType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtpslFeatureType_e.html)

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::ISetFeatureTypeFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~ISetFeatureTypeFilter.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
