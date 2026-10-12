---
title: "IReorderComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IReorderComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IReorderComponents.html"
---

# IReorderComponents Method (IAssemblyDoc)

Moves components to a different location in the FeatureManager tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function IReorderComponents( _
   ByVal Count As System.Integer, _
   ByRef Source As Component2, _
   ByVal Target As System.Object, _
   ByVal Where As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Source As Component2
Dim Target As System.Object
Dim Where As System.Integer
Dim value As System.Boolean

value = instance.IReorderComponents(Count, Source, Target, Where)
```

### C#

```csharp
System.bool IReorderComponents(
   System.int Count,
   ref Component2 Source,
   System.object Target,
   System.int Where
)
```

### C++/CLI

```cpp
System.bool IReorderComponents(
   System.int Count,
   Component2^% Source,
   System.Object^ Target,
   System.int Where
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of items in the Source array
- `Source`: Array of the [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) to move
- `Target`: Target component or folder feature to which to move the components
- `Where`: Where to move the components as defined in [swReorderComponentsWhere_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swReorderComponentsWhere_e.html)

### Return Value

True if the components were moved, false if not

## VBA Syntax

See [AssemblyDoc::IReorderComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IReorderComponents.html).

## Remarks

The Source argument contains the components to reorder in the FeatureManager tree.

The order of the items in the array will be the order that the components appear after the reorder occurs. The components can only be moved within the same component of the model; you cannot move a component from a subassembly into the top level assembly.

The Where argument indicates where the Source should be moved relative to the Target as defined by [swReorderComponentsWhere_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swReorderComponentsWhere_e.html). If the target is a feature, but not a folder feature, this method takes no action and returns false. Only folders that occur within the components section of the Assembly FeatureManager tree can be used; a folder that is among the body features will not be accepted. If the Where argument is specified as one of the two folder-related values, but the Target is a component, the method uses swReorderComponents_After.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.html)
[IPartDoc::ReorderFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
