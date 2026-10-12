---
title: "MakeLightWeight Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "MakeLightWeight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeLightWeight.html"
---

# MakeLightWeight Method (IAssemblyDoc)

Sets the selected components to lightweight.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MakeLightWeight()
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc

instance.MakeLightWeight()
```

### C#

```csharp
void MakeLightWeight()
```

### C++/CLI

```cpp
void MakeLightWeight();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [AssemblyDoc::MakeLightWeight](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~MakeLightWeight.html).

## Examples

[Make Assembly Components Lightweight (VBA)](Make_Assembly_Components_Lightweight_Example_VB.htm)

## Remarks

The purpose of this method is to support recording macros. You should use [IComponent2::GetSuppression](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetSuppression.html) or [IComponent2::SetSuppression2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetSuppression2.html) to get or set a component to lightweight.

This method sets the current selected components to lightweight, which is suitable for recording and running macros. IComponent2::GetSuppression and IComponent2::SetSuppression2 operate on the component itself.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ResolveAllLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.html)
[IAssemblyDoc::ResolveAllLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.html)
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.html)
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html)
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.html)
[IComponent2::GetSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.html)
[IComponent2::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.html)
[IAssemblyDoc::SelectiveOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
