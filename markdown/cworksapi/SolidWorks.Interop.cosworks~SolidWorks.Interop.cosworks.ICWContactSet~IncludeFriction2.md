---
title: "IncludeFriction2 Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "IncludeFriction2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~IncludeFriction2.html"
---

# IncludeFriction2 Property (ICWContactSet)

Sets whether to include friction in this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeFriction2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
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

See [CWContactSet::IncludeFriction2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~IncludeFriction2.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is one of:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearNoPrenetration
- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearShrinkFit

To set this property, you can specify either the boolean or the integer.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
