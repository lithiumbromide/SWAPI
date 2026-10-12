---
title: "IPropertyManagerPage2 Interface"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html"
---

# IPropertyManagerPage2 Interface

Provides add-in applications the ability to display and use views that have the look and feel of SOLIDWORKS PropertyManager pages.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPropertyManagerPage2
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
```

### C#

```csharp
public interface IPropertyManagerPage2
```

### C++/CLI

```cpp
public interface class IPropertyManagerPage2
```

## VBA Syntax

See [PropertyManagerPage2](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2.html).

## Examples

To create a .NET add-in that implements this interface, start with one of these Visual Studio projects:

- Visual Basic - SwVBAddin
- Visual C# - SwCSharpAddin

## Examples

[Create PropertyManager Page (VBA)](Create_PropertyManager_Page_Example_VB.htm)

## Remarks

OK and Cancel buttons are optional for IPropertyManagerPage2 objects, but a Help button is always displayed. If you do not want to implement help for your add-in, return false on help notification to display SOLIDWORKS Help.

PropertyManager controls are displayed in a single, left-aligned column. Slight vertical spacing adjustment is available with the [IPropertyManagerPageGroup::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~AddControl.html) or [IPropertyManagerPageGroup::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~IAddControl.html) or the [PropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) or [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html) Options argument.

Use [IModelDocExtension::GetUserPreferenceInteger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html)(swPropertyManagerColorDivider,UserPrefOption) to get the color of the PropertyManager divider box backgrounds for custom bitmap color blending purposes. The returned integer value is the COLORREF value.

The add-in application must implement the [IPropertyManagerPage2Handler8](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8.html) interface for data to be exchanged with the add-in application. The add-in application owns the IPropertyManagerPage2 object, which owns the IPropertyManagerPage2Handler8 for that page.

The limits on the number of controls on a PropertyManager page are:

- Total number of controls = 300 (This number does not include group and selection boxes.)
- Total number of group boxes = 20
- Total number of selection boxes = 15

NOTE: Number boxes count as 2 controls. All other controls count as 1 control.

SOLIDWORKS does not allow suppressing components or features while a PropertyManager page is open.

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

## Accessors

[ISldWorks::CreatePropertyManagerPage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.html) and [ISldWorks::ICreatePropertyManagerPage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.html)

## Access Diagram

[PropertyManagerPage2](SWObjectModel.pdf#PropertyManagerPage2)

## See Also

[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IPropertyManagerPageActiveX Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX.html)
[IPropertyManagerPageBitmap Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap.html)
[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.html)
[IPropertyManagerPageButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton.html)
[IPropertyManagerPageCheckbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox.html)
[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html)
[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.html)
[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageOption Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageOption.html)
[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.html)
[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.html)
[IPropertyManagerPageTextbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTextbox.html)
[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html)
[IModelDocExtension::GetActivePropertyManagerPage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetActivePropertyManagerPage.html)
