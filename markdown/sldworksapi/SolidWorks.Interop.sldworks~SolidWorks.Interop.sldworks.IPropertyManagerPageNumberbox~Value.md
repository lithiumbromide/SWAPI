---
title: "Value Property (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "Value"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~Value.html"
---

# Value Property (IPropertyManagerPageNumberbox)

Gets and sets the value that appears in the number box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Value As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
Dim value As System.Double

instance.Value = value

value = instance.Value
```

### C#

```csharp
System.double Value {get; set;}
```

### C++/CLI

```cpp
property System.double Value {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value in number box

## VBA Syntax

See [PropertyManagerPageNumberbox::Value](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageNumberbox~Value.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)
[IPropertyManagerPageNumberbox::DisplayedUnit Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~DisplayedUnit.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
