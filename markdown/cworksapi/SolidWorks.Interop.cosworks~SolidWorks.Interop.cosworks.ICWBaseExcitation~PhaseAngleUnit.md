---
title: "PhaseAngleUnit Property (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "PhaseAngleUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~PhaseAngleUnit.html"
---

# PhaseAngleUnit Property (ICWBaseExcitation)

Gets or sets the units of phase angle for this base excitation.

## Syntax

### Visual Basic (Declaration)

```vb
Property PhaseAngleUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
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

Value as defined in [swsPhaseAngleUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPhaseAngleUnit_e.html); -1 if undefined

## VBA Syntax

See [CWBaseExcitation::PhaseAngleUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~PhaseAngleUnit.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)
[ICWBaseExcitation::PhaseAngle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~PhaseAngle.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
