---
title: "TotalMass Property (ICWDistributedMass)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDistributedMass"
member: "TotalMass"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass~TotalMass.html"
---

# TotalMass Property (ICWDistributedMass)

Gets or sets the total distributed mass.

## Syntax

### Visual Basic (Declaration)

```vb
Property TotalMass As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDistributedMass
Dim value As System.Double

instance.TotalMass = value

value = instance.TotalMass
```

### C#

```csharp
System.double TotalMass {get; set;}
```

### C++/CLI

```cpp
property System.double TotalMass {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Weight

## VBA Syntax

See [CWDistributedMass::TotalMass](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDistributedMass~TotalMass.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## See Also

[ICWDistributedMass Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass.html)
[ICWDistributedMass Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDistributedMass_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
