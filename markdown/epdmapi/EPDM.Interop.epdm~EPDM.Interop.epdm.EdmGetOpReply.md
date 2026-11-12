---
title: "EdmGetOpReply Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetOpReply"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetOpReply.html"
---

# EdmGetOpReply Enumeration

Options for continuing with a command; returned from [IEdmGetOpCallback2::ReportFailureEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetOpCallback2~ReportFailureEx.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmGetOpReply
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetOpReply : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetOpReply : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmGetRep_CallReportFailure | 0 = Call IEdmGetOpCallback::ReportFailure |
| EdmGetRep_Cancel | 1 = Cancel the operation |
| EdmGetRep_Process | 3 = Proceed to process the file |
| EdmGetRep_Skip | 2 = Skip the file but proceed with the operation |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
