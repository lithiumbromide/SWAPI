---
title: "HarmonicNoOfPoints Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "HarmonicNoOfPoints"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicNoOfPoints.html"
---

# HarmonicNoOfPoints Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetHarmonicNoOfPoints](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicNoOfPoints2.html) and [ICWDynamicStudyOptions::SetHarmonicNoOfPoints.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicNoOfPoints2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property HarmonicNoOfPoints As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.HarmonicNoOfPoints = value

value = instance.HarmonicNoOfPoints
```

### C#

```csharp
System.int HarmonicNoOfPoints {get; set;}
```

### C++/CLI

```cpp
property System.int HarmonicNoOfPoints {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of points for each frequency

## VBA Syntax

See [CWDynamicStudyOptions::HarmonicNoOfPoints](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~HarmonicNoOfPoints.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::HarmonicBandwidth Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicBandwidth.html)
[ICWDynamicStudyOptions::HarmonicFrequencyLowerLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyLowerLimit.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUnits.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::HarmonicInterpolation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicInterpolation.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
