---
title: "IsSubAssemblyRigid Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "IsSubAssemblyRigid"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IsSubAssemblyRigid.html"
---

# IsSubAssemblyRigid Method (IExplodeStep)

Gets whether the subassembly is rigid or flexible.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSubAssemblyRigid() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Boolean

value = instance.IsSubAssemblyRigid()
```

### C#

```csharp
System.bool IsSubAssemblyRigid()
```

### C++/CLI

```cpp
System.bool IsSubAssemblyRigid();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the subassembly is rigid, false if it is flexible

## VBA Syntax

See [ExplodeStep::IsSubAssemblyRigid](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~IsSubAssemblyRigid.html).

## Remarks

See the SOLIDWORKS Help for more information about flexible and rigid subassemblies.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IComponent2::Solving Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Solving.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
