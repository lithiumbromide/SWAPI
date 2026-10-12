---
title: "CreateSectionView Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "CreateSectionView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.html"
---

# CreateSectionView Method (IModelViewManager)

Creates a section view in parts and assemblies.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSectionView( _
   ByVal SectionData As SectionViewData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim SectionData As SectionViewData
Dim value As System.Boolean

value = instance.CreateSectionView(SectionData)
```

### C#

```csharp
System.bool CreateSectionView(
   SectionViewData SectionData
)
```

### C++/CLI

```cpp
System.bool CreateSectionView(
   SectionViewData^ SectionData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SectionData`: [Section view data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData.html)

### Return Value

True if the section view is created, false if not (**see** **Remarks**)

## VBA Syntax

See [ModelViewManager::CreateSectionView](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~CreateSectionView.html).

## Examples

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)

## Remarks

To create a section view in a part or assembly:

1. Use [IModelViewManager::CreateSectionViewData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateSectionViewData.html) to create the SectionViewData object.
2. Set the properties of [ISectionViewData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData.html).
3. Use IModelViewManager::CreateSectionView to create the section view. This method only returns whether it successfully created the section view. It does not return whether it created valid section bodies. Set [ISectionViewData::Redraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData~Redraw.html) to true to have IModelViewManager::CreateSectionView validate and return a status for section bodies instead of section views.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::GetSectionViewData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSectionViewData.html)
[IModelViewManager::RemoveSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~RemoveSectionView.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
