---
title: "UngroupComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "UngroupComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UngroupComponents.html"
---

# UngroupComponents Method (IAssemblyDoc)

Ungroups the grouped components in the selected folder in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function UngroupComponents() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.UngroupComponents()
```

### C#

```csharp
System.bool UngroupComponents()
```

### C++/CLI

```cpp
System.bool UngroupComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the grouped components in the selected folder in the FeatureManager design tree are ungrouped, false if not

## VBA Syntax

See [AssemblyDoc::UngroupComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~UngroupComponents.html).

## Examples

[Group and Ungroup Components (C#)](Group_Components_Example_CSharp.htm)
[Group and Ungroup Components (VB.NET)](Group_Components_Example_VBNET.htm)
[Group and Ungroup Components (VBA)](Group_Components_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IFeatureManager::GroupComponentInstances Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GroupComponentInstances.html)
[IAssemblyDoc::ReorderComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.html)
[IAssemblyDoc::ReorganizeComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorganizeComponents.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
