---
title: "GetSimplifiedText Method (ITable)"
project: ""
interface: "ITable"
member: "GetSimplifiedText"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetSimplifiedText.html"
---

# GetSimplifiedText Method (ITable)

Gets the raw text in the specified cell.

## Syntax

### Visual Basic

```vb
Function GetSimplifiedText( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetSimplifiedText(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetSimplifiedText(
   Row : System.int,
   Column : System.int
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetSimplifiedText(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.String^ GetSimplifiedText(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Row in which the cell exists
- `Column`: Column in which the cell exists

### Return Value

Unformatted text string

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::GetText Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetText.html)

## Availability

DraftSight 2018 SP0
