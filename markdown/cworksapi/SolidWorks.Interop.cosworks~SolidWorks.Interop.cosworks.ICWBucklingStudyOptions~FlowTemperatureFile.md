---
title: "FlowTemperatureFile Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "FlowTemperatureFile"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~FlowTemperatureFile.html"
---

# FlowTemperatureFile Property (ICWBucklingStudyOptions)

Gets or sets the SOLIDWORKS Flow Simulation result file that is used to import flow temperatures.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlowTemperatureFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::FlowTemperatureFile](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~FlowTemperatureFile.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWBucklingStudyOptions::ThermalResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ThermalResults.html) is set to [swsThermalOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html).swsThermalOption_TemperatureFromFlow.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
