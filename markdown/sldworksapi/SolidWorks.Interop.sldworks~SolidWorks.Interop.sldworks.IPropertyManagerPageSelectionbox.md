---
title: "IPropertyManagerPageSelectionbox Interface"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html"
---

# IPropertyManagerPageSelectionbox Interface

Allows you to access a [PropertyManager page](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2.html) selection box control.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPropertyManagerPageSelectionbox
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
```

### C#

```csharp
public interface IPropertyManagerPageSelectionbox
```

### C++/CLI

```cpp
public interface class IPropertyManagerPageSelectionbox
```

## VBA Syntax

See [PropertyManagerPageSelectionbox](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox.html).

## Examples

[Show Bubble ToolTip for PropertyManager Page Control (VBA)](Show_Bubble_ToolTip_for_PropertyManager_Page_Control_Example_VB.htm)

## Remarks

The behavior of your selection boxes imitates the behavior of SOLIDWORKS selection boxes, including:

- Filters that you can use to specify which types of objects can be selected for the selection box.
- Toggled object selection that selects objects on the first click, and clears them on the next click.
- Clear selections item on the shortcut menu in the model view.

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

## Accessors

[IPropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) and [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html)

## Access Diagram

[PropertyManagerPageSelectionbox](SWObjectModel.pdf#PropertyManagerPageSelectionbox)

## See Also

[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
