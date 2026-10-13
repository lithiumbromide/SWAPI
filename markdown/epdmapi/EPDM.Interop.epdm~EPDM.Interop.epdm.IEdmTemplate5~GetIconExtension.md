---
title: "GetIconExtension Method (IEdmTemplate5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTemplate5"
member: "GetIconExtension"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5~GetIconExtension.html"
---

# GetIconExtension Method (IEdmTemplate5)

Gets the file extension for the icon registered with this template.

## Syntax

### Visual Basic

```vb
Function GetIconExtension() As System.String
```

### C#

```csharp
System.string GetIconExtension()
```

### C++/CLI

```cpp
System.String^ GetIconExtension();
```

### Return Value

File extension of the icon registered with this template

## Remarks

Templates are listed with a menu string and, optionally, an icon in SOLIDWORKS PDM Professional's menus and list controls. The file extension retrieved maps to the registered icon for the Windows file type of this template.

C++ programmers not using bstr_t wrapper functions must free the returned string with a call to SysFreeString.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTemplate5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5.html)
[IEdmTemplate5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
