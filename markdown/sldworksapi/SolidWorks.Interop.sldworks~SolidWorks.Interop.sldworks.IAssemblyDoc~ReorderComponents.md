---
title: "ReorderComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ReorderComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.html"
---

# ReorderComponents Method (IAssemblyDoc)

Moves components to a different location in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReorderComponents( _
   ByVal Source As System.Object, _
   ByVal Target As System.Object, _
   ByVal Where As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Source As System.Object
Dim Target As System.Object
Dim Where As System.Integer
Dim value As System.Boolean

value = instance.ReorderComponents(Source, Target, Where)
```

### C#

```csharp
System.bool ReorderComponents(
   System.object Source,
   System.object Target,
   System.int Where
)
```

### C++/CLI

```cpp
System.bool ReorderComponents(
   System.Object^ Source,
   System.Object^ Target,
   System.int Where
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Source`: Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) to move
- `Target`: Target component or folder to which to move the components
- `Where`: Where to move the components as defined in [swReorderComponentsWhere_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swReorderComponentsWhere_e.html)

### Return Value

True if the components are moved, false if not

## VBA Syntax

See [AssemblyDoc::ReorderComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ReorderComponents.html).

## Examples

[Move Assembly Components to New Folder (C#)](Move_Assembly_Components_to_New_Folder_Example_CSharp.htm)
[Move Assembly Components to New Folder (VB.NET)](Move_Assembly_Components_to_New_Folder_Example_VBNET.htm)
[Move Assembly Components to New Folder (VBA)](Move_Assembly_Components_to_New_Folder_Example_VB.htm)

## Remarks

The Source argument contains the components to reorder in the FeatureManager design tree.

The order of the elements in the array will be the order that the components appear after the reorder occurs. The components can only be moved within the same component of the model; you cannot move a component from a subassembly into the top-level assembly.

The Where argument indicates where the Source should be moved relative to the Target as defined by swReorderComponentsWhere_e. If the target is not a folder feature, then this method takes no action and returns false. Only folders that occur within the components section of the assembly FeatureManager design tree can be used; a folder that is among the body features will not be accepted. If the Where argument is specified as one of the two folder-related values, but the Target is a component, the method uses swReorderCompentsWhere_e.swReorderComponents_After.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IReorderComponents.html)
[IFeatureManager::InsertFeatureTreeFolder2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureTreeFolder2.html)
[IFeatureManager::GroupComponentInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GroupComponentInstances.html)
[IAssemblyDoc::UngroupComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UngroupComponents.html)
[IPartDoc::ReorderFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature.html)
[IModelDocExtension::ReorderFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
