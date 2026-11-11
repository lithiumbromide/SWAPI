---
title: "GetDrawingSupportFiles Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetDrawingSupportFiles"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetDrawingSupportFiles.html"
---

# GetDrawingSupportFiles Method (IApplication)

Gets access to the DraftSight options that get and set default paths and file names for these drawing-support files: alternate font, drawing, drawing template, external references, font mapping, library, LineStyle, and RichLineStyle.

## Syntax

### Visual Basic

```vb
Function GetDrawingSupportFiles() As DrawingSupportFiles
```

### C#

```csharp
DrawingSupportFiles GetDrawingSupportFiles()
```

### JScript

```
function GetDrawingSupportFiles() : DrawingSupportFiles;
```

### Managed Extensions for C++

```
DrawingSupportFiles* GetDrawingSupportFiles();
```

### C++/CLI

```cpp
DrawingSupportFiles^ GetDrawingSupportFiles();
```

### Return Value

[IDrawingSupportFiles](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles.html)

## Examples

[Set Alternate Drawing Support Files (C#)](Set_Alternate_Drawing_Support_Files_Example_CSharp.htm)
[Set Alternate Drawing Support Files (VB.NET)](Set_Alternate_Drawing_Support_Files_Example_VBNET.htm)
[Set Alternate Drawing Support Files (VBA)](Set_Alternate_Drawing_Support_Files_Example_VBA.htm)

## Remarks

The IDrawingSupportFiles interface corresponds to clicking **Tools > Options > File Locations > Drawing Support** in the user interface.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R5.0
