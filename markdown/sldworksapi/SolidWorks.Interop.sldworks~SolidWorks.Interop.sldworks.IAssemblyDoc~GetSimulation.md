---
title: "GetSimulation Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetSimulation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetSimulation.html"
---

# GetSimulation Method (IAssemblyDoc)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSimulation() As Simulation
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As Simulation

value = instance.GetSimulation()
```

### C#

```csharp
Simulation GetSimulation()
```

### C++/CLI

```cpp
Simulation^ GetSimulation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ISimulation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation.html)

## VBA Syntax

See [AssemblyDoc::GetSimulation](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetSimulation.html).

## Remarks

The Simulation folder is returned even if the folder does not yet exist or does not currently appear in the FeatureManager design tree.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
