---
title: "AddToFeatureScope Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddToFeatureScope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.html"
---

# AddToFeatureScope Method (IAssemblyDoc)

Adds a component to the scope of the currently selected assembly feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddToFeatureScope( _
   ByVal CompName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim value As System.Boolean

value = instance.AddToFeatureScope(CompName)
```

### C#

```csharp
System.bool AddToFeatureScope(
   System.string CompName
)
```

### C++/CLI

```cpp
System.bool AddToFeatureScope(
   System.String^ CompName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompName`: Name of component to add

### Return Value

True if added successfully, false otherwise

## VBA Syntax

See [AssemblyDoc::AddToFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddToFeatureScope.html).

## Remarks

If no assembly feature is selected, then this method adds a component to a list for use with the next assembly feature created.

Assembly features allow you to create a feature that affects multiple components in an assembly. For example, if you need a hole through two blocks so that you could bolt them together, you can create a hole as an assembly feature and make it go through both blocks.

The scope of the assembly feature determines which components are effected by this feature. In other words, it describes which components can contain the feature.

There are two ways to use the IAssemblyDoc::AddToFeatureScope method:

- When an assembly feature is selected, IAssemblyDoc::AddToFeatureScope adds a component to the assembly feature's scope. Any component in the scope of the assembly feature can be affected by the assembly feature.
- You can also use IAssemblyDoc::AddToFeatureScope to compile a group of components. The next assembly feature created (for example, [IFeatureManager::SimpleHole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SimpleHole.html)) affects each of the components in the compiled group.

After completing these steps, use [IAssemblyDoc::UpdateFeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.html) to display the changes.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
