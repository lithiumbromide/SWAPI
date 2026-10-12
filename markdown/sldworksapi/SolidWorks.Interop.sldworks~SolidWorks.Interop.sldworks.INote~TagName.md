---
title: "TagName Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "TagName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TagName.html"
---

# TagName Property (INote)

Gets or sets the tag name for this note.

## Syntax

### Visual Basic (Declaration)

```vb
Property TagName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.String

instance.TagName = value

value = instance.TagName
```

### C#

```csharp
System.string TagName {get; set;}
```

### C++/CLI

```cpp
property System.String^ TagName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tag name

## VBA Syntax

See [Note::TagName](ms-its:sldworksapivb6.chm::/sldworks~Note~TagName.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)
[Remove Hyperlink From Note in Drawing (VBA)](Remove_Hyperlink_from_Note_in_Drawing_Example_VB.htm)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
