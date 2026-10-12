---
title: "ComputingAlternatingStressOption Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "ComputingAlternatingStressOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ComputingAlternatingStressOption.html"
---

# ComputingAlternatingStressOption Property (ICWFatigueStudyOptions)

Gets or sets the stress type used to calculate alternating stress.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComputingAlternatingStressOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim value As System.Integer

instance.ComputingAlternatingStressOption = value

value = instance.ComputingAlternatingStressOption
```

### C#

```csharp
System.int ComputingAlternatingStressOption {get; set;}
```

### C++/CLI

```cpp
property System.int ComputingAlternatingStressOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Stress type as defined in [swsFatigueAlternatingStressOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueAlternatingStressOption_e.html)

## VBA Syntax

See [CWFatigueStudyOptions::ComputingAlternatingStressOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~ComputingAlternatingStressOption.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## Remarks

This property is valid only for constant and variable amplitude fatigue studies.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
