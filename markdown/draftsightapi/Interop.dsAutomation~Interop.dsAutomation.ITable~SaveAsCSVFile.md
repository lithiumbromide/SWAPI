---
title: "SaveAsCSVFile Method (ITable)"
project: ""
interface: "ITable"
member: "SaveAsCSVFile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SaveAsCSVFile.html"
---

# SaveAsCSVFile Method (ITable)

Saves the content of the Table as a **.csv** (comma-separated values) file.

## Syntax

### Visual Basic

```vb
Function SaveAsCSVFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool SaveAsCSVFile(
   System.string FileName
)
```

### JScript

```
function SaveAsCSVFile(
   FileName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SaveAsCSVFile(
   System.string* FileName
)
```

### C++/CLI

```cpp
System.bool SaveAsCSVFile(
   System.String^ FileName
)
```

### Parameters

- `FileName`: Full path, file name, and filename extension of **.csv** to which to save the contents of the file

### Return Value

True if the contents of the Table are saved to a **.csv** file, false if not

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)

## Availability

DraftSight V1R4.0
