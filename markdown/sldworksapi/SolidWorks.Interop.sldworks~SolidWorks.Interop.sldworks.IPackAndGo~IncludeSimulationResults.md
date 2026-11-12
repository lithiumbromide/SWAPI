---
title: "IncludeSimulationResults Property (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "IncludeSimulationResults"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeSimulationResults.html"
---

# IncludeSimulationResults Property (IPackAndGo)

Gets or sets whether to add the model's SOLIDWORKS Simulation results to Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeSimulationResults As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim value As System.Boolean

instance.IncludeSimulationResults = value

value = instance.IncludeSimulationResults
```

### C#

```csharp
System.bool IncludeSimulationResults {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeSimulationResults {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the model's SOLIDWORKS Simulation results are added to Pack and Go, false if not

## VBA Syntax

See [PackAndGo::IncludeSimulationResults](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~IncludeSimulationResults.html).

## Examples

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
