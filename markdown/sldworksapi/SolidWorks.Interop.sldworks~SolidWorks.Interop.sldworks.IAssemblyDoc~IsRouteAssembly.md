---
title: "IsRouteAssembly Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IsRouteAssembly"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsRouteAssembly.html"
---

# IsRouteAssembly Method (IAssemblyDoc)

Gets whether the assembly document is a routing assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsRouteAssembly() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.IsRouteAssembly()
```

### C#

```csharp
System.bool IsRouteAssembly()
```

### C++/CLI

```cpp
System.bool IsRouteAssembly();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the assembly document is a routing assembly, false if not

## VBA Syntax

See [AssemblyDoc::IsRouteAssembly](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IsRouteAssembly.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetRouteManager Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetRouteManager.html)
[IModelDoc2::InsertRoutePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRoutePoint.html)
[IModelDoc2::EditRoute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRoute.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
