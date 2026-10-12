---
title: "Checked Property (IPropertyManagerPageBitmapButton)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageBitmapButton"
member: "Checked"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~Checked.html"
---

# Checked Property (IPropertyManagerPageBitmapButton)

Gets or sets the state of the bitmap button.

## Syntax

### Visual Basic (Declaration)

```vb
Property Checked As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageBitmapButton
Dim value As System.Boolean

instance.Checked = value

value = instance.Checked
```

### C#

```csharp
System.bool Checked {get; set;}
```

### C++/CLI

```cpp
property System.bool Checked {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if bitmap button is clicked, false if not

## VBA Syntax

See [PropertyManagerPageBitmapButton::Checked](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageBitmapButton~Checked.html).

## Remarks

This property is only meaningful and used by the SOLIDWORKS Design application when the bitmap button control is of type swControlType_CheckableBitmapButton.

You can create a bitmap button control using either of these methods:

- [IPropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) or [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html)
- [IPropertyManagerPageGroup::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~AddControl.html) or [IPropertyManagerPageGroup::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~IAddControl.html)

## See Also

[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.html)
[IPropertyManagerPageBitmapButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.html)
[IPropertyManagerPageBitmapButton::IsCheckable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~IsCheckable.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
