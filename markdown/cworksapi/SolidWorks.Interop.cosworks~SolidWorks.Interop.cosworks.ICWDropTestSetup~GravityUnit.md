---
title: "GravityUnit Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "GravityUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~GravityUnit.html"
---

# GravityUnit Property (ICWDropTestSetup)

Gets or sets the units of gravity.

## Syntax

### Visual Basic (Declaration)

```vb
Property GravityUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Integer

instance.GravityUnit = value

value = instance.GravityUnit
```

### C#

```csharp
System.int GravityUnit {get; set;}
```

### C++/CLI

```cpp
property System.int GravityUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined in [swsAccelerationUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAccelerationUnit_e.html)

## VBA Syntax

See [CWDropTestSetup::GravityUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~GravityUnit.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForGravityDirection Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForGravityDirection.html)
[ICWDropTestSetup::FlipGravityDirection Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipGravityDirection.html)
[ICWDropTestSetup::Gravity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~Gravity.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
