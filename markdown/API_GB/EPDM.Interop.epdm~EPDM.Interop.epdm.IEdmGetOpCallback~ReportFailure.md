---
title: "ReportFailure Method (IEdmGetOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmGetOpCallback"
member: "ReportFailure"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback~ReportFailure.html"
---

# ReportFailure Method (IEdmGetOpCallback)

Obsolete. Superseded by [IEdmGetOpCallback2::ReportFailureEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback2~ReportFailureEx.html).

## Syntax

### Visual Basic

```vb
Function ReportFailure( _
   ByVal lFileID As System.Integer, _
   ByVal bsPath As System.String, _
   ByVal hError As System.Integer, _
   ByVal bsDetails As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool ReportFailure(
   System.int lFileID,
   System.string bsPath,
   System.int hError,
   System.string bsDetails
)
```

### C++/CLI

```cpp
System.bool ReportFailure(
   System.int lFileID,
   System.String^ bsPath,
   System.int hError,
   System.String^ bsDetails
)
```

### Parameters

- `lFileID`: ID of affected file
- `bsPath`: Path to the affected file
- `hError`: Error code
- `bsDetails`: Detailed description of the error

### Return Value

True to continue, false to cancel the operation

## Remarks

SOLIDWORKS PDM Professional calls this method when an error related to a specific file has occurred. Implement this method to display a message box to the user or to automatically process the error.

This method is extended by [IEdmGetOpCallback2::ReportFailureEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback2~ReportFailureEx.html) which provides support for recovering from archive file errors.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmGetOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback.html)
[IEdmGetOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
