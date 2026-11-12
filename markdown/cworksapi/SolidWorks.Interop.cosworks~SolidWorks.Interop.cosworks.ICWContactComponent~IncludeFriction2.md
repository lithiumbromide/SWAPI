---
title: "IncludeFriction2 Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "IncludeFriction2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~IncludeFriction2.html"
---

# IncludeFriction2 Property (ICWContactComponent)

Sets whether to specify a friction coefficient for this contact.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeFriction2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim value As System.Boolean

instance.IncludeFriction2 = value

value = instance.IncludeFriction2
```

### C#

```csharp
System.bool IncludeFriction2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeFriction2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to include friction, 0 or false to not

## VBA Syntax

See [CWContactComponent::IncludeFriction2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~IncludeFriction2.html).

## Remarks

This property is valid only in static and nonlinear studies where [ICWContactComponent::ContactComponentType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ContactComponentType.html) is set to [swsContactType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html).swsContactTypeStaticNoPenetration.

To set this property, you can specify either the boolean or the integer.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
