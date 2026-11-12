---
title: "OnPopupMenuItem Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnPopupMenuItem"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnPopupMenuItem.html"
---

# OnPopupMenuItem Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnPopupMenuItem](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnPopupMenuItem.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnPopupMenuItem( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
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

See [PropertyManagerPage2Handler8::OnPopupMenuItem](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnPopupMenuItem.html).

## Remarks

The add-in should then perform the appropriate action.

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
