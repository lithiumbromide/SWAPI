---
title: "ApplyNameViewOrientation2 Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ApplyNameViewOrientation2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ApplyNameViewOrientation2.html"
---

# ApplyNameViewOrientation2 Method (ICWPlot)

Associates this plot with the specified view orientation.

## Syntax

### Visual Basic (Declaration)

```vb
Function ApplyNameViewOrientation2( _
   ByVal NNameViewOrientation As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim NNameViewOrientation As System.Integer
Dim value As System.Integer

value = instance.ApplyNameViewOrientation2(NNameViewOrientation)
```

### C#

```csharp
System.int ApplyNameViewOrientation2(
   System.int NNameViewOrientation
)
```

### C++/CLI

```cpp
System.int ApplyNameViewOrientation2(
   System.int NNameViewOrientation
)
```

### Parameters

- `NNameViewOrientation`: View orientation as defined in [swsNameViewOrientation_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNameViewOrientation_e.html)

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ApplyNameViewOrientation2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ApplyNameViewOrientation2.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

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

SOLIDWORKS Simulation API 2016 SP0
