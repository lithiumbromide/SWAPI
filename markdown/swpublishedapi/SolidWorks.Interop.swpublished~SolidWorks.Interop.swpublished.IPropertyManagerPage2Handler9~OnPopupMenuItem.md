---
title: "OnPopupMenuItem Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnPopupMenuItem"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnPopupMenuItem.html"
---

# OnPopupMenuItem Method (IPropertyManagerPage2Handler9)

Determines which item was selected when the user selects a pop-up menu item.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnPopupMenuItem( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
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

See [PropertyManagerPage2Handler9::OnPopupMenuItem](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnPopupMenuItem.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)
[IPropertyManagerPage2Handler9::OnPopupMenuItemUpdate Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnPopupMenuItemUpdate.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
