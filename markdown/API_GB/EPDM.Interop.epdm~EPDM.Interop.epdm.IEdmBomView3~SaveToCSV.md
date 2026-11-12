---
title: "SaveToCSV Method (IEdmBomView3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomView3"
member: "SaveToCSV"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView3~SaveToCSV.html"
---

# SaveToCSV Method (IEdmBomView3)

Saves this BOM to a comma separated values (CSV) file.

## Syntax

### Visual Basic

```vb
Sub SaveToCSV( _
   ByVal bsFilePath As System.String, _
   ByVal bCreateLevelColumn As System.Boolean _
)
```

### C#

```csharp
void SaveToCSV(
   System.string bsFilePath,
   System.bool bCreateLevelColumn
)
```

### C++/CLI

```cpp
void SaveToCSV(
   System.String^ bsFilePath,
   System.bool bCreateLevelColumn
)
```

### Parameters

- `bsFilePath`: Path and file name (***.CSV**) to which to save this BOM
- `bCreateLevelColumn`: True to include a level column in the CSV file for an indented BOM, false to not

## Examples

See the [IEdmBomView3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView3.html) examples.

## See Also

[IEdmBomView3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView3.html)
[IEdmBomView3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView3_members.html)

## Availability

SOLIDWORKS PDM Professional 2017
