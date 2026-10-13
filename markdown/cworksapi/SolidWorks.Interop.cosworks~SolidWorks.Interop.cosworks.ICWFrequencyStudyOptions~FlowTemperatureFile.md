---
title: "FlowTemperatureFile Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "FlowTemperatureFile"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FlowTemperatureFile.html"
---

# FlowTemperatureFile Property (ICWFrequencyStudyOptions)

Gets or sets the SOLIDWORKS Flow Simulation result file that is used to import flow temperatures.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlowTemperatureFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
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

Full path name of a SOLIDWORKS Flow Simulation result file (***.fld**)

## VBA Syntax

See [CWFrequencyStudyOptions::FlowTemperatureFile](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~FlowTemperatureFile.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromFlow.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
