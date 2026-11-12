---
title: "FrictionValue Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "FrictionValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~FrictionValue.html"
---

# FrictionValue Property (ICWContactSet)

Gets or sets the friction coefficient for this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrictionValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
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

0.0 <= Coefficient of friction <= 1.0

## VBA Syntax

See [CWContactSet::FrictionValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~FrictionValue.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is one of:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearNoPrenetration
- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearShrinkFit

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::IncludeFriction Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~IncludeFriction.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
