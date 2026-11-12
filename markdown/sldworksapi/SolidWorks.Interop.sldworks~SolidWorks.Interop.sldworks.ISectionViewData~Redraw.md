---
title: "Redraw Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "Redraw"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~Redraw.html"
---

# Redraw Property (ISectionViewData)

Gets or sets whether to have [IModelViewManager::CreateSectionView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateSectionView.html) validate and return a status for section bodies instead of section views.

## Syntax

### Visual Basic (Declaration)

```vb
Property Redraw As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.Redraw = value

value = instance.Redraw
```

### C#

```csharp
System.bool Redraw {get; set;}
```

### C++/CLI

```cpp
property System.bool Redraw {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to validate and return a status for newly created section bodies, false to not

## VBA Syntax

See [SectionViewData::Redraw](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~Redraw.html).

## Examples

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)

## Remarks

By default, [IModelViewManager::CreateSectionView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateSectionView.html) returns whether it successfully created a section view. Set this property to true to have [IModelViewManager::CreateSectionView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateSectionView.html) check and return whether it successfully created the section bodies.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
