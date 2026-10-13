---
title: "SilentMode Property (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "SilentMode"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~SilentMode.html"
---

# SilentMode Property (IEdmVault5)

Gets whether the add-in is running in silent mode.

## Syntax

### Visual Basic

```vb
ReadOnly Property SilentMode As System.Boolean
```

### C#

```csharp
System.bool SilentMode {get;}
```

### C++/CLI

```cpp
property System.bool SilentMode {
   System.bool get();
}
```

### Property Value

True if in silent mode, false if dialog boxes are displayed

## Remarks

This property always returns true on SOLIDWORKS PDM Professional's Web Server. When in silent mode, add-ins may not display a user interface, because that blocks the server.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
