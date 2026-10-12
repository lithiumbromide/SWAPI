---
title: "ReferencePressureOption Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "ReferencePressureOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ReferencePressureOption.html"
---

# ReferencePressureOption Property (ICWBucklingStudyOptions)

Gets or sets whether to use the reference pressure offset defined in the Flow Simulation results file to subtract from imported pressure values.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePressureOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::ReferencePressureOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~ReferencePressureOption.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWBucklingStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~CheckFlowPressure.html) is set to 1.

| If you set this property to... | Then you must set... |
| --- | --- |
| 0 | ICWBucklingStudyOptions::DefinedReferencePressure |
| 1 | ICWBucklingStudyOptions::FlowPressureFile |

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
