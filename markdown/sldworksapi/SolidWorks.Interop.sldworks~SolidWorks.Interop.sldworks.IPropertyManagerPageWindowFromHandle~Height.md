---
title: "Height Property (IPropertyManagerPageWindowFromHandle)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageWindowFromHandle"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle~Height.html"
---

# Height Property (IPropertyManagerPageWindowFromHandle)

Gets or sets the height of this .NET control.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageWindowFromHandle
Dim value As System.Integer

instance.Height = value

value = instance.Height
```

### C#

```csharp
System.int Height {get; set;}
```

### C++/CLI

```cpp
property System.int Height {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height of the control

## VBA Syntax

See [PropertyManagerPageWindowFromHandle::Height](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageWindowFromHandle~Height.html).

## Examples

See the [IPropertyManagerPageWindowFromHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html) examples.

## Remarks

This property only applies to some .NET controls.

The height is in dialog-box units. You can convert these values to screen units (pixels) by using the Windows MapDialogRect function.

## See Also

[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html)
[IPropertyManagerPageWindowFromHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
