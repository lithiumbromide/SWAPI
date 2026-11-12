---
title: "BigFont Property (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "BigFont"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~BigFont.html"
---

# BigFont Property (ITextStyle)

Gets or sets the file name of the big font for the TextStyle.

## Syntax

### Visual Basic

```vb
Property BigFont As System.String
```

### C#

```csharp
System.string BigFont {get; set;}
```

### JScript

```
function get,set BigFont : System.String
```

### Managed Extensions for C++

```
__property System.string* get_BigFont();
__property void set_BigFont(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ BigFont {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

File name of big font (see **Remarks**)

## Remarks

The filename extension of a big font file is **.shx**, and the file is a compiled [shape](Interop.dsAutomation~Interop.dsAutomation.IShape.html) font file.

## See Also

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)
[IDrawingSupportFiles::AlternateBigFontFile Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateBigFontFile.html)
[ITextStyle::Font Property](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~Font.html)

## Availability

DraftSight V1R1.1
