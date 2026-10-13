---
title: "GetBitmapInfo Method (IEdmBitmap5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBitmap5"
member: "GetBitmapInfo"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5~GetBitmapInfo.html"
---

# GetBitmapInfo Method (IEdmBitmap5)

Gets bitmap information.

## Syntax

### Visual Basic

```vb
Sub GetBitmapInfo( _
   ByVal lDataSize As System.Integer, _
   ByRef pbData As System.Byte _
)
```

### C#

```csharp
void GetBitmapInfo(
   System.int lDataSize,
   out System.byte pbData
)
```

### C++/CLI

```cpp
void GetBitmapInfo(
   System.int lDataSize,
   [Out] System.byte pbData
)
```

### Parameters

- `lDataSize`: Size of pbData (see **Remarks**)
- `pbData`: Buffer in which to return the bitmap information

## Remarks

Before calling this method, you must properly allocate the size of the pbData buffer. Call [IEdmBitmap5::GetBitmapInfoSize](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5~GetBitmapInfoSize.html) to determine the size of buffer to allocate and to specify lDataSize.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_INVALIDARG: lDataSize does not match the size of the returned structure.

## See Also

[IEdmBitmap5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5.html)
[IEdmBitmap5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
