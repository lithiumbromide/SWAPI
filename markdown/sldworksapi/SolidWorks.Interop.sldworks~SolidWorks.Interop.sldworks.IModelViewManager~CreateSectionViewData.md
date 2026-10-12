---
title: "CreateSectionViewData Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "CreateSectionViewData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionViewData.html"
---

# CreateSectionViewData Method (IModelViewManager)

Creates an empty [ISectionViewData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData.html) object whose properties you set before [creating a section view in a part or an assembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateSectionView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSectionViewData() As SectionViewData
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim value As SectionViewData

value = instance.CreateSectionViewData()
```

### C#

```csharp
SectionViewData CreateSectionViewData()
```

### C++/CLI

```cpp
SectionViewData^ CreateSectionViewData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Section view data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData.html)

## VBA Syntax

See [ModelViewManager::CreateSectionViewData](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~CreateSectionViewData.html).

## Examples

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)

## Remarks

To create a section view in a part or assembly:

1. Use this method to create the SectionViewData object.
2. Set the properties of [ISectionViewData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData.html).
3. Use [IModelViewManager::CreateSectionView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateSectionView.html) to create the section view. IModelViewManager::CreateSectionView only returns whether it successfully created the section view. It does not return whether it created valid section bodies. Set [ISectionViewData::Redraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData~Redraw.html) to true to have IModelViewManager::CreateSectionView validate and return a status for section bodies.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::GetSectionViewData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSectionViewData.html)
[IModelViewManager::RemoveSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~RemoveSectionView.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
