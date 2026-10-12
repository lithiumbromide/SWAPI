---
title: "AddGroupBox Method (IPropertyManagerPageTab)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageTab"
member: "AddGroupBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~AddGroupBox.html"
---

# AddGroupBox Method (IPropertyManagerPageTab)

Adds a group box to this tab on a PropertyManager page.

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
Dim instance As IPropertyManagerPageTab
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

Newly created [PropertyManager Page group box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup.html)

## VBA Syntax

See [PropertyManagerPageTab::AddGroupBox](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageTab~AddGroupBox.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

To change the title of an existing group box, use [IPropertyManagerPageTab::Caption](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageTab~Caption.html).

## See Also

[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.html)
[IPropertyManagerPageTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab_members.html)
[IPropertyManagerPageTab::IAddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~IAddGroupBox.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
