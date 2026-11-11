---
title: "FontMappingFile Property (IDrawingSupportFiles)"
project: ""
interface: "IDrawingSupportFiles"
member: "FontMappingFile"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~FontMappingFile.html"
---

# FontMappingFile Property (IDrawingSupportFiles)

Gets or sets the path and file name of the font mapping file when the current font file is not available.

## Syntax

### Visual Basic

```vb
Property FontMappingFile As System.String
```

### C#

```csharp
System.string FontMappingFile {get; set;}
```

### JScript

```
function get,set FontMappingFile : System.String
```

### Managed Extensions for C++

```
__property System.string* get_FontMappingFile();
__property void set_FontMappingFile(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ FontMappingFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Path and file name of the font mapping file when the current font file is not available

## Remarks

DraftSight uses the path and file name specified by this property when a font file referenced in a [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html) is not available.

## See Also

[IDrawingSupportFiles Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles.html)
[IDrawingSupportFiles Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles_members.html)

## Availability

DraftSight V1R5.0
