---
title: "GetMenuString Method (IEdmTemplate5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTemplate5"
member: "GetMenuString"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5~GetMenuString.html"
---

# GetMenuString Method (IEdmTemplate5)

Gets the string displayed in the SOLIDWORKS PDM Professional menu for this template.

## Syntax

### Visual Basic

```vb
Function GetMenuString() As System.String
```

### C#

```csharp
System.string GetMenuString()
```

### C++/CLI

```cpp
System.String^ GetMenuString();
```

### Return Value

Menu string

## Examples

[Execute Template (C#)](Execute_Template_Example_CSharp.htm)
[Execute Template (VB.NET)](Execute_Template_Example_VBNET.htm)

## Remarks

C++ programmers not using bstr_t wrapper functions must free the returned string with a call to SysFreeString.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTemplate5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5.html)
[IEdmTemplate5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
