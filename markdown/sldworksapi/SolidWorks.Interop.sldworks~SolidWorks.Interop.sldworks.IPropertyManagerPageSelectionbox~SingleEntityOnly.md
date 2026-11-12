---
title: "SingleEntityOnly Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "SingleEntityOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SingleEntityOnly.html"
---

# SingleEntityOnly Property (IPropertyManagerPageSelectionbox)

Gets or sets whether this selection box is for single or multiple items.

## Syntax

### Visual Basic (Declaration)

```vb
Property SingleEntityOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Boolean

instance.SingleEntityOnly = value

value = instance.SingleEntityOnly
```

### C#

```csharp
System.bool SingleEntityOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool SingleEntityOnly {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the selection box is for a single item, false for multiple items

## VBA Syntax

See [PropertyManagerPageSelectionbox::SingleEntityOnly](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~SingleEntityOnly.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
