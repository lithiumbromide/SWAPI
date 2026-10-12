---
title: "ResponseSpectrumClusterFactor Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "ResponseSpectrumClusterFactor"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumClusterFactor.html"
---

# ResponseSpectrumClusterFactor Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetResponseSpectrumClusterFactor2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumClusterFactor2.html) and [ICWDynamicStudyOptions::SetResponseSpectrumClusterFactor2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumClusterFactor2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseSpectrumClusterFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Double

instance.ResponseSpectrumClusterFactor = value

value = instance.ResponseSpectrumClusterFactor
```

### C#

```csharp
System.double ResponseSpectrumClusterFactor {get; set;}
```

### C++/CLI

```cpp
property System.double ResponseSpectrumClusterFactor {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Cluster factor (see **Remarks**)

## VBA Syntax

See [CWDynamicStudyOptions::ResponseSpectrumClusterFactor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~ResponseSpectrumClusterFactor.html).

## Remarks

This property is valid only if [ICWDynamicStudyOptions::ResponseSpectrumModeCombinationMethod](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumModeCombinationMethod.html) = 1 (Absolute Sum).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::ResponseSpectrumCurveInterpolation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumCurveInterpolation.html)
[ICWDynamicStudyOptions::ResponseSpectrumUseMaterialDamping Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumUseMaterialDamping.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
