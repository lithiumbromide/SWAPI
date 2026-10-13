---
title: "SetPlotTitle Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "SetPlotTitle"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetPlotTitle.html"
---

# SetPlotTitle Method (ICWPlot)

Sets a title for this plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlotTitle( _
   ByVal SPlotTitle As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim SPlotTitle As System.String
Dim value As System.Integer

value = instance.SetPlotTitle(SPlotTitle)
```

### C#

```csharp
System.int SetPlotTitle(
   System.string SPlotTitle
)
```

### C++/CLI

```cpp
System.int SetPlotTitle(
   System.String^ SPlotTitle
)
```

### Parameters

- `SPlotTitle`: Plot title

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::SetPlotTitle](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~SetPlotTitle.html).

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

SOLIDWORKS Simulation API 2015 SP0
