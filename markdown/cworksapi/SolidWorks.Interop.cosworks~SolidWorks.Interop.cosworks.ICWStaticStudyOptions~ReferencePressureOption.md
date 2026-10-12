---
title: "ReferencePressureOption Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "ReferencePressureOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ReferencePressureOption.html"
---

# ReferencePressureOption Property (ICWStaticStudyOptions)

Gets or sets whether to use the reference pressure offset defined in the Flow Simulation results file to subtract from imported pressure values.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePressureOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.ReferencePressureOption = value

value = instance.ReferencePressureOption
```

### C#

```csharp
System.int ReferencePressureOption {get; set;}
```

### C++/CLI

```cpp
property System.int ReferencePressureOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use the reference pressure offset defined in the Flow Simulation results file, 0 to specify the reference pressure offset

## VBA Syntax

See [CWStaticStudyOptions::ReferencePressureOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~ReferencePressureOption.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

This property is valid only if [ICWStaticStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckFlowPressure.html) is set to 1.

| If you set this property to... | Then you must also set... |
| --- | --- |
| 0 | ICWStaticStudyOptions::DefinedReferencePressure |
| 1 | ICWStaticStudyOptions::FlowPressureFile |

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
