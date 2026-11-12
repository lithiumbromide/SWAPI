---
title: "IncludeFriction Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "IncludeFriction"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~IncludeFriction.html"
---

# IncludeFriction Property (ICWContactSet)

Obsolete. Superseded by [ICWContactSet::IncludeFriction2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~IncludeFriction2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeFriction As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
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

1 to include friction, 0 to not

## VBA Syntax

See [CWContactSet::IncludeFriction](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~IncludeFriction.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is one of:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearNoPrenetration
- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearShrinkFit

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::FrictionValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~FrictionValue.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
