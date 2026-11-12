---
title: "AlternateBigFontFile Property (IDrawingSupportFiles)"
project: ""
interface: "IDrawingSupportFiles"
member: "AlternateBigFontFile"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateBigFontFile.html"
---

# AlternateBigFontFile Property (IDrawingSupportFiles)

Gets or sets the file name of the alternate big font file when the current font is not available.

## Syntax

### Visual Basic

```vb
Property AlternateBigFontFile As System.String
```

### C#

```csharp
System.string AlternateBigFontFile {get; set;}
```

### JScript

```
function get,set AlternateBigFontFile : System.String
```

### Managed Extensions for C++

```
__property System.string* get_AlternateBigFontFile();
__property void set_AlternateBigFontFile(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ AlternateBigFontFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

File name of the alternate big font file when the current font is not available (see **Remarks**)

## Examples

See the [IDrawingSupportFiles](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles.html) examples.

## Remarks

The filename extension of an alternate big font file is **.shx**, and the file is a compiled [shape](Interop.dsAutomation~Interop.dsAutomation.IShape.html) font file.

## See Also

[IDrawingSupportFiles Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles.html)
[IDrawingSupportFiles Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles_members.html)
[ITextStyle::BigFont Property ()](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~BigFont.html)
[IDrawingSupportFiles::AlternateShapeFile Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateShapeFile.html)
[IDrawingSupportFiles::AlternateShxFontFile Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateShxFontFile.html)

## Availability

DraftSight V1R5.0
