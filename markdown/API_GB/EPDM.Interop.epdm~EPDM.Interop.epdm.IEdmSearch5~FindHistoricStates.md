---
title: "FindHistoricStates Property (IEdmSearch5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch5"
member: "FindHistoricStates"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~FindHistoricStates.html"
---

# FindHistoricStates Property (IEdmSearch5)

Gets or sets whether to find all files that have ever been in the state specified by [IEdmSearch5::State](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~State.html).

## Syntax

### Visual Basic

```vb
Property FindHistoricStates As System.Boolean
```

### C#

```csharp
System.bool FindHistoricStates {get; set;}
```

### C++/CLI

```cpp
property System.bool FindHistoricStates {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to find all files that have ever been in IEdmSearch5::State, false to return only files that are currently in IEdmSearch5::State

## Remarks

This property is only valid if [IEdmSearch5::State](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~State.html) is set.

## See Also

[IEdmSearch5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html)
[IEdmSearch5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
