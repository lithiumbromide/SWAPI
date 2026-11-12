---
title: "ResetEdgeTolerances Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ResetEdgeTolerances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetEdgeTolerances.html"
---

# ResetEdgeTolerances Method (IBody2)

Resets the tolerance on all edges of this body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ResetEdgeTolerances()
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2

instance.ResetEdgeTolerances()
```

### C#

```csharp
void ResetEdgeTolerances()
```

### C++/CLI

```cpp
void ResetEdgeTolerances();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Body2::ResetEdgeTolerances](ms-its:sldworksapivb6.chm::/sldworks~Body2~ResetEdgeTolerances.html).

## Remarks

Use this method if [IBody2::Operations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Operations2.html) or [IBody2::IOperations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IOperations2.html) returns a non-manifold error. Then use IBody2::Operations2 or IBody2::IOperations2 again after using this method.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
