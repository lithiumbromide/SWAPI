---
title: "IPropertyManagerPageNumberbox Interface"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html"
---

# IPropertyManagerPageNumberbox Interface

Allows you to access a [PropertyManager page](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2.html) number box control.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPropertyManagerPageNumberbox
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
```

### C#

```csharp
public interface IPropertyManagerPageNumberbox
```

### C++/CLI

```cpp
public interface class IPropertyManagerPageNumberbox
```

## VBA Syntax

See [PropertyManagerPageNumberbox](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageNumberbox.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

| If you implement a... | Then... |
| --- | --- |
| Spin box | an edit box with attached up and down arrow buttons for incrementing and decrementing the value is created. |
| Combo box/spin box | a text box with: a down-arrow button to display the attached drop-down list. You must set up and control the attached drop-down list up and down buttons for incrementing and decrementing the value is created. Use IPropertyManagerPageNumberbox::Style to select the type of combo-box/spin-box number box you want to implement. |

For both types of number boxes, SOLIDWORKS automatically validates the values and units. The up and down arrow buttons automatically increment and decrement the value. Both types of number boxes:

- Accept numerical expressions.
- Store all values as meters or radians and display them in the units specified in the current unit settings.

NOTE: When a document's unit system is set to a non-metric setting, the dimension precision value (the number of digits displayed after a decimal point) is based on the number of digits specified. It is not based on the document's dimension precision settings.

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

## Accessors

[IPropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) and [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html)

## Access Diagram

[PropertyManagerPageNumberbox](SWObjectModel.pdf#PropertyManagerPageNumberbox)

## See Also

[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
