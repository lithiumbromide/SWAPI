---
title: "PhaseAngle Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "PhaseAngle"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~PhaseAngle.html"
---

# PhaseAngle Property (ICWPressure)

Gets or sets the phase angle of the pressure in a linear dynamic harmonic study.

## Syntax

### Visual Basic (Declaration)

```vb
Property PhaseAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
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

Phase angle of the pressure; -1 if not set

## VBA Syntax

See [CWPressure::PhaseAngle](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~PhaseAngle.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## Remarks

Call [ICWPressure::PhaseAngleUnit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPressure~PhaseAngleUnit.html) to get or set the unit for measuring the phase angle of the pressure.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
