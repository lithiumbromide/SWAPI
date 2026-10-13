---
title: "GapType Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "GapType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GapType.html"
---

# GapType Property (ICWContactSet)

Gets or sets the gap type associated with this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property GapType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

instance.GapType = value

value = instance.GapType
```

### C#

```csharp
System.int GapType {get; set;}
```

### C++/CLI

```cpp
property System.int GapType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of gap as defined in [swsGapType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsGapType_e.html)SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~ClearanceValue.html

## VBA Syntax

See [CWContactSet::GapType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~GapType.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is one of:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall
- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearNoPenetration

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::ClearanceUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ClearanceUnit.html)
[ICWContactSet::ClearanceValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ClearanceValue.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
