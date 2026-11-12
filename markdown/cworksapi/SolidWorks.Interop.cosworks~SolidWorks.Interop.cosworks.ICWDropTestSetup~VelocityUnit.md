---
title: "VelocityUnit Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "VelocityUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~VelocityUnit.html"
---

# VelocityUnit Property (ICWDropTestSetup)

Gets or sets the units of velocity.

## Syntax

### Visual Basic (Declaration)

```vb
Property VelocityUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Integer

instance.VelocityUnit = value

value = instance.VelocityUnit
```

### C#

```csharp
System.int VelocityUnit {get; set;}
```

### C++/CLI

```cpp
property System.int VelocityUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined in [swsVelocityUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsVelocityUnit_e.html)

## VBA Syntax

See [CWDropTestSetup::VelocityUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~VelocityUnit.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

This method is valid only if [ICWDropTestSetup::DropType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropType.html) = swsDropType_e.swsDropType_VelocityAtImpact.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForVelocityDirection Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForVelocityDirection.html)
[ICWDropTestSetup::FlipVelocityDirection Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipVelocityDirection.html)
[ICWDropTestSetup::Velocity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~Velocity.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
