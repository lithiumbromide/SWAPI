---
title: "Text Property (IComment)"
project: "SOLIDWORKS API Help"
interface: "IComment"
member: "Text"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Text.html"
---

# Text Property (IComment)

Gets or sets the text for the comment.

## Syntax

### Visual Basic (Declaration)

```vb
Property Text As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComment
Dim value As System.String

instance.Text = value

value = instance.Text
```

### C#

```csharp
System.string Text {get; set;}
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for the comment

## VBA Syntax

See [Comment::Text](ms-its:sldworksapivb6.chm::/sldworks~Comment~Text.html).

## Examples

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

## See Also

[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.html)
[IComment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
