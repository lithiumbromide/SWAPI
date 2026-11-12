---
title: "FatigueStrengthReductionFactor Property (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "FatigueStrengthReductionFactor"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~FatigueStrengthReductionFactor.html"
---

# FatigueStrengthReductionFactor Property (ICWFatigueStudyOptions)

Gets or sets the fatigue strength reduction factor to use when reading S-N curve data.

## Syntax

### Visual Basic (Declaration)

```vb
Property FatigueStrengthReductionFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim value As System.Double

instance.FatigueStrengthReductionFactor = value

value = instance.FatigueStrengthReductionFactor
```

### C#

```csharp
System.double FatigueStrengthReductionFactor {get; set;}
```

### C++/CLI

```cpp
property System.double FatigueStrengthReductionFactor {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 <= fatigue strength reduction factor <= 1.0 (see **Remarks**)

## VBA Syntax

See [CWFatigueStudyOptions::FatigueStrengthReductionFactor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~FatigueStrengthReductionFactor.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## Remarks

Use this factor to account for differences between the test environment that is used to generate the S-N curve and the actual loading environment. The program divides the alternating stress by this factor before reading the corresponding number of cycles from the S-N curve. This is equivalent to reducing the number of cycles that causes failure at a certain alternating stress.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::ComputingAlternatingStressOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~ComputingAlternatingStressOption.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
