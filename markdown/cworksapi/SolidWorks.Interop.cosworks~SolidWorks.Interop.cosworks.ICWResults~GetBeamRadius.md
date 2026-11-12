---
title: "GetBeamRadius Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetBeamRadius"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamRadius.html"
---

# GetBeamRadius Method (ICWResults)

Gets the radii of beams used to render the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBeamRadius( _
   ByVal SPlotName As System.String, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetBeamRadius(SPlotName, ErrorCode)
```

### C#

```csharp
System.object GetBeamRadius(
   System.string SPlotName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetBeamRadius(
   System.String^ SPlotName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SPlotName`: Name of plot
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of beam radii

## VBA Syntax

See [CWResults::GetBeamRadius](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetBeamRadius.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetBeamForcesForEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamForcesForEntities.html)
[ICWResults::GetBeamMinMaxStress Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamMinMaxStress.html)
[ICWResults::GetBeamStressForEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamStressForEntities.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
