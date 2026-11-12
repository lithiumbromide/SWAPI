---
title: "Height Property (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~Height.html"
---

# Height Property (IPropertyManagerPageNumberbox)

Gets or sets the maximum height of the attached drop-down list for this number box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
Dim value As System.Short

instance.Height = value

value = instance.Height
```

### C#

```csharp
System.short Height {get; set;}
```

### C++/CLI

```cpp
property System.short Height {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum height of attached drop-down list

## VBA Syntax

See [PropertyManagerPageNumberbox::Height](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageNumberbox~Height.html).

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
