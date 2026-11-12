---
title: "OnPopupMenuItem Method (IPropertyManagerPage2Handler7)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler7"
member: "OnPopupMenuItem"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnPopupMenuItem.html"
---

# OnPopupMenuItem Method (IPropertyManagerPage2Handler7)

Obsoleted. Superseded by [IPropertyManagerPage2Handler8::OnPopupMenuItem](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnPopupMenuItem.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnPopupMenuItem( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler7
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

See [PropertyManagerPage2Handler7::OnPopupMenuItem](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler7~OnPopupMenuItem.html).

## Remarks

The add-in should then perform the appropriate action.

## See Also

[IPropertyManagerPage2Handler7 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7.html)
[IPropertyManagerPage2Handler7 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7_members.html)
[IPropertyManagerPage2Handler7::OnPopupMenuItemUpdate Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnPopupMenuItemUpdate.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
