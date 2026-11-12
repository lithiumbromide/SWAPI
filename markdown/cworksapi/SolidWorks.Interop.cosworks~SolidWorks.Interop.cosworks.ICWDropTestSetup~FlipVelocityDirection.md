---
title: "FlipVelocityDirection Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "FlipVelocityDirection"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipVelocityDirection.html"
---

# FlipVelocityDirection Property (ICWDropTestSetup)

Obsolete. Superseded by [ICWDropTestSetup::FlipVelocityDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipVelocityDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipVelocityDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Integer

instance.FlipVelocityDirection = value

value = instance.FlipVelocityDirection
```

### C#

```csharp
System.int FlipVelocityDirection {get; set;}
```

### C++/CLI

```cpp
property System.int FlipVelocityDirection {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse the direction, 0 to not

## VBA Syntax

See [CWDropTestSetup::FlipVelocityDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~FlipVelocityDirection.html).

## Remarks

This method is valid only if [ICWDropTestSetup::DropType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropType.html) = swsDropType_e.swsDropType_VelocityAtImpact.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForVelocityDirection Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForVelocityDirection.html)
[ICWDropTestSetup::Velocity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~Velocity.html)
[ICWDropTestSetup::VelocityUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~VelocityUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
