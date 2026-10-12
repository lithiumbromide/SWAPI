---
title: "Status Property (ISimulation)"
project: "SOLIDWORKS API Help"
interface: "ISimulation"
member: "Status"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~Status.html"
---

# Status Property (ISimulation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Status As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation
Dim value As System.Boolean

value = instance.Status
```

### C#

```csharp
System.bool Status {get;}
```

### C++/CLI

```cpp
property System.bool Status {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the Physical Simulation has been calculated, false if it has not or if the calculation was unsuccessful

## VBA Syntax

See [Simulation::Status](ms-its:sldworksapivb6.chm::/sldworks~Simulation~Status.html).

## See Also

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.html)
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
