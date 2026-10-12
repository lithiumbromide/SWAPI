---
title: "AddControl Method (IPropertyManagerPageTab)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageTab"
member: "AddControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~AddControl.html"
---

# AddControl Method (IPropertyManagerPageTab)

Obsolete. Superseded by [IPropertyManagerPageTab::AddControl2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageTab~AddControl2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function AddControl( _
   ByVal ID As System.Integer, _
   ByVal ControlType As System.Short, _
   ByVal Caption As System.String, _
   ByVal LeftAlign As System.Short, _
   ByVal Options As System.Integer, _
   ByVal Tip As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageTab
Dim ID As System.Integer
Dim ControlType As System.Short
Dim Caption As System.String
Dim LeftAlign As System.Short
Dim Options As System.Integer
Dim Tip As System.String
Dim value As System.Object

value = instance.AddControl(ID, ControlType, Caption, LeftAlign, Options, Tip)
```

### C#

```csharp
System.object AddControl(
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
System.Object^ AddControl(
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

- `ID`: Resource ID of this control
- `ControlType`: Type of control as defined in [swPropertyManagerPageControlType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlType_e.html)
- `Caption`: Caption of the control
- `LeftAlign`: Left alignment of this control as defined in [swPropertyManagerPageControlLeftAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlLeftAlign_e.html)
- `Options`: Options as defined in [swAddControlOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddControlOptions_e.html) (see **Remarks**)
- `Tip`: Tool tip text for the control

### Return Value

Newly created [PropertyManager page tab control](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageControl.html)

## VBA Syntax

See [PropertyManagerPageTab::AddControl](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageTab~AddControl.html).

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

This method associates controls with a tab. When a user clicks a tab, controls associated with that tab are automatically shown and controls not associated with that tab are automatically hidden.

However, any controls added to a tab using [IPropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) or [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html) are not associated with the tab; you must still hide and show those controls. But, because the name of this method and its parameters are identical to IPropertyManagerPage2::AddControl or IPropertyManagerPage2::IAddControl, switching to this method and cleaning up your handler code should be easy.

To add a control to a group box associated with a tab, add the controls from the [group box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.html). Only use this method to add controls not associated with group boxes.

When you specify swControlOptions_SmallGapAbove for the Options parameter, gap is used between a new control and the previous control that is smaller than the typical gap.

## See Also

[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.html)
[IPropertyManagerPageTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab_members.html)
[IPropertyManagerPageTab::IAddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~IAddControl.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
