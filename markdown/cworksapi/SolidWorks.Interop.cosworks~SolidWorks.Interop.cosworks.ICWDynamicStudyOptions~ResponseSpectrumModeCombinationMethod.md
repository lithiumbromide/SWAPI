---
title: "ResponseSpectrumModeCombinationMethod Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "ResponseSpectrumModeCombinationMethod"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumModeCombinationMethod.html"
---

# ResponseSpectrumModeCombinationMethod Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetResponseSpectrumModeCombinationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumModeCombinationMethod2.html) and [ICWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseSpectrumModeCombinationMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.ResponseSpectrumModeCombinationMethod = value

value = instance.ResponseSpectrumModeCombinationMethod
```

### C#

```csharp
System.int ResponseSpectrumModeCombinationMethod {get; set;}
```

### C++/CLI

```cpp
property System.int ResponseSpectrumModeCombinationMethod {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Mode combination method as defined in [swsModeCombinationMethod_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsModeCombinationMethod_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::ResponseSpectrumModeCombinationMethod](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~ResponseSpectrumModeCombinationMethod.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::ResponseSpectrumClusterFactor Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumClusterFactor.html)
[ICWDynamicStudyOptions::ResponseSpectrumCurveInterpolation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumCurveInterpolation.html)
[ICWDynamicStudyOptions::ResponseSpectrumUseMaterialDamping Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumUseMaterialDamping.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
