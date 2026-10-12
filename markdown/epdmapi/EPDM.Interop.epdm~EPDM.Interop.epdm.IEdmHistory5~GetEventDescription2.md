---
title: "GetEventDescription2 Method (IEdmHistory5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory5"
member: "GetEventDescription2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetEventDescription2.html"
---

# GetEventDescription2 Method (IEdmHistory5)

Gets the event description for the specified history item in the specified language.

## Syntax

### Visual Basic

```vb
Function GetEventDescription2( _
   ByRef historyItem As EdmHistoryItem2, _
   Optional ByVal eLancode As EdmLangCode _
) As System.String
```

### C#

```csharp
System.string GetEventDescription2(
   ref EdmHistoryItem2 historyItem,
   EdmLangCode eLancode
)
```

### C++/CLI

```cpp
System.String^ GetEventDescription2(
   EdmHistoryItem2% historyItem,
   EdmLangCode eLancode
)
```

### Parameters

- `historyItem`: [EdmHistoryItem2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2.html) (see **Remarks**)
- `eLancode`: Localization language as defined in [EdmLangCode](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLangCode.html)

## Examples

See the [IEdmHistory3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html) examples.

## Remarks

Before calling this method, call [IEdmHistory5::GetSortedHistory2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetSortedHistory2.html) to specify a history item.

## See Also

[IEdmHistory5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5.html)
[IEdmHistory5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5_members.html)
[IEdmHistory5::GetHistory2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetHistory2.html)
[IEdmHistory5::GetSortedHistory2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~GetSortedHistory2.html)
[IEdmHistory5::Rollback2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory5~Rollback2.html)

## Availability

SOLIDWORKS PDM Professional 2026 SP02
