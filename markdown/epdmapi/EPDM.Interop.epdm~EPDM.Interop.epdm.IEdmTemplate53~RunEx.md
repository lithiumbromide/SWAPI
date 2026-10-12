---
title: "RunEx Method (IEdmTemplate53)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTemplate53"
member: "RunEx"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate53~RunEx.html"
---

# RunEx Method (IEdmTemplate53)

Executes this template in the specified folder.

## Syntax

### Visual Basic

```vb
Function RunEx( _
   ByVal hParentWnd As System.Integer, _
   ByVal lCurrentFolderID As System.Integer, _
   ByRef ppoRetData() As System.Object _
) As System.Integer
```

### C#

```csharp
System.int RunEx(
   System.int hParentWnd,
   System.int lCurrentFolderID,
   out System.object[] ppoRetData
)
```

### C++/CLI

```cpp
System.int RunEx(
   System.int hParentWnd,
   System.int lCurrentFolderID,
   [Out] System.array<Object^>^ ppoRetData
)
```

### Parameters

- `hParentWnd`: Parent window handle
- `lCurrentFolderID`: ID of the folder in which to execute this template
- `ppoRetData`: Array of [IEdmData](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData.html) interfaces; one interface for each object created by this template

### Return Value

User-interface refresh flags as defined in [EdmRefleshFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefreshFlag.html)

## Examples

See the [IEdmTemplate53](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate53.html) examples.

## Remarks

This method executes this template like [IEdmTemplate5::Run](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5~Run.html) does, but it also returns information about all of the files, folders, and variables created by this template.

If your application needs to be backward compatible with SOLIDWORKS PDM Professional 5.2, use IEdmTemplate5::Run instead of this method.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTemplate53 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate53.html)
[IEdmTemplate53 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate53_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.3
