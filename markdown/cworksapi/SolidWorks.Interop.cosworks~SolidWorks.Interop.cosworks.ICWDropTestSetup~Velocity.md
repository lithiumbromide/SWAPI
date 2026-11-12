---
title: "Velocity Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "Velocity"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~Velocity.html"
---

# Velocity Property (ICWDropTestSetup)

Gets or sets the magnitude of velocity at impact.

## Syntax

### Visual Basic (Declaration)

```vb
Property Velocity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Double

instance.Velocity = value

value = instance.Velocity
```

### C#

```csharp
System.double Velocity {get; set;}
```

### C++/CLI

```cpp
property System.double Velocity {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Magnitude of velocity at impact

## VBA Syntax

See [CWDropTestSetup::Velocity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~Velocity.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

This method is valid only if [ICWDropTestSetup::DropType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropType.html) = swsDropType_e.swsDropType_VelocityAtImpact.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForVelocityDirection Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForVelocityDirection.html)
[ICWDropTestSetup::FlipVelocityDirection Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipVelocityDirection.html)
[ICWDropTestSetup::VelocityUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~VelocityUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
