---
title: "HAdaptiveMeshCoarsening Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "HAdaptiveMeshCoarsening"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMeshCoarsening.html"
---

# HAdaptiveMeshCoarsening Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::HAdaptiveMeshCoarsening2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMeshCoarsening2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property HAdaptiveMeshCoarsening As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.HAdaptiveMeshCoarsening = value

value = instance.HAdaptiveMeshCoarsening
```

### C#

```csharp
System.int HAdaptiveMeshCoarsening {get; set;}
```

### C++/CLI

```cpp
property System.int HAdaptiveMeshCoarsening {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to allow mesh coarsening in areas that do not need a highly defined mesh, 0 to not

## VBA Syntax

See [CWStaticStudyOptions::HAdaptiveMeshCoarsening](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~HAdaptiveMeshCoarsening.html).

## Remarks

This property is valid only if [ICWStaticStudyOptions::AdaptiveMethodType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~AdaptiveMethodType.html) is set to 1.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::HAdaptiveAccuracyBias Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveAccuracyBias.html)
[ICWStaticStudyOptions::HAdaptiveMaxNoIterations Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveMaxNoIterations.html)
[ICWStaticStudyOptions::HAdaptiveTargetAccuracy Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~HAdaptiveTargetAccuracy.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
