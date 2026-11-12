---
title: "OnPopupMenuItemUpdate Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnPopupMenuItemUpdate"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnPopupMenuItemUpdate.html"
---

# OnPopupMenuItemUpdate Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnPopupMenuItemUpdate](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnPopupMenuItemUpdate.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnPopupMenuItemUpdate( _
   ByVal Id As System.Integer, _
   ByRef retval As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
Dim Id As System.Integer
Dim retval As System.Integer

instance.OnPopupMenuItemUpdate(Id, retval)
```

### C#

```csharp
void OnPopupMenuItemUpdate(
   System.int Id,
   ref System.int retval
)
```

### C++/CLI

```cpp
void OnPopupMenuItemUpdate(
   System.int Id,
   System.int% retval
)
```

### Parameters

- `Id`: Unique user-defined ID for a pop-up menu item (see [IPropertyManagerPage2::AddMenuPopupItem](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddMenuPopupItem.html))
- `retval`: State of the specified unique user-defined pop-up menu item:

  - 0 - Not selected (i.e., not checked) and disabled (i.e., grayed out)
  - 1 - Not selected and enabled
  - 2 - Selected (i.e., checked) and disabled
  - 3 - Selected and enabled

## VBA Syntax

See [PropertyManagerPage2Handler8::OnPopupMenuItemUpdate](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnPopupMenuItemUpdate.html).

## Remarks

Thus, this method:

- Processes a request for the state of the specified pop-up menu item associated with the PropertyManager page.
- Passes the state back to SOLIDWORKS.

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
