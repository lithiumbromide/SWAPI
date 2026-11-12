---
title: "RemoveSectionView Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "RemoveSectionView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~RemoveSectionView.html"
---

# RemoveSectionView Method (IModelViewManager)

Removes a section view from a part and assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveSectionView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim value As System.Boolean

value = instance.RemoveSectionView()
```

### C#

```csharp
System.bool RemoveSectionView()
```

### C++/CLI

```cpp
System.bool RemoveSectionView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the section view is removed, false if not

## VBA Syntax

See [ModelViewManager::RemoveSectionView](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~RemoveSectionView.html).

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.html)
[IModelViewManager::CreateSectionViewData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionViewData.html)
[IModelViewManager::GetSectionViewData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSectionViewData.html)
[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
