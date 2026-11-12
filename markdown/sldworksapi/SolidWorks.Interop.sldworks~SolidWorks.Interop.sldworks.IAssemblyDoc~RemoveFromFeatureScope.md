---
title: "RemoveFromFeatureScope Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "RemoveFromFeatureScope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~RemoveFromFeatureScope.html"
---

# RemoveFromFeatureScope Method (IAssemblyDoc)

Removes a component from the scope of the currently selected assembly feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveFromFeatureScope( _
   ByVal CompName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim value As System.Boolean

value = instance.RemoveFromFeatureScope(CompName)
```

### C#

```csharp
System.bool RemoveFromFeatureScope(
   System.string CompName
)
```

### C++/CLI

```cpp
System.bool RemoveFromFeatureScope(
   System.String^ CompName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompName`: Name of component to remove

### Return Value

True if successfully removed, false if not

## VBA Syntax

See [AssemblyDoc::RemoveFromFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~RemoveFromFeatureScope.html).

## Remarks

If no assembly feature is selected, this method removes a component from the list that is to be used with the next assembly feature created.

Assembly features allow you to create a feature that affects multiple components in an assembly. For example, if you need a hole through two blocks to bolt them together, you can create a hole as an assembly feature and make it go through both blocks.

The scope of the assembly feature determines which components are affected by this feature. In other words, it describes which components can contain the feature.

There are two ways to use the this technique:

- If you have an assembly feature selected, this method removes a component from the assembly features scope. Any component that is not in the scope of the assembly feature cannot be affected by the assembly feature.
- If you create a list of components, this method allows you to remove a component from the list. The next assembly feature created affects each of the components in your list.

After you use one of these techniques, you can use [IAssemblyDoc::UpdateFeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.html) to display the changes.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::UpdateFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.html)
[IAssemblyDoc::AddToFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.html)
[IAssemblyDoc::GetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.html)
[IAssemblyDoc::GetFeatureScopeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.html)
