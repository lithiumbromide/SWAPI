---
title: "OnComboboxEditChanged Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnComboboxEditChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnComboboxEditChanged.html"
---

# OnComboboxEditChanged Method (IPropertyManagerPage2Handler9)

Called when a user changes the text string in the text box of a combo box on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnComboboxEditChanged( _
   ByVal Id As System.Integer, _
   ByVal Text As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer
Dim Text As System.String

instance.OnComboboxEditChanged(Id, Text)
```

### C#

```csharp
void OnComboboxEditChanged(
   System.int Id,
   System.string Text
)
```

### C++/CLI

```cpp
void OnComboboxEditChanged(
   System.int Id,
   System.String^ Text
)
```

### Parameters

- `Id`: ID of the combo box
- `Text`: Text string

## VBA Syntax

See [PropertyManagerPage2Handler9::OnComboboxEditChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnComboboxEditChanged.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

This method is only called if the combo box was set up as an editable text box. If the combo box is set up to as a static text box, then this method is not called.

If the user can edit the text in the text box, then use this method with [IPropertyManagerPage2Handler9::OnComboxSelectionChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnComboboxSelectionChanged.html) to find out what is in the text box of the combo box.

When this method is called, the control may not yet be updated with the current selection, so the [IPropertyManagerPageCombobox::CurrentSelection](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageCombobox~CurrentSelection.html) property is not reliable. The text passed into this method is the up-to-date text.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
