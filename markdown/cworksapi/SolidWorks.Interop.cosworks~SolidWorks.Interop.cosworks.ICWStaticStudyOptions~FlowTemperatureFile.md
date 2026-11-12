---
title: "FlowTemperatureFile Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "FlowTemperatureFile"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~FlowTemperatureFile.html"
---

# FlowTemperatureFile Property (ICWStaticStudyOptions)

Gets or sets the SOLIDWORKS Flow Simulation results file from which to import flow temperatures.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlowTemperatureFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.String

instance.FlowTemperatureFile = value

value = instance.FlowTemperatureFile
```

### C#

```csharp
System.string FlowTemperatureFile {get; set;}
```

### C++/CLI

```cpp
property System.String^ FlowTemperatureFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Full path name of a SOLIDWORKS Flow Simulation results file (***.fld**)

## VBA Syntax

See [CWStaticStudyOptions::FlowTemperatureFile](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~FlowTemperatureFile.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

This property is valid only if [ICWStaticStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromFlow.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
