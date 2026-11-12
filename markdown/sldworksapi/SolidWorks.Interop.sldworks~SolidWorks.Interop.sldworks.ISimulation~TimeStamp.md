---
title: "TimeStamp Property (ISimulation)"
project: "SOLIDWORKS API Help"
interface: "ISimulation"
member: "TimeStamp"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~TimeStamp.html"
---

# TimeStamp Property (ISimulation)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TimeStamp As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation
Dim value As System.Integer

value = instance.TimeStamp
```

### C#

```csharp
System.int TimeStamp {get;}
```

### C++/CLI

```cpp
property System.int TimeStamp {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Time stamp for this Physical Simulation (see **Remarks**)

## VBA Syntax

See [Simulation::Timestamp](ms-its:sldworksapivb6.chm::/sldworks~Simulation~Timestamp.html).

## Remarks

| If a... | Then... |
| --- | --- |
| New Physical Simulation is calculated | The time stamp (return value) changes |
| Physical Simulation does not exist or it was deleted | 0 is returned |
| Physical Simulation was created using SOLIDWORKS 2005 or earlier | -1 is returned |

## See Also

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.html)
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
