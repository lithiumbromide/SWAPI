---
title: "IAddControl Method (IPropertyManagerPageGroup)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageGroup"
member: "IAddControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~IAddControl.html"
---

# IAddControl Method (IPropertyManagerPageGroup)

Obsolete. Superseded by [IPropertyManagerPageGroup::AddControl2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~AddControl2.html)

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
Dim instance As IPropertyManagerPageGroup
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

- `ID`: Resource ID of the control
- `ControlType`: Type of control as defined in [swPropertyManagerPageControlType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlType_e.html)
- `Caption`: Caption of the control
- `LeftAlign`: Left align property of this control as defined in [swPropertyManagerPageControlLeftAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlLeftAlign_e.html)
- `Options`: Options as defined in [swAddControlOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddControlOptions_e.html)
- `Tip`: ToolTip text for the control

### Return Value

Newly created [control for this PropertyManager page group box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageControl.html)

## VBA Syntax

See [PropertyManagerPageGroup::IAddControl](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageGroup~IAddControl.html).

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

When you specify swControlOptions_SmallGapAbove for the Options parameter, gap is used between a new control and the previous control that is smaller than the typical gap.

## See Also

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.html)
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.html)
[IPropertyManagerPageGroup::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~AddControl.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
