---
title: "ClearanceUnit Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "ClearanceUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ClearanceUnit.html"
---

# ClearanceUnit Property (ICWContactSet)

Gets or sets the units of clearance for this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClearanceUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

instance.ClearanceUnit = value

value = instance.ClearanceUnit
```

### C#

```csharp
System.int ClearanceUnit {get; set;}
```

### C++/CLI

```cpp
property System.int ClearanceUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units of clearance as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWContactSet::ClearanceUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~ClearanceUnit.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is one of:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall
- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearNoPenetration

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::ClearanceValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ClearanceValue.html)
[ICWContactSet::GapType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GapType.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
