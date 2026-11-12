---
title: "AddGroupBox Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "AddGroupBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.html"
---

# AddGroupBox Method (IPropertyManagerPage2)

Adds a group box to a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddGroupBox( _
   ByVal ID As System.Integer, _
   ByVal Caption As System.String, _
   ByVal Options As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim Caption As System.String
Dim Options As System.Integer
Dim value As System.Object

value = instance.AddGroupBox(ID, Caption, Options)
```

### C#

```csharp
System.object AddGroupBox(
   System.int ID,
   System.string Caption,
   System.int Options
)
```

### C++/CLI

```cpp
System.Object^ AddGroupBox(
   System.int ID,
   System.String^ Caption,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Resource ID of the group box
- `Caption`: Title of the group box
- `Options`: Options as defined in [swAddGroupBoxOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddGroupBoxOptions_e.html)

### Return Value

Newly created [PropertyManager page group box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup.html)

## VBA Syntax

See [PropertyManagerPage2::AddGroupBox](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~AddGroupBox.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

Use this method to set properties on the PropertyManager page before the page is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [PropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html) for details.

To change the title of an existing group box, use [IPropertyManagerPageGroup::Caption](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~Caption.html).

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[IPropertyManagerPage2::IAddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
