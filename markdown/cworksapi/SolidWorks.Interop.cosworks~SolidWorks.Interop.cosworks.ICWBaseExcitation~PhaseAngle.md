---
title: "PhaseAngle Property (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "PhaseAngle"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~PhaseAngle.html"
---

# PhaseAngle Property (ICWBaseExcitation)

Gets or sets the phase angle of this base excitation.

## Syntax

### Visual Basic (Declaration)

```vb
Property PhaseAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
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

Phase angle; -1 if not set

## VBA Syntax

See [CWBaseExcitation::PhaseAngle](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~PhaseAngle.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)
[ICWBaseExcitation::PhaseAngleUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~PhaseAngleUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
