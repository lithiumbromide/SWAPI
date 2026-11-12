---
title: "GetFeatureColorFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "GetFeatureColorFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~GetFeatureColorFilter.html"
---

# GetFeatureColorFilter Method (gtcocswPowerSelect)

Gets the Feature color filter set in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureColorFilter( _
   ByRef Red As System.Double, _
   ByRef Green As System.Double, _
   ByRef Blue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim Red As System.Double
Dim Green As System.Double
Dim Blue As System.Double
Dim value As System.Integer

value = instance.GetFeatureColorFilter(Red, Green, Blue)
```

### C#

```csharp
System.int GetFeatureColorFilter(
   out System.double Red,
   out System.double Green,
   out System.double Blue
)
```

### C++/CLI

```cpp
System.int GetFeatureColorFilter(
   [Out] System.double Red,
   [Out] System.double Green,
   [Out] System.double Blue
)
```

### Parameters

- `Red`: <=0.0 to <= 1.0
- `Green`: <=0.0 to <= 1.0
- `Blue`: <=0.0 to <= 1.0

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::GetFeatureColorFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetFeatureColorFilter.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
