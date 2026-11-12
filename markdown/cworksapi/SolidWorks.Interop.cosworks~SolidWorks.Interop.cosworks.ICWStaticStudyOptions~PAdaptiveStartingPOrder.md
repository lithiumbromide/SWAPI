---
title: "PAdaptiveStartingPOrder Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "PAdaptiveStartingPOrder"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStartingPOrder.html"
---

# PAdaptiveStartingPOrder Property (ICWStaticStudyOptions)

Gets or sets the polynomial order at which to start the p-adaptive mesh iteration.

## Syntax

### Visual Basic (Declaration)

```vb
Property PAdaptiveStartingPOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.PAdaptiveStartingPOrder = value

value = instance.PAdaptiveStartingPOrder
```

### C#

```csharp
System.int PAdaptiveStartingPOrder {get; set;}
```

### C++/CLI

```cpp
property System.int PAdaptiveStartingPOrder {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

2 <= Starting polynomial order of the mesh <= 5

## VBA Syntax

See [CWStaticStudyOptions::PAdaptiveStartingPOrder](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~PAdaptiveStartingPOrder.html).

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
[ICWStaticStudyOptions::PAdaptiveStrainEnergyErrorLimit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStrainEnergyErrorLimit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
