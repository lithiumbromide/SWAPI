---
title: "Caption Property (IPropertyManagerPageCheckbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCheckbox"
member: "Caption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox~Caption.html"
---

# Caption Property (IPropertyManagerPageCheckbox)

Gets or sets the label for this check box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Caption As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageCheckbox
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

Check box label

## VBA Syntax

See [PropertyManagerPageCheckbox::Caption](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageCheckbox~Caption.html).

## See Also

[IPropertyManagerPageCheckbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox.html)
[IPropertyManagerPageCheckbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
