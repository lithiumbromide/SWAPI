---
title: "GetPlotDefinition Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetPlotDefinition"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDefinition.html"
---

# GetPlotDefinition Method (ICWResults)

Gets the definition of the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlotDefinition( _
   ByVal SPlotName As System.String, _
   ByRef NPlotType As System.Integer, _
   ByRef NComponentName As System.String, _
   ByRef BNodal As System.Boolean, _
   ByRef BDeformed As System.Boolean, _
   ByRef DScaleFactor As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim NPlotType As System.Integer
Dim NComponentName As System.String
Dim BNodal As System.Boolean
Dim BDeformed As System.Boolean
Dim DScaleFactor As System.Double
Dim value As System.Integer

value = instance.GetPlotDefinition(SPlotName, NPlotType, NComponentName, BNodal, BDeformed, DScaleFactor)
```

### C#

```csharp
System.int GetPlotDefinition(
   System.string SPlotName,
   out System.int NPlotType,
   out System.string NComponentName,
   out System.bool BNodal,
   out System.bool BDeformed,
   out System.double DScaleFactor
)
```

### C++/CLI

```cpp
System.int GetPlotDefinition(
   System.String^ SPlotName,
   [Out] System.int NPlotType,
   [Out] System.String^ NComponentName,
   [Out] System.bool BNodal,
   [Out] System.bool BDeformed,
   [Out] System.double DScaleFactor
)
```

### Parameters

- `SPlotName`: Name of plot
- `NPlotType`: Type of plot as defined in [swsPlotResultTypes_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPlotResultTypes_e.html)
- `NComponentName`: Name of plotted component
- `BNodal`: True if plot is nodal, false if elemental
- `BDeformed`: True if deformed, false if not
- `DScaleFactor`: Scale factor for deformation

### Return Value

Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

## VBA Syntax

See [CWResults::GetPlotDefinition](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetPlotDefinition.html).

## Examples

[Create Body From Deformed Shape (VBA)](Create_Body_From_Deformed_Shape_Example_VB.htm)
[Create Body From Deformed Shape (VB.NET)](Create_Body_From_Deformed_Shape_Example_VBNET.htm)
[Create Body From Deformed Shape (C#)](Create_Body_From_Deformed_Shape_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::GetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html)
[ICWResults::GetPlotNames Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html)
[ICWResults::GetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html)
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)
[ICWResults::GetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
