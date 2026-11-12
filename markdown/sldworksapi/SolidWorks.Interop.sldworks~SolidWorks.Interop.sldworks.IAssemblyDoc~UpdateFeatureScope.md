---
title: "UpdateFeatureScope Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "UpdateFeatureScope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.html"
---

# UpdateFeatureScope Method (IAssemblyDoc)

Updates the feature scope and rebuilds the currently selected assembly feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UpdateFeatureScope()
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc

instance.UpdateFeatureScope()
```

### C#

```csharp
void UpdateFeatureScope()
```

### C++/CLI

```cpp
void UpdateFeatureScope();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [AssemblyDoc::UpdateFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~UpdateFeatureScope.html).

## Remarks

You can use assembly features to create a feature that affects multiple components in an assembly. For example, if you need a hole through two blocks to bolt them together, you can create a hole as an assembly feature that goes through both of the blocks.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddToFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.html)
[IAssemblyDoc::GetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.html)
[IAssemblyDoc::GetFeatureScopeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.html)
[IAssemblyDoc::RemoveFromFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~RemoveFromFeatureScope.html)
