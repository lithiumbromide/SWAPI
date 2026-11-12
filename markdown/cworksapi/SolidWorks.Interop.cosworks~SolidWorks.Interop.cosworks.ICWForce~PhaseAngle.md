---
title: "PhaseAngle Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "PhaseAngle"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~PhaseAngle.html"
---

# PhaseAngle Property (ICWForce)

Gets or sets the phase angle of the force in a harmonic analysis of a linear dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Property PhaseAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Double

instance.PhaseAngle = value

value = instance.PhaseAngle
```

### C#

```csharp
System.double PhaseAngle {get; set;}
```

### C++/CLI

```cpp
property System.double PhaseAngle {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Phase angle of the force; -1 if not set

## VBA Syntax

See [CWForce::PhaseAngle](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~PhaseAngle.html).

## Examples

[Apply Table-driven Load to Multiple Beams (C#)](Apply_Table-driven_Load_to_Multiple_Beams_Example_CSharp.htm)
[Apply Table-driven Load to Multiple Beams (VB.NET)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VBNET.htm)
[Apply Table-driven Load to Multiple Beams (VBA)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VB.htm)

## Remarks

Call [ICWForce::PhaseAngleUnit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWForce~PhaseAngleUnit.html) to get or set the units of phase angle for this force.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
