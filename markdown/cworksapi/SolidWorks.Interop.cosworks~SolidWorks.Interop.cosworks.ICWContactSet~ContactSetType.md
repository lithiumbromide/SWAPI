---
title: "ContactSetType Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "ContactSetType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html"
---

# ContactSetType Property (ICWContactSet)

Gets or sets the type of this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property ContactSetType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

instance.ContactSetType = value

value = instance.ContactSetType
```

### C#

```csharp
System.int ContactSetType {get; set;}
```

### C++/CLI

```cpp
property System.int ContactSetType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of contact set for:

- [static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies as defined in [swsContactSetTypeStaticNonLinear_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html)
- [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies as defined in [swsContactSetTypeThermal_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeThermal_e.html)
- [buckling](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html) and [frequency](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html) studies as defined [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html), excluding swsContactTypeStaticNoPenetration

## VBA Syntax

See [CWContactSet::ContactSetType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~ContactSetType.html).

## Remarks

See the SOLIDWORKS Simulation Help for guidelines about studies with contact conditions.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
