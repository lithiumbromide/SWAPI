---
title: "ResistanceType Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "ResistanceType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ResistanceType.html"
---

# ResistanceType Property (ICWContactSet)

Gets or sets the thermal resistance type for this thermal resistance contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResistanceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

instance.ResistanceType = value

value = instance.ResistanceType
```

### C#

```csharp
System.int ResistanceType {get; set;}
```

### C++/CLI

```cpp
property System.int ResistanceType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Thermal resistance type as defined in [swsResistanceType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResistanceType_e.html)

## VBA Syntax

See [CWContactSet::ResistanceType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~ResistanceType.html).

## Remarks

This property is valid only for thermal studies and when [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is set to [swsContactSetTypeThermal_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeThermal_e.html).swsContactSetTypeThermalResistance.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::ResistanceUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ResistanceUnit.html)
[ICWContactSet::ResistanceValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ResistanceValue.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
