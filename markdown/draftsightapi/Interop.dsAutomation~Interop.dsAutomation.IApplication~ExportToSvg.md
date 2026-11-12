---
title: "ExportToSvg Method (IApplication)"
project: ""
interface: "IApplication"
member: "ExportToSvg"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~ExportToSvg.html"
---

# ExportToSvg Method (IApplication)

Obsolete. Superseded by [IApplication::ExportToSvg2](Interop.dsAutomation~Interop.dsAutomation.IApplication~ExportToSvg2.html).

## Syntax

### Visual Basic

```vb
Sub ExportToSvg( _
   ByVal DrawingFilePath As System.String, _
   ByVal SvgFilePath As System.String, _
   ByRef Success As System.Boolean _
)
```

### C#

```csharp
void ExportToSvg(
   System.string DrawingFilePath,
   System.string SvgFilePath,
   out System.bool Success
)
```

### JScript

```
function ExportToSvg(
   DrawingFilePath : System.String,
   SvgFilePath : System.String,
   Success : System.boolean
);
```

### Managed Extensions for C++

```
void ExportToSvg(
   System.string* DrawingFilePath,
   System.string* SvgFilePath,
   [PARAMFLAG::Out] System.bool Success
)
```

### C++/CLI

```cpp
void ExportToSvg(
   System.String^ DrawingFilePath,
   System.String^ SvgFilePath,
   [Out] System.bool Success
)
```

### Parameters

- `DrawingFilePath`: Full path name of drawing file
- `SvgFilePath`: Full path name of SVG file
- `Success`: True if successful, false if not

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight 2020 SP1
