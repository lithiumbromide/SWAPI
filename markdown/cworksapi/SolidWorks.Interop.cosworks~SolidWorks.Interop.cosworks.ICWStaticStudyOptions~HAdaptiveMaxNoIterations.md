---
title: "HAdaptiveMaxNoIterations Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "HAdaptiveMaxNoIterations"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMaxNoIterations.html"
---

# HAdaptiveMaxNoIterations Property (ICWStaticStudyOptions)

Gets or sets the maximum number of h-adaptive mesh iterations.

## Syntax

### Visual Basic (Declaration)

```vb
Property HAdaptiveMaxNoIterations As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.HAdaptiveMaxNoIterations = value

value = instance.HAdaptiveMaxNoIterations
```

### C#

```csharp
System.int HAdaptiveMaxNoIterations {get; set;}
```

### C++/CLI

```cpp
property System.int HAdaptiveMaxNoIterations {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

2 <= Maximum number of mesh iterations <= 5

## VBA Syntax

See [CWStaticStudyOptions::HAdaptiveMaxNoIterations](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~HAdaptiveMaxNoIterations.html).

## Remarks

This property is valid only if [ICWStaticStudyOptions::AdaptiveMethodType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~AdaptiveMethodType.html) is set to 1.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::HAdaptiveAccuracyBias Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveAccuracyBias.html)
[ICWStaticStudyOptions::HAdaptiveMeshCoarsening Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMeshCoarsening.html)
[ICWStaticStudyOptions::HAdaptiveTargetAccuracy Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveTargetAccuracy.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
