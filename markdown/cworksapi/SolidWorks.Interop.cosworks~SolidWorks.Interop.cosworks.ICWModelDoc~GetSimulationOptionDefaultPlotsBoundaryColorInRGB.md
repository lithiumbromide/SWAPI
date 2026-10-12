---
title: "GetSimulationOptionDefaultPlotsBoundaryColorInRGB Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "GetSimulationOptionDefaultPlotsBoundaryColorInRGB"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionDefaultPlotsBoundaryColorInRGB.html"
---

# GetSimulationOptionDefaultPlotsBoundaryColorInRGB Method (ICWModelDoc)

Gets the RGB color for the specified default plot boundary option.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSimulationOptionDefaultPlotsBoundaryColorInRGB( _
   ByVal NBoundaryOption As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NBoundaryOption As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetSimulationOptionDefaultPlotsBoundaryColorInRGB(NBoundaryOption, ErrorCode)
```

### C#

```csharp
System.object GetSimulationOptionDefaultPlotsBoundaryColorInRGB(
   System.int NBoundaryOption,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetSimulationOptionDefaultPlotsBoundaryColorInRGB(
   System.int NBoundaryOption,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NBoundaryOption`: Boundary option as defined in [swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e.html)
- `ErrorCode`: Error code as defined in [swsSimulationOptionDefaultPlotsBoundaryColorInRGBError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimulationOptionDefaultPlotsBoundaryColorInRGBError_e.html)

### Return Value

Array of three values; [0-255][0-255][0-255]

## VBA Syntax

See [CWModelDoc::GetSimulationOptionDefaultPlotsBoundaryColorInRGB](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~GetSimulationOptionDefaultPlotsBoundaryColorInRGB.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::SetSimulationOptionDefaultPlotsBoundaryColorInRGB Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionDefaultPlotsBoundaryColorInRGB.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
