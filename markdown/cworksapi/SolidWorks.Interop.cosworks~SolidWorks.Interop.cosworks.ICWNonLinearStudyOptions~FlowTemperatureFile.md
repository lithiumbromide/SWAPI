---
title: "FlowTemperatureFile Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "FlowTemperatureFile"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FlowTemperatureFile.html"
---

# FlowTemperatureFile Property (ICWNonLinearStudyOptions)

Gets or sets the SOLIDWORKS Flow Simulation result file that is used to import flow temperatures.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlowTemperatureFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
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

See [CWNonLinearStudyOptions::FlowTemperatureFile](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~FlowTemperatureFile.html).

## Remarks

This property is valid only if [ICWNonLinearStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromFlow.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
