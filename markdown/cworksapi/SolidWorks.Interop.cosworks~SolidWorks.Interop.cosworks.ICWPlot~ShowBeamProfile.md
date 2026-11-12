---
title: "ShowBeamProfile Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ShowBeamProfile"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowBeamProfile.html"
---

# ShowBeamProfile Method (ICWPlot)

Sets whether to render a beam diagram on the actual beam geometry.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowBeamProfile( _
   ByVal BShowBeamProfile As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BShowBeamProfile As System.Boolean
Dim value As System.Integer

value = instance.ShowBeamProfile(BShowBeamProfile)
```

### C#

```csharp
System.int ShowBeamProfile(
   System.bool BShowBeamProfile
)
```

### C++/CLI

```cpp
System.int ShowBeamProfile(
   System.bool BShowBeamProfile
)
```

### Parameters

- `BShowBeamProfile`: True to render a beam diagram on the beam geometry, false to not

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ShowBeamProfile](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ShowBeamProfile.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

This method is valid only for studies with beams and the following plots:

- Displacement
- Stress

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
