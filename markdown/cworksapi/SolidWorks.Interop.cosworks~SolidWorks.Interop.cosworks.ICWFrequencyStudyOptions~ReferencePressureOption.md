---
title: "ReferencePressureOption Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "ReferencePressureOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~ReferencePressureOption.html"
---

# ReferencePressureOption Property (ICWFrequencyStudyOptions)

Gets or sets whether to use the reference pressure offset defined in the Flow Simulation results file to subtract from imported pressure values.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePressureOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
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

See [CWFrequencyStudyOptions::ReferencePressureOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~ReferencePressureOption.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWFrequencyStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckFlowPressure.html) is set to 1.

| If you set this property to... | Then you must set... |
| --- | --- |
| 0 | ICWFrequencyStudyOptions::DefinedReferencePressure |
| 1 | ICWFrequencyStudyOptions::FlowPressureFile |

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
