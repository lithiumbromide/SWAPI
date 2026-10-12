---
title: "PAdaptiveMaxIterations Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "PAdaptiveMaxIterations"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveMaxIterations.html"
---

# PAdaptiveMaxIterations Property (ICWStaticStudyOptions)

Gets or sets the maximum number of p-adaptive mesh iterations.

## Syntax

### Visual Basic (Declaration)

```vb
Property PAdaptiveMaxIterations As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.PAdaptiveMaxIterations = value

value = instance.PAdaptiveMaxIterations
```

### C#

```csharp
System.int PAdaptiveMaxIterations {get; set;}
```

### C++/CLI

```cpp
property System.int PAdaptiveMaxIterations {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 <= Maximum number of iterations <= 4

## VBA Syntax

See [CWStaticStudyOptions::PAdaptiveMaxIterations](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~PAdaptiveMaxIterations.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWStaticStudyOptions::AdaptiveMethodType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~AdaptiveMethodType.html) is set to 2.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::PAdaptiveConvergenceCriteria Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveConvergenceCriteria.html)
[ICWStaticStudyOptions::PAdaptiveErrorLimit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveErrorLimit.html)
[ICWStaticStudyOptions::PAdaptiveMaxPOrder Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveMaxPOrder.html)
[ICWStaticStudyOptions::PAdaptiveStartingPOrder Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStartingPOrder.html)
[ICWStaticStudyOptions::PAdaptiveStrainEnergyErrorLimit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~PAdaptiveStrainEnergyErrorLimit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
