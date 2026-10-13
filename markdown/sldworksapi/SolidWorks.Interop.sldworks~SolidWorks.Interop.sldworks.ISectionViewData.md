---
title: "ISectionViewData Interface"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html"
---

# ISectionViewData Interface

Allows you to create and access section views in parts and assemblies.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISectionViewData
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
```

### C#

```csharp
public interface ISectionViewData
```

### C++/CLI

```cpp
public interface class ISectionViewData
```

## VBA Syntax

See [SectionViewData](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData.html).

## Examples

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)
[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)
[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

## Remarks

A section view is defined by multiple planes, colors, offsets, etc.

To create a section view in a part or assembly:

1. Use [IModelViewManager::CreateSectionViewData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateSectionViewData.html) to create the ISectionViewData object.
2. Set the properties of ISectionViewData.
3. Use [IModelViewManager::CreateSectionView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateSectionView.html) to create the section view. IModelViewManager::CreateSectionView returns whether it successfully created the section view; it does not return whether it successfully created valid section bodies. Set [ISectionViewData::Redraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData~Redraw.html) to true to have IModelViewManager::CreateSectionView validate and return a status for section bodies instead of section views.

## Accessors

[IModelViewManager::CreateSectionViewData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateSectionViewData.html)

[IModelViewManager::GetSectionViewData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~GetSectionViewData.html)

## Access Diagram

[SectionViewData](SWObjectModel.pdf#SectionViewData)

## See Also

[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
