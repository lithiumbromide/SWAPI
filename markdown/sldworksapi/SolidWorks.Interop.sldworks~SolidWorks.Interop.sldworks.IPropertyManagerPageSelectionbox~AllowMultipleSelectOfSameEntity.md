---
title: "AllowMultipleSelectOfSameEntity Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "AllowMultipleSelectOfSameEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~AllowMultipleSelectOfSameEntity.html"
---

# AllowMultipleSelectOfSameEntity Property (IPropertyManagerPageSelectionbox)

Gets or sets whether the same entity can be selected multiple times in this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllowMultipleSelectOfSameEntity As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Boolean

instance.AllowMultipleSelectOfSameEntity = value

value = instance.AllowMultipleSelectOfSameEntity
```

### C#

```csharp
System.bool AllowMultipleSelectOfSameEntity {get; set;}
```

### C++/CLI

```cpp
property System.bool AllowMultipleSelectOfSameEntity {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the same entity can be selected multiple times in this selection box, false if not

## VBA Syntax

See [PropertyManagerPageSelectionbox::AllowMultipleSelectOfSameEntity](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~AllowMultipleSelectOfSameEntity.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
