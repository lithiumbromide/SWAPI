---
title: "SetFeatureColorFilter Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "SetFeatureColorFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~SetFeatureColorFilter.html"
---

# SetFeatureColorFilter Method (gtcocswPowerSelect)

Sets the Feature color filter for this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFeatureColorFilter( _
   ByVal Red As System.Double, _
   ByVal Green As System.Double, _
   ByVal Blue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim Red As System.Double
Dim Green As System.Double
Dim Blue As System.Double
Dim value As System.Integer

value = instance.SetFeatureColorFilter(Red, Green, Blue)
```

### C#

```csharp
System.int SetFeatureColorFilter(
   System.double Red,
   System.double Green,
   System.double Blue
)
```

### C++/CLI

```cpp
System.int SetFeatureColorFilter(
   System.double Red,
   System.double Green,
   System.double Blue
)
```

### Parameters

- `Red`: <=0.0 to <= 1.0
- `Green`: <=0.0 to <= 1.0
- `Blue`: <=0.0 to <= 1.0

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SetFeatureColorFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SetFeatureColorFilter.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
