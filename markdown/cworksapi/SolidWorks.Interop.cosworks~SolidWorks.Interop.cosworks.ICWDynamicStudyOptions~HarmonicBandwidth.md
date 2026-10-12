---
title: "HarmonicBandwidth Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "HarmonicBandwidth"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicBandwidth.html"
---

# HarmonicBandwidth Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetHarmonicBandwidth2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetHarmonicBandwidth2.html) and [ICWDynamicStudyOptions::SetHarmonicBandwidth2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetHarmonicBandwidth2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property HarmonicBandwidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Double

instance.HarmonicBandwidth = value

value = instance.HarmonicBandwidth
```

### C#

```csharp
System.double HarmonicBandwidth {get; set;}
```

### C++/CLI

```cpp
property System.double HarmonicBandwidth {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Bandwidth of each frequency

## VBA Syntax

See [CWDynamicStudyOptions::HarmonicBandwidth](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~HarmonicBandwidth.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::HarmonicFrequencyLowerLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyLowerLimit.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUnits Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUnits.html)
[ICWDynamicStudyOptions::HarmonicFrequencyUpperLimit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicFrequencyUpperLimit.html)
[ICWDynamicStudyOptions::HarmonicInterpolation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicInterpolation.html)
[ICWDynamicStudyOptions::HarmonicNoOfPoints Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~HarmonicNoOfPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
