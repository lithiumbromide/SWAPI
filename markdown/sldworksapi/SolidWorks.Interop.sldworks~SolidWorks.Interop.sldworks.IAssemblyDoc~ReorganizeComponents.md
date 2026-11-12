---
title: "ReorganizeComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ReorganizeComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorganizeComponents.html"
---

# ReorganizeComponents Method (IAssemblyDoc)

Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReorganizeComponents( _
   ByVal Source As System.Object, _
   ByVal Target As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Source As System.Object
Dim Target As System.Object
Dim value As System.Boolean

value = instance.ReorganizeComponents(Source, Target)
```

### C#

```csharp
System.bool ReorganizeComponents(
   System.object Source,
   System.object Target
)
```

### C++/CLI

```cpp
System.bool ReorganizeComponents(
   System.Object^ Source,
   System.Object^ Target
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Source`: Array of selected [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) to more; all of the components must be at the same level in one parent assembly
- `Target`: Where to move the components, which can be a top-level assembly or sub-assembly anywhere at any level of the hierarchy

### Return Value

True if the selected components were moved to the selected assembly or sub-assembly, false if not

## VBA Syntax

See [AssemblyDoc::ReorganizeComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ReorganizeComponents.html).

## Examples

[Reorganize Components (VBA)](Reorganize_Components_Example_VB.htm)

## Remarks

See SOLIDWORKS Help for more information about reorganizing components and restructuring assemblies.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IReorganizeComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IReorganizeComponents.html)
[IAssemblyDoc::ReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.html)
[DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler.html)
[IFeatureManager::GroupComponentInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GroupComponentInstances.html)
[IAssemblyDoc::UngroupComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UngroupComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
