---
title: "ReferencePressureOption Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "ReferencePressureOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ReferencePressureOption.html"
---

# ReferencePressureOption Property (ICWNonLinearStudyOptions)

Gets or sets whether to use the reference pressure offset defined in the Flow Simulation results file to subtract from imported pressure values.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePressureOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
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

See [CWNonLinearStudyOptions::ReferencePressureOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~ReferencePressureOption.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWNonLinearStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckFlowPressure.html) is set to 1.

| If you set this property to... | Then you must also set... |
| --- | --- |
| 0 | ICWNonLinearStudyOptions::DefinedReferencePressure |
| 1 | ICWNonLinearStudyOptions::FlowPressureFile |

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
