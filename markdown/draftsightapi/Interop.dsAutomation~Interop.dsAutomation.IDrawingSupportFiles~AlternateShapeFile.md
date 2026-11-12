---
title: "AlternateShapeFile Property (IDrawingSupportFiles)"
project: ""
interface: "IDrawingSupportFiles"
member: "AlternateShapeFile"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateShapeFile.html"
---

# AlternateShapeFile Property (IDrawingSupportFiles)

Gets or sets the file name of the alternate compiled [shape](Interop.dsAutomation~Interop.dsAutomation.IShape.html) file when the current font is not available.

## Syntax

### Visual Basic

```vb
Property AlternateShapeFile As System.String
```

### C#

```csharp
System.string AlternateShapeFile {get; set;}
```

### JScript

```
function get,set AlternateShapeFile : System.String
```

### Managed Extensions for C++

```
__property System.string* get_AlternateShapeFile();
__property void set_AlternateShapeFile(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ AlternateShapeFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

File name of the alternate compiled shape file when the current font is not available (see **Remarks**)

## Examples

See the [IDrawingSupportFiles](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles.html) examples.

## Remarks

The filename extension of a compiled shape file is **.shx**.

## See Also

[IDrawingSupportFiles Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles.html)
[IDrawingSupportFiles Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles_members.html)
[IShapeManager::Load](Interop.dsAutomation~Interop.dsAutomation.IShapeManager~Load.html)
[IDrawingSupportFiles::AlternateBigFontFile Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateBigFontFile.html)
[IDrawingSupportFiles::AlternateShxFontFile Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~AlternateShxFontFile.html)

## Availability

DraftSight V1R5.0
