---
title: "MomentOrRotationUnit Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "MomentOrRotationUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MomentOrRotationUnit.html"
---

# MomentOrRotationUnit Property (ICWRemoteLoad)

Sets the units of moment or rotation for this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Property MomentOrRotationUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim value As System.Integer

instance.MomentOrRotationUnit = value

value = instance.MomentOrRotationUnit
```

### C#

```csharp
System.int MomentOrRotationUnit {get; set;}
```

### C++/CLI

```cpp
property System.int MomentOrRotationUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

If remote moment, a value as defined in [swsMomentUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMomentUnit_e.html).

If remote rotation, a value as defined in [swsRotationUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRotationUnit_e.html).

## VBA Syntax

See [CWRemoteLoad::MomentOrRotationUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~MomentOrRotationUnit.html).

## Examples

[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)

## Remarks

This property is valid only if [ICWRemoteLoad::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html) returns false. If it returns true, use [ICWRemoteLoad::MomentUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MomentUnit.html) and [ICWRemoteLoad::RotationUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~RotationUnit.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::GetMomentOrRotationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetMomentOrRotationValues.html)
[ICWRemoteLoad::SetMomentOrRotationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMomentOrRotationValues.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
