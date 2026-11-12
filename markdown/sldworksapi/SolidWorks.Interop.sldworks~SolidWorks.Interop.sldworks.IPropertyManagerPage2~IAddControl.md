---
title: "IAddControl Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "IAddControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddControl.html"
---

# IAddControl Method (IPropertyManagerPage2)

Obsolete. Superseded by [IPropertyManagerPage2::AddControl2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddControl( _
   ByVal ID As System.Integer, _
   ByVal ControlType As System.Short, _
   ByVal Caption As System.String, _
   ByVal LeftAlign As System.Short, _
   ByVal Options As System.Integer, _
   ByVal Tip As System.String _
) As PropertyManagerPageControl
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim ControlType As System.Short
Dim Caption As System.String
Dim LeftAlign As System.Short
Dim Options As System.Integer
Dim Tip As System.String
Dim value As PropertyManagerPageControl

value = instance.IAddControl(ID, ControlType, Caption, LeftAlign, Options, Tip)
```

### C#

```csharp
PropertyManagerPageControl IAddControl(
   System.int ID,
   System.short ControlType,
   System.string Caption,
   System.short LeftAlign,
   System.int Options,
   System.string Tip
)
```

### C++/CLI

```cpp
PropertyManagerPageControl^ IAddControl(
   System.int ID,
   System.short ControlType,
   System.String^ Caption,
   System.short LeftAlign,
   System.int Options,
   System.String^ Tip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Resource ID of this control; API passes this user-defined value back to the add-in through the [IPropertyManagerPage2Handler8](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8.html) interface
- `ControlType`: Type of control as defined in [swPropertyManagerPageControlType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlType_e.html)
- `Caption`: Caption of this control
- `LeftAlign`: Left-align property of this control as defined in [swPropertyManagerPageControlLeftAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlLeftAlign_e.html)
- `Options`: Options as defined in [swAddControlOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddControlOptions_e.html)
- `Tip`: ToolTip for this control

### Return Value

Newly created [PropertyManage page control](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageControl.html)

## VBA Syntax

See [PropertyManagerPage2::IAddControl](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~IAddControl.html).

## Examples

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

## Remarks

You can only use this method to set properties on the PropertyManager before the page is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

To follow the SOLIDWORKS standards when designing a new PropertyManager page, it is a good idea to use [IPropertyManagerPage2::AddGroupBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.html) or [IPropertyManagerPage2::IAddGroupBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.html) and [IPropertyManagerPageGroup::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) or IPropertyManagerPageGroup::IAddControl to add controls for the page inside group boxes.

When you specify swControlOptions_SmallGapAbove for the Options parameter, a gap, smaller than the typical gap, is used between a new control and the previous control.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
