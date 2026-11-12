---
title: "Caption Property (IPropertyManagerPageGroup)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageGroup"
member: "Caption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~Caption.html"
---

# Caption Property (IPropertyManagerPageGroup)

Gets or sets the title for this group box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Caption As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageGroup
Dim value As System.String

instance.Caption = value

value = instance.Caption
```

### C#

```csharp
System.string Caption {get; set;}
```

### C++/CLI

```cpp
property System.String^ Caption {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for the title for this group box

## VBA Syntax

See [PropertyManagerPageGroup::Caption](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageGroup~Caption.html).

## Remarks

See [IPropertyManagerPage2::AddGroupBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.html) or [IPropertyManagerPage2::IAddGroupBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.html) to add a group box.

## See Also

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.html)
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13.2
