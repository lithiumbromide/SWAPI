---
title: "SetFOSPlot Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "SetFOSPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetFOSPlot.html"
---

# SetFOSPlot Method (ICWPlot)

Sets whether to plot the factor of safety throughout the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFOSPlot( _
   ByVal BFOSPlot As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BFOSPlot As System.Boolean
Dim value As System.Integer

value = instance.SetFOSPlot(BFOSPlot)
```

### C#

```csharp
System.int SetFOSPlot(
   System.bool BFOSPlot
)
```

### C++/CLI

```cpp
System.int SetFOSPlot(
   System.bool BFOSPlot
)
```

### Parameters

- `BFOSPlot`: True to plot the factor of safety throughout the model, false to not

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::SetFOSPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~SetFOSPlot.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
