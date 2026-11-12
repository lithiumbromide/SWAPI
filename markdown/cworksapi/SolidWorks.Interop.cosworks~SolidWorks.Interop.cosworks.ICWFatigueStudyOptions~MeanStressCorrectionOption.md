---
title: "MeanStressCorrectionOption Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "MeanStressCorrectionOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~MeanStressCorrectionOption.html"
---

# MeanStressCorrectionOption Property (ICWFatigueStudyOptions)

Gets or sets the mean stress correction method to use in calculating alternating stresses.

## Syntax

### Visual Basic (Declaration)

```vb
Property MeanStressCorrectionOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim value As System.Integer

instance.MeanStressCorrectionOption = value

value = instance.MeanStressCorrectionOption
```

### C#

```csharp
System.int MeanStressCorrectionOption {get; set;}
```

### C++/CLI

```cpp
property System.int MeanStressCorrectionOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Mean stress correction method as defined in [swsFatigueMeanStressCorrectionType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueMeanStressCorrectionType_e.html)

## VBA Syntax

See [CWFatigueStudyOptions::MeanStressCorrectionOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~MeanStressCorrectionOption.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## Remarks

This property is valid only for constant and variable amplitude fatigue studies.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
