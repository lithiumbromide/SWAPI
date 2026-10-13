---
title: "Frames Property (ISimulation)"
project: "SOLIDWORKS API Help"
interface: "ISimulation"
member: "Frames"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~Frames.html"
---

# Frames Property (ISimulation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Frames As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation
Dim value As System.Integer

value = instance.Frames
```

### C#

```csharp
System.int Frames {get;}
```

### C++/CLI

```cpp
property System.int Frames {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of steps

## VBA Syntax

See [Simulation::Frames](ms-its:sldworksapivb6.chm::/sldworks~Simulation~Frames.html).

## Remarks

If the Physical Simulation is not yet calculated, then the return value is 0.0.

## See Also

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.html)
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
