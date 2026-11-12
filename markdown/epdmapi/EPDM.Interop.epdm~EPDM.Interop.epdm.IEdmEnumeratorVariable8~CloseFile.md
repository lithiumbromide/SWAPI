---
title: "CloseFile Method (IEdmEnumeratorVariable8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable8"
member: "CloseFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8~CloseFile.html"
---

# CloseFile Method (IEdmEnumeratorVariable8)

Closes the file that is open for access by this interface.

## Syntax

### Visual Basic

```vb
Sub CloseFile( _
   ByVal bFlush As System.Boolean _
)
```

### C#

```csharp
void CloseFile(
   System.bool bFlush
)
```

### C++/CLI

```cpp
void CloseFile(
   System.bool bFlush
)
```

### Parameters

- `bFlush`: True to call [IEdmEnumeratorVariable5::Flush](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~Flush.html) before closing the file, false to not

## Examples

[Set Part Number Using Default Serial Numbers (C#)](Set_Part_Number_Using_Default_Serial_Numbers_Example_CSharp.htm)
[Set Part Number Using Default Serial Numbers (VB.NET)](Set_Part_Number_Using_Default_Serial_Numbers_Example_VBNET.htm)

## Remarks

After closing the file using this method, none of the other methods in this interface work.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmEnumeratorVariable8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8.html)
[IEdmEnumeratorVariable8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
