---
title: "FlowPressureFile Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "FlowPressureFile"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~FlowPressureFile.html"
---

# FlowPressureFile Property (ICWStaticStudyOptions)

Gets or sets the SOLIDWORKS Flow Simulation results file from which to import fluid pressure loads.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlowPressureFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::FlowPressureFile](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~FlowPressureFile.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

This property is valid only if [ICWStaticStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckFlowPressure.html) and [ICWStaticStudyOptions::ReferencePressureOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ReferencePressureOption.html) are both set to 1.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::CheckRunAsLegacy Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckRunAsLegacy.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
