---
title: "MomentUnit Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "MomentUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MomentUnit.html"
---

# MomentUnit Property (ICWRemoteLoad)

Sets the units of moment for this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property MomentUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad

instance.MomentUnit = value
```

### C#

```csharp
System.int MomentUnit {set;}
```

### C++/CLI

```cpp
property System.int MomentUnit {
   void set (    System.int value);
}
```

### Property Value

Units of moment as defined in [swsMomentUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMomentUnit_e.html)

## VBA Syntax

See [CWRemoteLoad::MomentUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~MomentUnit.html).

## Remarks

This property is valid only if [ICWRemoteLoad::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html) returns true. If it returns false, use [ICWRemoteLoad::MomentOrRotationUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MomentOrRotationUnit.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::SetMomentOrRotationValuesEx Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMomentOrRotationValuesEx.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
