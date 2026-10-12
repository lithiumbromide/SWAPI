---
title: "FlowPressureFile Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "FlowPressureFile"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FlowPressureFile.html"
---

# FlowPressureFile Property (ICWNonLinearStudyOptions)

Gets or sets the SOLIDWORKS Flow Simulation results file from which to import fluid pressure loads.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlowPressureFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.String

instance.FlowPressureFile = value

value = instance.FlowPressureFile
```

### C#

```csharp
System.string FlowPressureFile {get; set;}
```

### C++/CLI

```cpp
property System.String^ FlowPressureFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Full path name of a SOLIDWORKS Flow Simulation results file (***.fld**)

## VBA Syntax

See [CWNonLinearStudyOptions::FlowPressureFile](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~FlowPressureFile.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWNonLinearStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckFlowPressure.html) and [ICWNonLinearStudyOptions::ReferencePressureOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ReferencePressureOption.html) are both set to 1.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::CheckRunAsLegacy Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckRunAsLegacy.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
