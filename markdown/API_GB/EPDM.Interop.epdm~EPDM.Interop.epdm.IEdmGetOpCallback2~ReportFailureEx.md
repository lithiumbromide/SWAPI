---
title: "ReportFailureEx Method (IEdmGetOpCallback2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmGetOpCallback2"
member: "ReportFailureEx"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback2~ReportFailureEx.html"
---

# ReportFailureEx Method (IEdmGetOpCallback2)

Notifies about a file error.

## Syntax

### Visual Basic

```vb
Function ReportFailureEx( _
   ByVal lFileID As System.Integer, _
   ByVal lVersionNo As System.Integer, _
   ByVal bsPath As System.String, _
   ByVal eError As EdmGetOpError, _
   ByVal oArg1 As System.Object, _
   ByVal oArg2 As System.Object, _
   ByVal oArg3 As System.Object _
) As EdmGetOpReply
```

### C#

```csharp
EdmGetOpReply ReportFailureEx(
   System.int lFileID,
   System.int lVersionNo,
   System.string bsPath,
   EdmGetOpError eError,
   System.object oArg1,
   System.object oArg2,
   System.object oArg3
)
```

### C++/CLI

```cpp
EdmGetOpReply ReportFailureEx(
   System.int lFileID,
   System.int lVersionNo,
   System.String^ bsPath,
   EdmGetOpError eError,
   System.Object^ oArg1,
   System.Object^ oArg2,
   System.Object^ oArg3
)
```

### Parameters

- `lFileID`: ID of the affected file
- `lVersionNo`: Version of the affected file
- `bsPath`: Path to the affected file
- `eError`: Error code as defined in [EdmGetOpError](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetOpError.html)
- `oArg1`: Unique 64-bit version ID
- `oArg2`: Reserved for future use
- `oArg3`: Reserved for future use

### Return Value

Reply with how to proceed as defined in [EdmGetOpReply](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetOpReply.html)

## Remarks

This method extends [IEdmGetOpCallback::ReportFailure](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ReportFailure.html) which does not support recovering from archive file errors.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmGetOpCallback2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback2.html)
[IEdmGetOpCallback2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback2_members.html)

## Availability

SOLIDWORKS PDM Professional 2011
