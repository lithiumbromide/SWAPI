---
title: "GetFeatureTreeRootItem Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetFeatureTreeRootItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFeatureTreeRootItem.html"
---

# GetFeatureTreeRootItem Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::GetFeatureTreeRootItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~GetFeatureTreeRootItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureTreeRootItem() As TreeControlItem
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As TreeControlItem

value = instance.GetFeatureTreeRootItem()
```

### C#

```csharp
TreeControlItem GetFeatureTreeRootItem()
```

### C++/CLI

```cpp
TreeControlItem^ GetFeatureTreeRootItem();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Root item in the FeatureManager design tree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem.html)

## VBA Syntax

See [FeatureManager::GetFeatureTreeRootItem](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetFeatureTreeRootItem.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
