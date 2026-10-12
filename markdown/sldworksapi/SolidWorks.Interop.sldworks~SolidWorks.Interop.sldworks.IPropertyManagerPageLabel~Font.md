---
title: "Font Property (IPropertyManagerPageLabel)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageLabel"
member: "Font"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Font.html"
---

# Font Property (IPropertyManagerPageLabel)

Gets or sets the font for the specified characters in this PropertyManager label.

## Syntax

### Visual Basic (Declaration)

```vb
Property Font( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.String

instance.Font(StartChar, EndChar) = value

value = instance.Font(StartChar, EndChar)
```

### C#

```csharp
System.string Font(
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ Font {
   System.String^ get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartChar`: 0-based index value of start character
- `EndChar`: 0-based index value of end character

### Property Value

Name of the font to use for the specified characters

## VBA Syntax

See [PropertyManagerPageLabel::Font](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageLabel~Font.html).

## See Also

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
