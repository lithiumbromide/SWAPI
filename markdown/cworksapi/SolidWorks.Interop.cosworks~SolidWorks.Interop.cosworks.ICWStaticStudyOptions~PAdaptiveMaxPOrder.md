---
title: "PAdaptiveMaxPOrder Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "PAdaptiveMaxPOrder"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveMaxPOrder.html"
---

# PAdaptiveMaxPOrder Property (ICWStaticStudyOptions)

Gets or sets the maximum polynomial order of the mesh at which to end the p-adaptive mesh iteration.

## Syntax

### Visual Basic (Declaration)

```vb
Property PAdaptiveMaxPOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.PAdaptiveMaxPOrder = value

value = instance.PAdaptiveMaxPOrder
```

### C#

```csharp
System.int PAdaptiveMaxPOrder {get; set;}
```

### C++/CLI

```cpp
property System.int PAdaptiveMaxPOrder {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

2 <= Maximum polynomial order of the mesh at which to end iteration <= 5

## VBA Syntax

See [CWStaticStudyOptions::PAdaptiveMaxPOrder](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~PAdaptiveMaxPOrder.html).

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
[ICWStaticStudyOptions::PAdaptiveStartingPOrder Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStartingPOrder.html)
[ICWStaticStudyOptions::PAdaptiveStrainEnergyErrorLimit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStrainEnergyErrorLimit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
