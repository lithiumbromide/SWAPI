---
title: "Caption Property (IPropertyManagerPageLabel)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageLabel"
member: "Caption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Caption.html"
---

# Caption Property (IPropertyManagerPageLabel)

Gets or sets the caption for this label.

## Syntax

### Visual Basic (Declaration)

```vb
Property Caption As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageLabel
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

Caption text

## VBA Syntax

See [PropertyManagerPageLabel::Caption](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageLabel~Caption.html).

## See Also

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
