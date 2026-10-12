---
title: "IAddGroupBox Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "IAddGroupBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.html"
---

# IAddGroupBox Method (IPropertyManagerPage2)

Adds a group box to a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddGroupBox( _
   ByVal ID As System.Integer, _
   ByVal Caption As System.String, _
   ByVal Options As System.Integer _
) As PropertyManagerPageGroup
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim Caption As System.String
Dim Options As System.Integer
Dim value As PropertyManagerPageGroup

value = instance.IAddGroupBox(ID, Caption, Options)
```

### C#

```csharp
PropertyManagerPageGroup IAddGroupBox(
   System.int ID,
   System.string Caption,
   System.int Options
)
```

### C++/CLI

```cpp
PropertyManagerPageGroup^ IAddGroupBox(
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

See [PropertyManagerPage2::IAddGroupBox](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~IAddGroupBox.html).

## Remarks

Use this method to set properties on the PropertyManager page before the page is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [PropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html) for details.

To change the title of an existing group box, use [IPropertyManagerPageGroup::Caption](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~Caption.html).

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[IPropertyManagerPage2::AddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
