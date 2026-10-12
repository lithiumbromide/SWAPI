---
title: "IReorganizeComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IReorganizeComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IReorganizeComponents.html"
---

# IReorganizeComponents Method (IAssemblyDoc)

Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function IReorganizeComponents( _
   ByVal Count As System.Integer, _
   ByRef Source As Component2, _
   ByVal Target As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Source As Component2
Dim Target As System.Object
Dim value As System.Boolean

value = instance.IReorganizeComponents(Count, Source, Target)
```

### C#

```csharp
System.bool IReorganizeComponents(
   System.int Count,
   ref Component2 Source,
   System.object Target
)
```

### C++/CLI

```cpp
System.bool IReorganizeComponents(
   System.int Count,
   Component2^% Source,
   System.Object^ Target
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of components to reorganize
- `Source`: Array of selected components to more; all of the components must be at the same level in one parent assembly
- `Target`: Where to move the components, which can be a top-level assembly or sub-assembly anywhere at any level of the hierarchy

### Return Value

True if the selected components were moved to the selected assembly or sub-assembly, false if not

## VBA Syntax

See [AssemblyDoc::IReorganizeComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IReorganizeComponents.html).

## Remarks

See the SOLIDWORKS Help for more information about reorganizing components.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ReorganizeComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorganizeComponents.html)
[IAssemblyDoc::ReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.html)
[DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
