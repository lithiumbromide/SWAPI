---
title: "SetFeatureColorFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "SetFeatureColorFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFeatureColorFilter.html"
---

# SetFeatureColorFilter Method (IPowerSelect)

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
Dim instance As IPowerSelect
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

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetFeatureColorFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFeatureColorFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
