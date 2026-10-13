---
title: "IPropertyManagerPageListbox Interface"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html"
---

# IPropertyManagerPageListbox Interface

Allows you to access a [PropertyManager page](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2.html) list box control.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPropertyManagerPageListbox
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
```

### C#

```csharp
public interface IPropertyManagerPageListbox
```

### C++/CLI

```cpp
public interface class IPropertyManagerPageListbox
```

## VBA Syntax

See [PropertyManagerPageListbox](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageListbox.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Remarks

Implement the event handler [IPropertyManagerPage2Handler8::OnListboxRMBUp](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnListboxRMBUp.html) to position and display a menu when the right mouse button is released.

By default, only one list item can be selected at a time. When another list item is selected, that item becomes the active item, and the previously selected item is cleared. To enable multi-selection, use swPropMgrPageListBoxStyle_MultipleItemSelect with [IProperytManagerPageListbox:Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageListbox~Style.html).

These methods support multi-selection:

- [IPropertyManagerPageListbox::GetSelectedItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItems.html) or [IPropertyManagerPageListbox::IGetSelectedItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageListbox~IGetSelectedItems.html)
- [IPropertyManagerPageListbox::GetSelectedItemsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItemsCount.html)
- [IPropertyManagerPageListbox::SetSelectedItem](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageListbox~SetSelectedItem.html)

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

## Accessors

[IPropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) and [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html)

## Access Diagram

[PropertyManagerPageListbox](SWObjectModel.pdf#PropertyManagerPageListbox)

## See Also

[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
