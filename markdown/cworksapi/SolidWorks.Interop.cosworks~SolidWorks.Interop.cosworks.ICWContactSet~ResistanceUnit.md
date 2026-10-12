---
title: "ResistanceUnit Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "ResistanceUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ResistanceUnit.html"
---

# ResistanceUnit Property (ICWContactSet)

Gets or sets the unit system for this thermal resistance contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResistanceUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

instance.ResistanceUnit = value

value = instance.ResistanceUnit
```

### C#

```csharp
System.int ResistanceUnit {get; set;}
```

### C++/CLI

```cpp
property System.int ResistanceUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Unit system as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)

## VBA Syntax

See [CWContactSet::ResistanceUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~ResistanceUnit.html).

## Remarks

This property is valid only for thermal studies and when [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is set to [swsContactSetTypeThermal_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeThermal_e.html).swsContactSetTypeThermalResistance.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::ResistanceType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ResistanceType.html)
[ICWContactSet::ResistanceValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ResistanceValue.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
