---
title: "ResetComponents Method (ISimulation)"
project: "SOLIDWORKS API Help"
interface: "ISimulation"
member: "ResetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~ResetComponents.html"
---

# ResetComponents Method (ISimulation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function ResetComponents() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation
Dim value As System.Boolean

value = instance.ResetComponents()
```

### C#

```csharp
System.bool ResetComponents()
```

### C++/CLI

```cpp
System.bool ResetComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the components' positions and orientations are reset, false if not

## VBA Syntax

See [Simulation::ResetComponents](ms-its:sldworksapivb6.chm::/sldworks~Simulation~ResetComponents.html).

## See Also

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.html)
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
