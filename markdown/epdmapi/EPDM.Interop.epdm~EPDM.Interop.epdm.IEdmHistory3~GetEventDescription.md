---
title: "GetEventDescription Method (IEdmHistory3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory3"
member: "GetEventDescription"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3~GetEventDescription.html"
---

# GetEventDescription Method (IEdmHistory3)

Gets the event description for the specified history item in the specified language.

## Syntax

### Visual Basic

```vb
Function GetEventDescription( _
   ByRef historyItem As EdmHistoryItem, _
   Optional ByVal eLancode As EdmLangCode _
) As System.String
```

### C#

```csharp
System.string GetEventDescription(
   ref EdmHistoryItem historyItem,
   EdmLangCode eLancode
)
```

### C++/CLI

```cpp
System.String^ GetEventDescription(
   EdmHistoryItem% historyItem,
   EdmLangCode eLancode
)
```

### Parameters

- `historyItem`: [EdmHistoryItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem.html) (see **Remarks**)
- `eLancode`: Localization language as defined in [EdmLangCode](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLangCode.html)

### Return Value

History item event description

## Examples

See the [IEdmHistory3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html) examples.

## Remarks

Before calling this method, call [IEdmHistory3::GetSortedHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3~GetSortedHistory.html) to specify a history item.

## See Also

[IEdmHistory3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3.html)
[IEdmHistory3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory3_members.html)

## Availability

SOLIDWORKS PDM Professional 2020
