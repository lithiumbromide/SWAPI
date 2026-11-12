---
title: "Units Property (ICWDistributedMass)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDistributedMass"
member: "Units"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass~Units.html"
---

# Units Property (ICWDistributedMass)

Gets or sets the units of the distributed mass.

## Syntax

### Visual Basic (Declaration)

```vb
Property Units As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDistributedMass
Dim value As System.Integer

instance.Units = value

value = instance.Units
```

### C#

```csharp
System.int Units {get; set;}
```

### C++/CLI

```cpp
property System.int Units {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined by [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)

## VBA Syntax

See [CWDistributedMass::Units](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDistributedMass~Units.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWDistributedMass Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass.html)
[ICWDistributedMass Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
