---
title: "OnPopupMenuItem Method (IPropertyManagerPage2Handler6)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler6"
member: "OnPopupMenuItem"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6~OnPopupMenuItem.html"
---

# OnPopupMenuItem Method (IPropertyManagerPage2Handler6)

Obsoleted. Superseded by [IPropertyManagerPage2Handler7::OnPopupMenuItem](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler7~OnPopupMenuItem.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnPopupMenuItem( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler6
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

See [PropertyManagerPage2Handler6::OnPopupMenuItem](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler6~OnPopupMenuItem.html).

## Remarks

The add-in should then perform the appropriate action.

## See Also

[IPropertyManagerPage2Handler6 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6.html)
[IPropertyManagerPage2Handler6 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6_members.html)
[IPropertyManagerPage2Handler6::OnPopupMenuItemUpdate Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6~OnPopupMenuItemUpdate.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
