---
title: "OnListboxSelectionChanged Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnListboxSelectionChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnListboxSelectionChanged.html"
---

# OnListboxSelectionChanged Method (IPropertyManagerPage2Handler9)

Called when a user changes the selected item in a list box or selection list box on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnListboxSelectionChanged( _
   ByVal Id As System.Integer, _
   ByVal Item As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer
Dim Item As System.Integer

instance.OnListboxSelectionChanged(Id, Item)
```

### C#

```csharp
void OnListboxSelectionChanged(
   System.int Id,
   System.int Item
)
```

### C++/CLI

```cpp
void OnListboxSelectionChanged(
   System.int Id,
   System.int Item
)
```

### Parameters

- `Id`: ID of the list box
- `Item`: ID of the item

## VBA Syntax

See [PropertyManagerPage2Handler9::OnListboxSelectionChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnListboxSelectionChanged.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
