---
title: "DistributionType Property (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "DistributionType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~DistributionType.html"
---

# DistributionType Property (ICWBearingLoad)

Gets or sets the distribution type of this bearing load.

## Syntax

### Visual Basic (Declaration)

```vb
Property DistributionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
Dim value As System.Integer

instance.DistributionType = value

value = instance.DistributionType
```

### C#

```csharp
System.int DistributionType {get; set;}
```

### C++/CLI

```cpp
property System.int DistributionType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Bearing load distribution as defined in [swsBearingLoadDistributionType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingLoadDistributionType_e.html)

## VBA Syntax

See [CWBearingLoad::DistributionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~DistributionType.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
