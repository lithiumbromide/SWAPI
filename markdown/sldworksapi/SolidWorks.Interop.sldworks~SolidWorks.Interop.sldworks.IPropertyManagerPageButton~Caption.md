---
title: "Caption Property (IPropertyManagerPageButton)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageButton"
member: "Caption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton~Caption.html"
---

# Caption Property (IPropertyManagerPageButton)

Gets or sets the caption for this button.

## Syntax

### Visual Basic (Declaration)

```vb
Property Caption As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageButton
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

Button text

## VBA Syntax

See [PropertyManagerPageButton::Caption](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageButton~Caption.html).

## See Also

[IPropertyManagerPageButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton.html)
[IPropertyManagerPageButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
