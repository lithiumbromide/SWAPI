---
title: "SetSimulationOptionDefaultPlotsBoundaryColorInRGB Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "SetSimulationOptionDefaultPlotsBoundaryColorInRGB"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionDefaultPlotsBoundaryColorInRGB.html"
---

# SetSimulationOptionDefaultPlotsBoundaryColorInRGB Method (ICWModelDoc)

Sets the RGB color for the specified default plot boundary option.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSimulationOptionDefaultPlotsBoundaryColorInRGB( _
   ByVal NBoundaryOption As System.Integer, _
   ByVal NRed As System.Integer, _
   ByVal NGreen As System.Integer, _
   ByVal NBlue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NBoundaryOption As System.Integer
Dim NRed As System.Integer
Dim NGreen As System.Integer
Dim NBlue As System.Integer
Dim value As System.Integer

value = instance.SetSimulationOptionDefaultPlotsBoundaryColorInRGB(NBoundaryOption, NRed, NGreen, NBlue)
```

### C#

```csharp
System.int SetSimulationOptionDefaultPlotsBoundaryColorInRGB(
   System.int NBoundaryOption,
   System.int NRed,
   System.int NGreen,
   System.int NBlue
)
```

### C++/CLI

```cpp
System.int SetSimulationOptionDefaultPlotsBoundaryColorInRGB(
   System.int NBoundaryOption,
   System.int NRed,
   System.int NGreen,
   System.int NBlue
)
```

### Parameters

- `NBoundaryOption`: Boundary option as defined in [swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e.html)
- `NRed`: 0 <= Red component <= 255
- `NGreen`: 0 <= Green component <= 255
- `NBlue`: 0 <= Blue component <= 255

### Return Value

Error code as defined in [swsSimulationOptionDefaultPlotsBoundaryColorInRGBError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimulationOptionDefaultPlotsBoundaryColorInRGBError_e.html)

## VBA Syntax

See [CWModelDoc::SetSimulationOptionDefaultPlotsBoundaryColorInRGB](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~SetSimulationOptionDefaultPlotsBoundaryColorInRGB.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::GetSimulationOptionDefaultPlotsBoundaryColorInRGB Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionDefaultPlotsBoundaryColorInRGB.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
