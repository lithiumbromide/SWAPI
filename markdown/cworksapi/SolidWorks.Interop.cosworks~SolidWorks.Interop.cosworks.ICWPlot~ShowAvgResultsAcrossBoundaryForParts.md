---
title: "ShowAvgResultsAcrossBoundaryForParts Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ShowAvgResultsAcrossBoundaryForParts"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowAvgResultsAcrossBoundaryForParts.html"
---

# ShowAvgResultsAcrossBoundaryForParts Method (ICWPlot)

Sets whether to show average results at the common nodes between two components in an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowAvgResultsAcrossBoundaryForParts( _
   ByVal BAvgResultsAcrossBoundaryForParts As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BAvgResultsAcrossBoundaryForParts As System.Boolean
Dim value As System.Integer

value = instance.ShowAvgResultsAcrossBoundaryForParts(BAvgResultsAcrossBoundaryForParts)
```

### C#

```csharp
System.int ShowAvgResultsAcrossBoundaryForParts(
   System.bool BAvgResultsAcrossBoundaryForParts
)
```

### C++/CLI

```cpp
System.int ShowAvgResultsAcrossBoundaryForParts(
   System.bool BAvgResultsAcrossBoundaryForParts
)
```

### Parameters

- `BAvgResultsAcrossBoundaryForParts`: True to show average results at the common nodes between two components in the assembly, false to not

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ShowAvgResultsAcrossBoundaryForParts](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ShowAvgResultsAcrossBoundaryForParts.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

This method is valid only for stress plots of assemblies.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
