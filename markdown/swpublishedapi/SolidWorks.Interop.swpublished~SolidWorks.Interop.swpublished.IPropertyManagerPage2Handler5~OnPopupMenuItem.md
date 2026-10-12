---
title: "OnPopupMenuItem Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnPopupMenuItem"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnPopupMenuItem.html"
---

# OnPopupMenuItem Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnPopupMenuItem](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnPopupMenuItem.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnPopupMenuItem( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler5
Dim Id As System.Integer

instance.OnPopupMenuItem(Id)
```

### C#

```csharp
void OnPopupMenuItem(
   System.int Id
)
```

### C++/CLI

```cpp
void OnPopupMenuItem(
   System.int Id
)
```

### Parameters

- `Id`: Unique user-defined ID for a pop-up menu item (see [IPropertyManagerPage2::AddMenuPopupItem](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddMenuPopupItem.html))

## VBA Syntax

See [PropertyManagerPage2Handler5::OnPopupMenuItem](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnPopupMenuItem.html).

## Remarks

The add-in should then perform the appropriate action.

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)
[IPropertyManagerPage2Handler5::OnPopupMenuItemUpdate Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnPopupMenuItemUpdate.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
