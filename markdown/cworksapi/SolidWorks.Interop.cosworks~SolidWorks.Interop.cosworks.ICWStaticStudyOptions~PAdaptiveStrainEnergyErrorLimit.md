---
title: "PAdaptiveStrainEnergyErrorLimit Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "PAdaptiveStrainEnergyErrorLimit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStrainEnergyErrorLimit.html"
---

# PAdaptiveStrainEnergyErrorLimit Property (ICWStaticStudyOptions)

Gets or sets the lowest relative strain energy error percent in model areas for which to apply a p-adaptive mesh iteration.

## Syntax

### Visual Basic (Declaration)

```vb
Property PAdaptiveStrainEnergyErrorLimit As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Double

instance.PAdaptiveStrainEnergyErrorLimit = value

value = instance.PAdaptiveStrainEnergyErrorLimit
```

### C#

```csharp
System.double PAdaptiveStrainEnergyErrorLimit {get; set;}
```

### C++/CLI

```cpp
property System.double PAdaptiveStrainEnergyErrorLimit {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

1.0e-006 <= Lowest relative strain energy error percent < 100.0

## VBA Syntax

See [CWStaticStudyOptions::PAdaptiveStrainEnergyErrorLimit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~PAdaptiveStrainEnergyErrorLimit.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWStaticStudyOptions::AdaptiveMethodType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~AdaptiveMethodType.html) is set to 2.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::PAdaptiveConvergenceCriteria Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveConvergenceCriteria.html)
[ICWStaticStudyOptions::PAdaptiveErrorLimit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveErrorLimit.html)
[ICWStaticStudyOptions::PAdaptiveMaxIterations Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveMaxIterations.html)
[ICWStaticStudyOptions::PAdaptiveMaxPOrder Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveMaxPOrder.html)
[ICWStaticStudyOptions::PAdaptiveStartingPOrder Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStartingPOrder.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
