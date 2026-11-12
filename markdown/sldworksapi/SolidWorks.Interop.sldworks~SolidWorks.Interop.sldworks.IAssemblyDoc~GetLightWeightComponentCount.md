---
title: "GetLightWeightComponentCount Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetLightWeightComponentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.html"
---

# GetLightWeightComponentCount Method (IAssemblyDoc)

Gets the number of lightweight components in the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLightWeightComponentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Integer

value = instance.GetLightWeightComponentCount()
```

### C#

```csharp
System.int GetLightWeightComponentCount()
```

### C++/CLI

```cpp
System.int GetLightWeightComponentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of lightweight components

## VBA Syntax

See [AssemblyDoc::GetLightWeightComponentCount](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetLightWeightComponentCount.html).

## Examples

[Make Assembly Components Lightweight (VBA)](Make_Assembly_Components_Lightweight_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html)
[IAssemblyDoc::ResolveAllLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.html)
[IAssemblyDoc::ResolveAllLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.html)
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.html)
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.html)
