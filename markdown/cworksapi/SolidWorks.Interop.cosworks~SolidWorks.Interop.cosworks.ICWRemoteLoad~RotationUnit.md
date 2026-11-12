---
title: "RotationUnit Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "RotationUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~RotationUnit.html"
---

# RotationUnit Property (ICWRemoteLoad)

Sets the units of rotation for this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property RotationUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad

instance.RotationUnit = value
```

### C#

```csharp
System.int RotationUnit {set;}
```

### C++/CLI

```cpp
property System.int RotationUnit {
   void set (    System.int value);
}
```

### Property Value

Units of rotation as defined by [swsRotationUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRotationUnit_e.html)

## VBA Syntax

See [CWRemoteLoad::RotationUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~RotationUnit.html).

## Remarks

This property is valid only if [ICWRemoteLoad::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html) returns true. If it returns false, use [ICWRemoteLoad::MomentOrRotationUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MomentOrRotationUnit.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::SetMomentOrRotationValuesEx Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMomentOrRotationValuesEx.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
