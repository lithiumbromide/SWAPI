---
title: "ResistanceValue Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "ResistanceValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ResistanceValue.html"
---

# ResistanceValue Property (ICWContactSet)

Gets or sets the thermal resistance value for this thermal resistance contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResistanceValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Double

instance.ResistanceValue = value

value = instance.ResistanceValue
```

### C#

```csharp
System.double ResistanceValue {get; set;}
```

### C++/CLI

```cpp
property System.double ResistanceValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Thermal resistance value

## VBA Syntax

See [CWContactSet::ResistanceValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~ResistanceValue.html).

## Remarks

This property is valid only for thermal studies and when [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is set to [swsContactSetTypeThermal_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeThermal_e.html).swsContactSetTypeThermalResistance.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::ResistanceType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ResistanceType.html)
[ICWContactSet::ResistanceUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ResistanceUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
