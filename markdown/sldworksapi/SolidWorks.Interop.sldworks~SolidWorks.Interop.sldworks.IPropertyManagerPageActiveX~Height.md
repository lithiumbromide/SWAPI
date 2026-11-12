---
title: "Height Property (IPropertyManagerPageActiveX)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageActiveX"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX~Height.html"
---

# Height Property (IPropertyManagerPageActiveX)

Gets or sets the height of this ActiveX control.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageActiveX
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

Height of the control

## VBA Syntax

See [PropertyManagerPageActiveX::Height](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageActiveX~Height.html).

## Remarks

This property only applies to some ActiveX controls. If the height does not apply to an ActiveX control, then this property does not affect the API PropertyManager page.

The height is in dialog-box units. You can convert these values to screen units (pixels) by using the MapDialogRect function.

## See Also

[IPropertyManagerPageActiveX Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX.html)
[IPropertyManagerPageActiveX Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
