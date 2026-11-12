---
title: "CharacterColor Property (IPropertyManagerPageLabel)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageLabel"
member: "CharacterColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~CharacterColor.html"
---

# CharacterColor Property (IPropertyManagerPageLabel)

Gets or sets the color of the specified characters in this PropertyManager label.

## Syntax

### Visual Basic (Declaration)

```vb
Property CharacterColor( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Integer

instance.CharacterColor(StartChar, EndChar) = value

value = instance.CharacterColor(StartChar, EndChar)
```

### C#

```csharp
System.int CharacterColor(
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

### C++/CLI

```cpp
property System.int CharacterColor {
   System.int get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartChar`: 0-based index value of start character
- `EndChar`: 0-based index value of end character

### Property Value

RGB value for the text color for the specified characters; if not specified, then the system default setting for text color is used

## VBA Syntax

See [PropertyManagerPageLabel::CharacterColor](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageLabel~CharacterColor.html).

## See Also

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
