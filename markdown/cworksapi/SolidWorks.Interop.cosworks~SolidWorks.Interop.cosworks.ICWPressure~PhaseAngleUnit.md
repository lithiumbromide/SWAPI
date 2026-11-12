---
title: "PhaseAngleUnit Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "PhaseAngleUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~PhaseAngleUnit.html"
---

# PhaseAngleUnit Property (ICWPressure)

Gets or sets the units of phase angle of the pressure in a linear dynamic harmonic study.

## Syntax

### Visual Basic (Declaration)

```vb
Property PhaseAngleUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
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

Units of phase angle as defined in [swsPhaseAngleUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPhaseAngleUnit_e.html); -1 if undefined

## VBA Syntax

See [CWPressure::PhaseAngleUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~PhaseAngleUnit.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## Remarks

Call [ICWPressure::PhaseAngle](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPressure~PhaseAngle.html) to get or set the phase angle of the pressure.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
