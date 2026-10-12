---
title: "ClearanceValue Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "ClearanceValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ClearanceValue.html"
---

# ClearanceValue Property (ICWContactSet)

Gets or sets the clearance (gap) value for this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClearanceValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Double

instance.ClearanceValue = value

value = instance.ClearanceValue
```

### C#

```csharp
System.double ClearanceValue {get; set;}
```

### C++/CLI

```cpp
property System.double ClearanceValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Clearance value

## VBA Syntax

See [CWContactSet::ClearanceValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~ClearanceValue.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is one of:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall
- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearNoPenetration

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::ClearanceUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ClearanceUnit.html)
[ICWContactSet::GapType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GapType.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
