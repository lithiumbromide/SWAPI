---
title: "ExportToSvg2 Method (IApplication)"
project: ""
interface: "IApplication"
member: "ExportToSvg2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~ExportToSvg2.html"
---

# ExportToSvg2 Method (IApplication)

Exports the specified drawing file to the specified SVG file.

## Syntax

### Visual Basic

```vb
Sub ExportToSvg2( _
   ByVal DrawingFilePath As System.String, _
   ByVal SvgFilePath As System.String, _
   ByVal GrayScale As System.Boolean, _
   ByRef Success As System.Boolean _
)
```

### C#

```csharp
void ExportToSvg2(
   System.string DrawingFilePath,
   System.string SvgFilePath,
   System.bool GrayScale,
   out System.bool Success
)
```

### JScript

```
function ExportToSvg2(
   DrawingFilePath : System.String,
   SvgFilePath : System.String,
   GrayScale : System.boolean,
   Success : System.boolean
);
```

### Managed Extensions for C++

```
void ExportToSvg2(
   System.string* DrawingFilePath,
   System.string* SvgFilePath,
   System.bool GrayScale,
   [PARAMFLAG::Out] System.bool Success
)
```

### C++/CLI

```cpp
void ExportToSvg2(
   System.String^ DrawingFilePath,
   System.String^ SvgFilePath,
   System.bool GrayScale,
   [Out] System.bool Success
)
```

### Parameters

- `DrawingFilePath`: Full path name of drawing file
- `SvgFilePath`: Full path name of SVG file
- `GrayScale`: True to export grayscale, false to export color
- `Success`: True if successful, false if not

## Examples

`'VBA`

`Option Explicit`

`Sub main()`

`Dim dsApp As DraftSight.Application`

`'Connect to DraftSight`

`Set dsApp = GetObject(, "DraftSight.Application")`

`'Abort any command currently running in DraftSight`

`'to avoid nested commands`

`dsApp.AbortRunningCommand`

`Dim DrawingFilePath As String`

`DrawingFilePath = "drawing_file_path"`

`Dim SvgFilePath As String`

`SvgFilePath = "svg_file_path"`

`Dim bSuccess As Boolean`

`dsApp.`**ExportToSvg2** `DrawingFilePath, SvgFilePath, True, bSuccess`

`If bSuccess = False Then`

`MsgBox "Failed to export " + DrawingFilePath + " document to SVG format."`

`End If`

`End Sub`

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight 2021 SP0
