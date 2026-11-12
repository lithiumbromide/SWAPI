---
title: "OnComboboxSelectionChanged Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnComboboxSelectionChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnComboboxSelectionChanged.html"
---

# OnComboboxSelectionChanged Method (IPropertyManagerPage2Handler9)

Called when a user changes the selected item in a combo box on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnComboboxSelectionChanged( _
   ByVal Id As System.Integer, _
   ByVal Item As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer
Dim Item As System.Integer

instance.OnComboboxSelectionChanged(Id, Item)
```

### C#

```csharp
void OnComboboxSelectionChanged(
   System.int Id,
   System.int Item
)
```

### C++/CLI

```cpp
void OnComboboxSelectionChanged(
   System.int Id,
   System.int Item
)
```

### Parameters

- `Id`: ID of the combo box
- `Item`: ID of the item

## VBA Syntax

See [PropertyManagerPage2Handler9::OnComboboxSelectionChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnComboboxSelectionChanged.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

If the user can edit the text in the text box, then use this method with [IPropertyManagerPage2Handler9::OnComboxEditChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnComboboxEditChanged.html) to find out what is in the text box of the combo box.

When this method is called, the control may not yet be updated with the current selection, so the [IPropertyManagerPageCombobox::CurrentSelection](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageCombobox~CurrentSelection.html) property is not reliable. To get the current text, use the value of Item that is passed into the method as the argument to [IPropertyManagerPageCombobox::ItemText](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageCombobox~ItemText.html).

If the user has edited the text in the text box and then clicks the arrow to show or hide the list box of the combo box, and the text in the text box matches the first character in any of the items in the list, then that item is automatically selected in the list and this method is called, indicating that the selected item has changed.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
