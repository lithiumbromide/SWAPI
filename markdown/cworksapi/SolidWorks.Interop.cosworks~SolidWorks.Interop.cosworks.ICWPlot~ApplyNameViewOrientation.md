---
title: "ApplyNameViewOrientation Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ApplyNameViewOrientation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ApplyNameViewOrientation.html"
---

# ApplyNameViewOrientation Method (ICWPlot)

Obsolete. Superseded by [ICWPlot::ApplyNameViewOrientation2.](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ApplyNameViewOrientation2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function ApplyNameViewOrientation( _
   ByVal SNameViewOrientation As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim SNameViewOrientation As System.String
Dim value As System.Integer

value = instance.ApplyNameViewOrientation(SNameViewOrientation)
```

### C#

```csharp
System.int ApplyNameViewOrientation(
   System.string SNameViewOrientation
)
```

### C++/CLI

```cpp
System.int ApplyNameViewOrientation(
   System.String^ SNameViewOrientation
)
```

### Parameters

- `SNameViewOrientation`: Name view orientation

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ApplyNameViewOrientation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ApplyNameViewOrientation.html).

## Remarks

This method is valid for the following plots:

- Acceleration
- Beam diagram
- Displacement
- Mode shape/amplitude
- Fatigue
- Strain
- Strain energy density
- Stress
- Thermal
- Vector

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
