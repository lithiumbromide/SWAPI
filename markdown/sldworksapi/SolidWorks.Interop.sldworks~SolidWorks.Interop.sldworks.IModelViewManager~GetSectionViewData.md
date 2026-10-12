---
title: "GetSectionViewData Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "GetSectionViewData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSectionViewData.html"
---

# GetSectionViewData Method (IModelViewManager)

Gets access to the data of the specified section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSectionViewData( _
   ByVal ViewName As System.String _
) As SectionViewData
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim ViewName As System.String
Dim value As SectionViewData

value = instance.GetSectionViewData(ViewName)
```

### C#

```csharp
SectionViewData GetSectionViewData(
   System.string ViewName
)
```

### C++/CLI

```cpp
SectionViewData^ GetSectionViewData(
   System.String^ ViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`: Name of the section view or an empty string for the active section view

### Return Value

[Section view data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData.html)

## VBA Syntax

See [ModelViewManager::GetSectionViewData](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~GetSectionViewData.html).

## Examples

[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)

## Remarks

If the specified string refers to a non-existent section view or a view that is not sectioned, then this method returns Nothing or null.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.html)
[IModelViewManager::CreateSectionViewData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionViewData.html)
[IModelViewManager::RemoveSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~RemoveSectionView.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
