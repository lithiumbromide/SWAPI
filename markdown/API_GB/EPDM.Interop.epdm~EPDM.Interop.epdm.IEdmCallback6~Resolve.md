---
title: "Resolve Method (IEdmCallback6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback6"
member: "Resolve"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6~Resolve.html"
---

# Resolve Method (IEdmCallback6)

Resolves multiple errors.

## Syntax

### Visual Basic

```vb
Sub Resolve( _
   ByVal lParentWnd As System.Integer, _
   ByRef ppoItems As EdmCmdData() _
)
```

### C#

```csharp
void Resolve(
   System.int lParentWnd,
   out EdmCmdData[] ppoItems
)
```

### C++/CLI

```cpp
void Resolve(
   System.int lParentWnd,
   [Out] array<EdmCmdData> ppoItems
)
```

### Parameters

- `lParentWnd`: Handle of the parent window
- `ppoItems`: Array of [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html) structures; one structure for each item that needs to be resolved (see **Remarks**)

## Examples

See the [IEdmCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6.html) examples.

## Remarks

SOLIDWORKS PDM Professional continues to call this method until all errors are resolved or until this method returns an error code. If you do not properly implement this method to return an error code, you may cause your program to hang.

Contents of each ppoItem EdmCmdData structure:

| Member | Direction | Contents |
| --- | --- | --- |
| mlObjectID1 | Input | ID of the source file that is being copied; 0 if the file is copied from outside the vault |
| mlObjectID2 | Input | ID of the source file's parent folder; 0 if the file is copied from outside the vault |
| mbsStrData1 | Input | Path to the source file |
| mbsStrData2 | Input | Path to the destination file |
| mlLongData1 | Input | Combination of EdmResolveReason bits telling why this method is called |
| mlLongData2 | Output | Combination of EdmResolveAction bits telling SOLIDWORKS PDM Professional how to proceed |

The ppoItems array may contain items that do not need to be resolved. The mlLongData1 struct members for those items are zero.

## See Also

[IEdmCallback6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6.html)
[IEdmCallback6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
