---
title: "Italic Property (IPropertyManagerPageLabel)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageLabel"
member: "Italic"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Italic.html"
---

# Italic Property (IPropertyManagerPageLabel)

Gets or sets whether to italicize the specified range of characters in this PropertyManager label.

## Syntax

### Visual Basic (Declaration)

```vb
Property Italic( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Boolean

instance.Italic(StartChar, EndChar) = value

value = instance.Italic(StartChar, EndChar)
```

### C#

```csharp
System.bool Italic(
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

### C++/CLI

```cpp
property System.bool Italic {
   System.bool get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartChar`: 0-based index value of start character
- `EndChar`: 0-based index value of end character

### Property Value

True to italicize the specified range of characters, false to not

## VBA Syntax

See [PropertyManagerPageLabel::Italic](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageLabel~Italic.html).

## See Also

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
