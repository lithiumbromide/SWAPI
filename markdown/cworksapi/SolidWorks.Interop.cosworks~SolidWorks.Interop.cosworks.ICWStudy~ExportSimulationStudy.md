---
title: "ExportSimulationStudy Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "ExportSimulationStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ExportSimulationStudy.html"
---

# ExportSimulationStudy Method (ICWStudy)

Exports this study to the specified finite-element analysis program.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportSimulationStudy( _
   ByVal SLocationPath As System.String, _
   ByVal SFileName As System.String, _
   ByVal NFormat As System.Integer, _
   ByVal NNodeOffset As System.Integer, _
   ByVal NElementOffset As System.Integer, _
   ByVal NOption As System.Integer, _
   ByVal NUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim SLocationPath As System.String
Dim SFileName As System.String
Dim NFormat As System.Integer
Dim NNodeOffset As System.Integer
Dim NElementOffset As System.Integer
Dim NOption As System.Integer
Dim NUnit As System.Integer
Dim value As System.Integer

value = instance.ExportSimulationStudy(SLocationPath, SFileName, NFormat, NNodeOffset, NElementOffset, NOption, NUnit)
```

### C#

```csharp
System.int ExportSimulationStudy(
   System.string SLocationPath,
   System.string SFileName,
   System.int NFormat,
   System.int NNodeOffset,
   System.int NElementOffset,
   System.int NOption,
   System.int NUnit
)
```

### C++/CLI

```cpp
System.int ExportSimulationStudy(
   System.String^ SLocationPath,
   System.String^ SFileName,
   System.int NFormat,
   System.int NNodeOffset,
   System.int NElementOffset,
   System.int NOption,
   System.int NUnit
)
```

### Parameters

- `SLocationPath`: Path to which to export this study
- `SFileName`: Name of file to which to export this study
- `NFormat`:

  | If nOption is swsStudyExportOption_e... | nFormat is... |
  | --- | --- |
  | swsStudyExport_Cosmos | Export option as defined by swsCosmosExportOption_e |
  | swsStudyExport_Nastran | Format in which to export this study as defined by swsNastranExportOption_e |
  | swsStudyExport_Abacus, swsStudyExport_Ansys, swsStudyExport_Exodus, swsStudyExport_IdeasUniversal, or swsStudyExport_PatranNeutral | Not valid |
- `NNodeOffset`: Starting node for exported data; the lowest node label in the generated file is NNodeOffset + 1
- `NElementOffset`: Starting element for exported data; the lowest element label in the generated file is NElementOffset + 1
- `NOption`: Finite-element analysis program to which to export as defined by [swsStudyExportOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStudyExportOption_e.html)
- `NUnit`:

  | If nOption is swsStudyExportOption_e... | nUnit is... |
  | --- | --- |
  | swsStudyExport_Cosmos | Defined by swsLinearUnit_e |
  | swsStudyExport_Nastran | Defined by swsNastranExportUnit_e |
  | swsStudyExport_Abacus, swsStudyExport_Ansys, swsStudyExport_Exodus, swsStudyExport_IdeasUniversal, or swsStudyExport_PatranNeutral | Not valid |

### Return Value

Error as defined in [swsStudyExportError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStudyExportError_e.html)

## VBA Syntax

See [CWStudy::ExportSimulationStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~ExportSimulationStudy.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::GenerateReport Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GenerateReport.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
