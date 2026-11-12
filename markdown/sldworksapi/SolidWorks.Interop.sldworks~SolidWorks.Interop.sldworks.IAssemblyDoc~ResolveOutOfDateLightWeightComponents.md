---
title: "ResolveOutOfDateLightWeightComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ResolveOutOfDateLightWeightComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.html"
---

# ResolveOutOfDateLightWeightComponents Method (IAssemblyDoc)

Resolves the selected out-of-date lightweight component, and any out-of-date lightweight sub-components, in the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function ResolveOutOfDateLightWeightComponents() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.ResolveOutOfDateLightWeightComponents()
```

### C#

```csharp
System.bool ResolveOutOfDateLightWeightComponents()
```

### C++/CLI

```cpp
System.bool ResolveOutOfDateLightWeightComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if out-of-date components are resolved, false if not

## VBA Syntax

See [AssemblyDoc::ResolveOutOfDateLightWeightComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ResolveOutOfDateLightWeightComponents.html).

## Remarks

You must select a lightweight component before using this method. If the lightweight component and any of its lightweight subcomponents are out-of-date, then this method resolves them. If your selection is invalid, then this method returns false.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetLightWeightComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.html)
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html)
[IAssemblyDoc::MakeLightWeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeLightWeight.html)
[IAssemblyDoc::ResolveAllLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.html)
[IAssemblyDoc::ResolveAllLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.html)
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.html)
[IAssemblyDoc::SelectiveOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
