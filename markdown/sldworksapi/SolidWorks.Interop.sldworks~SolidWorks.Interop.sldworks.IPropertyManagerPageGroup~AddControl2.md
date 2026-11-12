---
title: "AddControl2 Method (IPropertyManagerPageGroup)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageGroup"
member: "AddControl2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~AddControl2.html"
---

# AddControl2 Method (IPropertyManagerPageGroup)

Adds a control to this PropertyManager page group box.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddControl2( _
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
Dim instance As IPropertyManagerPageGroup
Dim ID As System.Integer
Dim ControlType As System.Short
Dim Caption As System.String
Dim LeftAlign As System.Short
Dim Options As System.Integer
Dim Tip As System.String
Dim value As System.Object

value = instance.AddControl2(ID, ControlType, Caption, LeftAlign, Options, Tip)
```

### C#

```csharp
System.object AddControl2(
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
System.Object^ AddControl2(
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
- `LeftAlign`: Left alignment of this control as defined in [swPropertyManagerPageControlLeftAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlLeftAlign_e.html)
- `Options`: Options as defined in [swAddControlOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddControlOptions_e.html) (see **Remarks**)
- `Tip`: ToolTip text for the control

### Return Value

Newly created [control for this PropertyManager page group box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageControl.html)

## VBA Syntax

See [PropertyManagerPageGroup::AddControl2](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageGroup~AddControl2.html).

## Examples

See the [IPropertyManagerPageGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.html) examples.

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

When you specify swAddControlOptions_e.swControlOptions_SmallGapAbove for the Options parameter, the gap created between a new control and the previous control is smaller than the typical gap. Also, the control is hidden unless you specify swAddControlOptions_e.swControlOptions_Visible for the Options parameter. In the previous versions of this method, IPropertyManagerPageGroup::AddControl and IPropertyManagerGroup::IAddControl, the control was visible regardless if the Options parameter was set or not set to swAddControlOptions_e.swControlOptions_Visible.

## See Also

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.html)
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.html)

## Availability

SOLIDWORKS 2014 SP1, Revision Number 22.1
