---
title: "AlternateShxFontFile Property (IDrawingSupportFiles)"
project: ""
interface: "IDrawingSupportFiles"
member: "AlternateShxFontFile"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateShxFontFile.html"
---

# AlternateShxFontFile Property (IDrawingSupportFiles)

Gets or sets the file name of the alternate SHX font file when the current font is not available.

## Syntax

### Visual Basic

```vb
Property AlternateShxFontFile As System.String
```

### C#

```csharp
System.string AlternateShxFontFile {get; set;}
```

### JScript

```
function get,set AlternateShxFontFile : System.String
```

### Managed Extensions for C++

```
__property System.string* get_AlternateShxFontFile();
__property void set_AlternateShxFontFile(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ AlternateShxFontFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

File name of the alternate SHX font file when the current font is not available

## Examples

See the [IDrawingSupportFiles](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles.html) examples.

## Remarks

The filename extension of an alternate SHX font file is **.shx**, and the file is a compiled [shape](Interop.dsAutomation~Interop.dsAutomation.IShape.html) SHX font file.

## See Also

[IDrawingSupportFiles Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles.html)
[IDrawingSupportFiles Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles_members.html)
[IDrawingSupportFiles::AlternateShapeFile Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateShapeFile.html)
[IDrawingSupportFiles::AlternateBigFontFile Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateBigFontFile.html)

## Availability

DraftSight V1R5.0
