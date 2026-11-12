---
title: "AddControl2 Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "AddControl2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl2.html"
---

# AddControl2 Method (IPropertyManagerPage2)

Adds a control to this PropertyManager page.

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
Dim instance As IPropertyManagerPage2
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

- `ID`: Resource ID of this control whose value is passed back to the add-in through the [IPropertyManagerPage2Handler9](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9.html) interface
- `ControlType`: Type of control as defined in [swPropertyManagerPageControlType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlType_e.html)
- `Caption`: Caption of this control
- `LeftAlign`: Left alignment of this control as defined in [swPropertyManagerPageControlLeftAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageControlLeftAlign_e.html)
- `Options`: Options as defined in [swAddControlOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddControlOptions_e.html) (see **Remarks**)
- `Tip`: ToolTip for this control

### Return Value

Newly created [PropertyManager page control](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageControl.html)

## VBA Syntax

See [PropertyManagerPage2::AddControl2](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~AddControl2.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Remarks

You can only use this method to set properties on the PropertyManager before the page is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

To follow the SOLIDWORKS standards when designing a new PropertyManager page, it is a good idea to use [IPropertyManagerPage2::AddGroupBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.html) or [IPropertyManagerPage2::IAddGroupBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.html) and [IPropertyManagerPageGroup::AddControl2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~AddControl2.html) to add controls for the page inside group boxes.

When you specify swAddControlOptions_e.swControlOptions_SmallGapAbove for the Options parameter, the gap created between the new control and the previous control is smaller than a typical gap. Also, the control is hidden unless you specify swAddControlOptions_e.swControlOptions_Visible for the Options parameter. In the previous versions of this method, IPropertyManagerPage2::AddControl and IPropertyManagerPage2::IAddControl, the control was visible regardless if the Options parameter was set or not set to swAddControlOptions_e.swControlOptions_Visible.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)

## Availability

SOLIDWORKS 2014 SP1, Revision Number 22.1
