---
title: "GetObjects Method (IEdmVault9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault9"
member: "GetObjects"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault9~GetObjects.html"
---

# GetObjects Method (IEdmVault9)

Gets interfaces to all of the specified objects.

## Syntax

### Visual Basic

```vb
Sub GetObjects( _
   ByRef ppoObjects As EdmObjectInfo() _
)
```

### C#

```csharp
void GetObjects(
   out EdmObjectInfo[] ppoObjects
)
```

### C++/CLI

```cpp
void GetObjects(
   [Out] array<EdmObjectInfo> ppoObjects
)
```

### Parameters

- `ppoObjects`: Array of [EdmObjectInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectInfo.html) structures; one structure for each interface to retrieve

## Examples

[Batch Update Card Variables (C#)](Batch_Update_Variables_Example_CSharp.htm)
[Batch Update Card Variables (VB.NET)](Batch_Update_Variables_Example_VBNET.htm)

## Remarks

Call this method to get interfaces to several objects at once, which is more efficient than calling [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) multiple times.

## See Also

[IEdmVault9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault9.html)
[IEdmVault9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault9_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
