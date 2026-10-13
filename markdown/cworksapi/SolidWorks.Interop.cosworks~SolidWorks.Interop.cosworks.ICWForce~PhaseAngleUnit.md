---
title: "PhaseAngleUnit Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "PhaseAngleUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~PhaseAngleUnit.html"
---

# PhaseAngleUnit Property (ICWForce)

Gets or sets the units of phase angle of the force in a harmonic analysis of a linear dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Property PhaseAngleUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Integer

instance.PhaseAngleUnit = value

value = instance.PhaseAngleUnit
```

### C#

```csharp
System.int PhaseAngleUnit {get; set;}
```

### C++/CLI

```cpp
property System.int PhaseAngleUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units of phase angle of the force as defined in [swsPhaseAngleUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPhaseAngleUnit_e.html); -1 if undefined

## VBA Syntax

See [CWForce::PhaseAngleUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~PhaseAngleUnit.html).

## Examples

[Apply Table-driven Load to Multiple Beams (C#)](Apply_Table-driven_Load_to_Multiple_Beams_Example_CSharp.htm)
[Apply Table-driven Load to Multiple Beams (VB.NET)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VBNET.htm)
[Apply Table-driven Load to Multiple Beams (VBA)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VB.htm)

## Remarks

Call [ICWForce::PhaseAngle](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWForce~PhaseAngle.html) to get or set the phase angle of the force.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
