---
title: "LightweightAllResolved Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "LightweightAllResolved"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html"
---

# LightweightAllResolved Method (IAssemblyDoc)

Sets to lightweight all resolved child components of the selected components.

## Syntax

### Visual Basic (Declaration)

```vb
Function LightweightAllResolved() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.LightweightAllResolved()
```

### C#

```csharp
System.bool LightweightAllResolved()
```

### C++/CLI

```cpp
System.bool LightweightAllResolved();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if all child components of the selected components are set to lightweight, false if not

## VBA Syntax

See [AssemblyDoc::LightweightAllResolved](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~LightweightAllResolved.html).

## Remarks

If no components are selected, then this method is applied to this assembly document.

Suppressed components are ignored.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetLightWeightComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.html)
[IAssemblyDoc::ResolveAllLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.html)
[IAssemblyDoc::ResolveAllLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.html)
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.html)
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.html)
[IComponent2::GetSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.html)
[IComponent2::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.html)
[IAssemblyDoc::MakeLightWeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeLightWeight.html)
[IAssemblyDoc::SelectiveOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.html)

## Availability

SOLIDWORKS 2006 SP1, Revision Number 14
