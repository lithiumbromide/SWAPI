---
title: "PAdaptiveConvergenceCriteria Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "PAdaptiveConvergenceCriteria"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveConvergenceCriteria.html"
---

# PAdaptiveConvergenceCriteria Property (ICWStaticStudyOptions)

Gets or sets the criterion with which to determine convergence of the p-adaptive mesh iteration.

## Syntax

### Visual Basic (Declaration)

```vb
Property PAdaptiveConvergenceCriteria As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.PAdaptiveConvergenceCriteria = value

value = instance.PAdaptiveConvergenceCriteria
```

### C#

```csharp
System.int PAdaptiveConvergenceCriteria {get; set;}
```

### C++/CLI

```cpp
property System.int PAdaptiveConvergenceCriteria {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 0 = RMS Resultant Displacement
- 1 = RMS von Mises Stress
- 2 = Total Strain Energy

## VBA Syntax

See [CWStaticStudyOptions::PAdaptiveConvergenceCriteria](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~PAdaptiveConvergenceCriteria.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWStaticStudyOptions::AdaptiveMethodType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~AdaptiveMethodType.html) is set to 2.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::PAdaptiveErrorLimit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveErrorLimit.html)
[ICWStaticStudyOptions::PAdaptiveMaxIterations Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveMaxIterations.html)
[ICWStaticStudyOptions::PAdaptiveMaxPOrder Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveMaxPOrder.html)
[ICWStaticStudyOptions::PAdaptiveStartingPOrder Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStartingPOrder.html)
[ICWStaticStudyOptions::PAdaptiveStrainEnergyErrorLimit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStrainEnergyErrorLimit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
