---
title: "GetWin32Window Method (IEdmVault8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault8"
member: "GetWin32Window"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8~GetWin32Window.html"
---

# GetWin32Window Method (IEdmVault8)

Converts the specified window handle to an Win32Window interface that can be used in the .NET Framework.

## Syntax

### Visual Basic

```vb
Function GetWin32Window( _
   ByVal lHwnd As System.Integer _
) As System.Object
```

### C#

```csharp
System.object GetWin32Window(
   System.int lHwnd
)
```

### C++/CLI

```cpp
System.Object^ GetWin32Window(
   System.int lHwnd
)
```

### Parameters

- `lHwnd`: Window handle to convert

### Return Value

IWin32Window interface

## Examples

[Creating Add-ins (VB.NET)](DotNetAddIns.htm)

## See Also

[IEdmVault8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8.html)
[IEdmVault8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
