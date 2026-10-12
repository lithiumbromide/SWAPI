---
title: "Mark Property (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "Mark"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Mark.html"
---

# Mark Property (IPropertyManagerPageSelectionbox)

Gets or sets the mark used on selected items in this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Mark As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer

instance.Mark = value

value = instance.Mark
```

### C#

```csharp
System.int Mark {get; set;}
```

### C++/CLI

```cpp
property System.int Mark {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number to use as a mark; this number is used by methods or properties that require ordered entity selection

## VBA Syntax

See [PropertyManagerPageSelectionbox::Mark](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~Mark.html).

## Examples

[Select Multiple Objects for Selection Boxes (C#)](Select_Multiple_Objects_for_Selection_Boxes_Example_CSharp.htm)
[Select Multiple Objects for Selection Boxes (VB.NET)](Select_Multiple_Objects_for_Selection_Boxes_Example_VBNET.htm)
[Select Multiple Objects for Selection Boxes (VBA)](Select_Multiple_Objects_for_Selection_Boxes_Example_VB.htm)

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

It is easiest to use the Mark property as a read-only property. If this property is not set before the PropertyManager is shown, then the Mark value is automatically set. Once the PropertyManager page is displayed, then the application can query the Mark for its value.

If the application must rely on specific mark values for specific selection boxes, then the set the Mark value before the PropertyManager page is shown. In this case, ensure that each selection box contains a different value. Otherwise, the user's selection is displayed in the selection boxes that have the same Mark value.

Mark values (whether set by the SOLIDWORKS Design application or by your application) must be powers of two (for example, 1, 2, 4, 8).

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
