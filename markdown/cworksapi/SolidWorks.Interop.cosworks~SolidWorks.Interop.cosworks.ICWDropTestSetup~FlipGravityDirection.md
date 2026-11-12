---
title: "FlipGravityDirection Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "FlipGravityDirection"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipGravityDirection.html"
---

# FlipGravityDirection Property (ICWDropTestSetup)

Obsolete. Superseded by [ICWDropTestSetup::FlipGravityDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipGravityDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipGravityDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Integer

instance.FlipGravityDirection = value

value = instance.FlipGravityDirection
```

### C#

```csharp
System.int FlipGravityDirection {get; set;}
```

### C++/CLI

```cpp
property System.int FlipGravityDirection {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse the direction, 0 to not

## VBA Syntax

See [CWDropTestSetup::FlipGravityDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~FlipGravityDirection.html).

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForGravityDirection Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForGravityDirection.html)
[ICWDropTestSetup::Gravity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~Gravity.html)
[ICWDropTestSetup::GravityUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~GravityUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
