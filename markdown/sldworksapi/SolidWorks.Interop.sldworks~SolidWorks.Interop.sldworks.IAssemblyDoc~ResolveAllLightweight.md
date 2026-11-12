---
title: "ResolveAllLightweight Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ResolveAllLightweight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.html"
---

# ResolveAllLightweight Method (IAssemblyDoc)

Resolves all lightweight child components of the selected components

## Syntax

### Visual Basic (Declaration)

```vb
Function ResolveAllLightweight() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.ResolveAllLightweight()
```

### C#

```csharp
System.bool ResolveAllLightweight()
```

### C++/CLI

```cpp
System.bool ResolveAllLightweight();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if all lightweight child components of the selected components are resolved, false if not

## VBA Syntax

See [AssemblyDoc::ResolveAllLightweight](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ResolveAllLightweight.html).

## Remarks

If no components are selected, then this method is applied to this assembly document.

Suppressed components are ignored.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetLightWeightComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.html)
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html)
[IAssemblyDoc::MakeLightWeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeLightWeight.html)
[IAssemblyDoc::ResolveAllLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.html)
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.html)
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.html)
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.html)
[IAssemblyDoc::SelectiveOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.html)

## Availability

SOLIDWORKS SP1, Revision Number 14
