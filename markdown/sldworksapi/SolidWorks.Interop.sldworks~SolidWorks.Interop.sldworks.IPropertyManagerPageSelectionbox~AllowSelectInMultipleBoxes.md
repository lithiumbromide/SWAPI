---
title: "AllowSelectInMultipleBoxes Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "AllowSelectInMultipleBoxes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~AllowSelectInMultipleBoxes.html"
---

# AllowSelectInMultipleBoxes Property (IPropertyManagerPageSelectionbox)

Gets or sets whether an entity can be selected in this selection box if the entity is selected elsewhere.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllowSelectInMultipleBoxes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Boolean

instance.AllowSelectInMultipleBoxes = value

value = instance.AllowSelectInMultipleBoxes
```

### C#

```csharp
System.bool AllowSelectInMultipleBoxes {get; set;}
```

### C++/CLI

```cpp
property System.bool AllowSelectInMultipleBoxes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

| If... | Then... |
| --- | --- |
| true | When an entity is selected while this selection box is active and that entity is selected in a different selection box, then the entity is added to this selection box. If the entity is already selected in this selection box, then the entity is removed from the selection box. |
| false | When an entity is selected while this selection box is active and that entity is already selected, then the entity is removed from the selection box. This is the default behavior of a selection box. |

## VBA Syntax

See [PropertyManagerPageSelectionbox::AllowSelectInMultipleBoxes](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~AllowSelectInMultipleBoxes.html).

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
