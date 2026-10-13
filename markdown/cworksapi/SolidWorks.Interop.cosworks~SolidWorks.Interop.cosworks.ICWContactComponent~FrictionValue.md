---
title: "FrictionValue Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "FrictionValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~FrictionValue.html"
---

# FrictionValue Property (ICWContactComponent)

Gets or sets the friction coefficient for this contact.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrictionValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Double

instance.FrictionValue = value

value = instance.FrictionValue
```

### C#

```csharp
System.double FrictionValue {get; set;}
```

### C++/CLI

```cpp
property System.double FrictionValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 <= Coefficient of friction for contact <= 1.0

## VBA Syntax

See [CWContactComponent::FrictionValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~FrictionValue.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## Remarks

This property is valid only in static and nonlinear studies where [ICWContactComponent::IncludeFriction](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeFriction.html) is set to 1, and [ICWContactComponent::ContactComponentType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ContactComponentType.html) is set to [swsContactType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html).swsContactTypeStaticNoPenetration.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
