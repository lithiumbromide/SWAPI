---
title: "Tip Property (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "Tip"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Tip.html"
---

# Tip Property (IPropertyManagerPageControl)

Gets or sets the ToolTip for this control on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property Tip As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim value As System.String

instance.Tip = value

value = instance.Tip
```

### C#

```csharp
System.string Tip {get; set;}
```

### C++/CLI

```cpp
property System.String^ Tip {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

ToolTip text

## VBA Syntax

See [PropertyManagerPageControl::Tip](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~Tip.html).

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
