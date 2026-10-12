---
title: "Using PropertyManagerPage2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm"
---

# Using PropertyManagerPage2

## Using IPropertyManagerPage2 and the Related Objects

[IPropertyManagerPage2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPage2.html) and related objects provide an add-in application with the ability to create a PropertyManager page with the same look and feel as SOLIDWORKS PropertyManager pages. The SOLIDWORKS API provides a series of standard controls that are managed by SOLIDWORKS Design.

This topic explains:

- [What is available?](#available)
- [What does the add-in have to do?](#add_in)
- [What does the SOLIDWORKS application do?](#application)
- [IPropertyManagerPage2 states](#states)

### What is available?

The SOLIDWORKS API provides:

- Standard buttons for OK, Cancel, Next Page, Previous Page, and Help
- Confirmation corner display in the model view
- Bitmaps ([IPropertyManagerPageBitmap](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageBitmap.html))
- Buttons ([IPropertyManagerPageButton](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageButton.html) and [IPropertyManagerPageBitmapButton](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageBitmapButton.html))
- Pull-down groups with check boxes ([IPropertyManagerPageGroup](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageGroup.html))
- Check boxes ([IPropertyManagerPageCheckbox](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageCheckbox.html))
- Radio buttons ([IPropertyManagerPageOption](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageOption.html))
- Number input boxes with application-defined spin control ([IPropertyManagerPageNumberbox](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageNumberbox.html))
- Text boxes ([IPropertyManagerPageTextbox](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageTextbox.html))
- List boxes ([IPropertyManagerPageListbox](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageListbox.html))
- Combo boxes ([IPropertyManagerPageCombobox](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageCombobox.html))
- Selection list boxes ([IPropertyManagerPageSelectionbox](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageSelectionbox.html))
- Labels ([IPropertyManagerPageLabel](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageLabel.html))
- Sliders ([IPropertyManagerPageSlider](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageSlider.html))
- Tabs ([IPropertyManagerPageTab](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageTab.html))
- ActiveX controls ([IPropertyManagerPageActiveX](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageActiveX.html))
- .NET controls ([IPropertyManagerPageWindowFromHandle](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageWindowFromHandle.html))
- A set of methods and properties common to all controls ([IPropertyManagerPageControl](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageControl.html))

See [Controls on Multipage PropertyManager Page](Controls_on_Multipage_PropertyManager_Page.htm) for details about programming controls on a multipage PropertyManager page.

[Back to top](#top)

### What does the add-in have to do?

To take advantage of this functionality, the add-in application must:

1. Implement an object that supports [IPropertyManagerPage2Handler8](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.IPropertyManagerPage2Handler8.html).
2. Call [ISldWorks::CreatePropertyManagerPage](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISldWorks~CreatePropertyManagerPage.html) to create the new page, including a pointer to the IPropertyManagerPage2Handler8 for that page.
3. Use the pointer returned by ISldWorks::CreatePropertyManagerPage to add group boxes and controls to the new page using [IPropertyManagerPage2::AddControl](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPage2~AddControl.html), [IPropertyManagerPage2::AddGroupBox](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPage2~AddGroupBox.html), and [IPropertyManagerPageGroup::AddControl.](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPageGroup~AddControl.html)
4. Call [IPropertyManagerPage2::Show](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IPropertyManagerPage2~Show.html) to display the PropertyManager page in the user interface.
5. Respond to events generated by the SOLIDWORKS Design application (such as [IPropertyManagerPage2Handler8::OnButtonPress](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.IPropertyManagerPage2Handler8~OnButtonPress.html) or [IPropertyManagerPage2Handler8::OnClose](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.IPropertyManagerPage2Handler8~OnClose.html)) to collect data that your user typed in the PropertyManager page and take action based on that data, if necessary.
6. Destroy the IPropertyManagerPage2 object.

[Back to top](#top)

### What does the SOLIDWORKS Design application do?

When you create a IPropertyManagerPage2 object, SOLIDWORKS Design:

1. Creates the PropertyManager page (not visible) and associates it with the specified IPropertyManagerPage2Handler8 in the add-in application.
2. Makes calls to the IPropertyManagerPage2Handler8 based on end-user-initiated events.
3. Closes the PropertyManager page in the user interface when the end-user clicks OK or Cancel, but does not destroy the IPropertyManagerPage2 object.

[Back to top](#top)

### IPropertyManagerPage2 states

The controls associated with IPropertyManagerPage2 have two distinct states: not visible and visible.

When the PropertyManager is not visible, the window does not exist. The only items that exist are the API objects. These objects hold onto only the default values that are set by the application before it displays the PropertyManager.

When the PropertyManager is visible, the objects represent the controls displayed in the PropertyManager window. When a given control is queried, the value represents the current setting of the control.

These states are important because if the end-user closes a PropertyManager page, you cannot determine the user-specified value for the control. It is up to you to provide data exchange between your application and the controls while they are visible and before the PropertyManager page goes away.

[Back to top](#top)
