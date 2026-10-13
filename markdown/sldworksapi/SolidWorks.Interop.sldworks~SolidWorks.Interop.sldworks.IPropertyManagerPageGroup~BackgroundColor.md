---
title: "BackgroundColor Property (IPropertyManagerPageGroup)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageGroup"
member: "BackgroundColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~BackgroundColor.html"
---

# BackgroundColor Property (IPropertyManagerPageGroup)

Gets or sets the background color of this PropertyManager group box.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageGroup
Dim value As System.Integer

instance.BackgroundColor = value

value = instance.BackgroundColor
```

### C#

```csharp
System.int BackgroundColor {get; set;}
```

### C++/CLI

```cpp
property System.int BackgroundColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

COLORREF value

## VBA Syntax

See [PropertyManagerPageGroup::BackgroundColor](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageGroup~BackgroundColor.html).

## Remarks

You can use a group box with just a [label](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageLabel.html) to look like a [message box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~SetMessage3.html) on a PropertyManager page. Set the background of the group box and the [background of the label](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageControl~BackgroundColor.html) to the same color and the [label text](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageLabel~CharacterColor.html) to a different color. You can also position the group box anywhere on the PropertyManager page.

NOTE: If you want to set the background color of the message box to be the same as the color typically used by SOLIDWORKS for a message box, use [ISldWorks::GetUserPreferenceIntegerValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceIntegerValue.html) swPropertyManagerColorImportantMessage to get the COLORREF value.

## See Also

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.html)
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
