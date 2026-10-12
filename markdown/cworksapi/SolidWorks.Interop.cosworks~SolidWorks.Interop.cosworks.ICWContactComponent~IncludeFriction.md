---
title: "IncludeFriction Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "IncludeFriction"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeFriction.html"
---

# IncludeFriction Property (ICWContactComponent)

Obsolete. Superseded by [ICWContactComponent::IncludeFriction2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeFriction2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeFriction As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Integer

instance.IncludeFriction = value

value = instance.IncludeFriction
```

### C#

```csharp
System.int IncludeFriction {get; set;}
```

### C++/CLI

```cpp
property System.int IncludeFriction {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to specify friction, 0 to not

## VBA Syntax

See [CWContactComponent::IncludeFriction](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~IncludeFriction.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## Remarks

This property is valid only in static and nonlinear studies where [ICWContactComponent::ContactComponentType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ContactComponentType.html) is set to [swsContactType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html).swsContactTypeStaticNoPenetration.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)
[ICWContactComponent::FrictionValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~FrictionValue.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
