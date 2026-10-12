---
title: "FlowPressureFile Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "FlowPressureFile"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~FlowPressureFile.html"
---

# FlowPressureFile Property (ICWBucklingStudyOptions)

Gets or sets the SOLIDWORKS Flow Simulation results file from which to import fluid pressure loads.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlowPressureFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::FlowPressureFile](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~FlowPressureFile.html).

## Remarks

This property is valid only if [ICWBucklingStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~CheckFlowPressure.html) and [ICWBucklingStudyOptions::ReferencePressureOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ReferencePressureOption.html) are both set to 1.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)
[ICWBucklingStudyOptions::CheckRunAsLegacy Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~CheckRunAsLegacy.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
