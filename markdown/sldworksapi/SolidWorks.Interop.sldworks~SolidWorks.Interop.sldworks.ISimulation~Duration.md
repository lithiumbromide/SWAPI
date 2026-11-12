---
title: "Duration Property (ISimulation)"
project: "SOLIDWORKS API Help"
interface: "ISimulation"
member: "Duration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~Duration.html"
---

# Duration Property (ISimulation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Duration As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation
Dim value As System.Double

value = instance.Duration
```

### C#

```csharp
System.double Duration {get;}
```

### C++/CLI

```cpp
property System.double Duration {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Elapsed time in seconds

## VBA Syntax

See [Simulation::Duration](ms-its:sldworksapivb6.chm::/sldworks~Simulation~Duration.html).

## Remarks

If the Physical Simulation has not yet been calculated, then the return value is 0.0.

The return value represents the length of time that the simulation is expected to last. This means that if a bouncing ball takes 15 seconds to come to a stop, then this property returns a value of 15.

## See Also

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.html)
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
