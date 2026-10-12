---
title: "Unit Property (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "Unit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~Unit.html"
---

# Unit Property (ICWBaseExcitation)

Gets or sets the units for this base excitation.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim value As System.Integer

instance.Unit = value

value = instance.Unit
```

### C#

```csharp
System.int Unit {get; set;}
```

### C++/CLI

```cpp
property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

| Value as defined in... | If ICWBaseExcitation::BaseExcitationType is... |
| --- | --- |
| swsLinearUnit_e | swsBaseExcitationType_e.swsBaseExcitationType_Displacement |
| swsVelocityUnit_e | swsBaseExcitationType_e.swsBaseExcitationType_Velocity |
| swsAccelerationUnit_e | swsBaseExcitationType_e.swsBaseExcitationType_Acceleration |

## VBA Syntax

See [CWBaseExcitation::Unit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~Unit.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
