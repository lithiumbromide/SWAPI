---
title: "IXRecord Interface"
project: ""
interface: "IXRecord"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord.html"
---

# IXRecord Interface

Allows access to a record, also called an XRecord, in a [dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html) of a drawing.

## Syntax

### Visual Basic

```vb
Public Interface IXRecord
```

### C#

```csharp
public interface IXRecord
```

### JScript

```
public interface IXRecord
```

### Managed Extensions for C++

```
public __gc __interface IXRecord
```

### C++/CLI

```cpp
public interface class IXRecord
```

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)
[Create and Remove Dictionary (JavaScript)](Create_and_Remove_Dictionary_Example_JS.htm)

## Remarks

An XRecord's data is made up of:

- Markers, which are stored as integers and which help identify the data type of an XRecord's data. Valid values for markers are shown in the following table.
- Data, which are variable data types such as strings, doubles, integers, etc.

  | Marker | Data | Data type |
  | --- | --- | --- |
  | 1 | Text | String |
  | 2 | Name | String |
  | 3-4 | Text | String |
  | 5 | Handle | String |
  | 6-8 | Name | String |
  | 9 | Text | String |
  | 10-19 | Point | Three numbers |
  | 20-49 | Double | Double |
  | 50-59 | Angle | Double |
  | 60-79 | Integer | Signed 16-bit integer, also called Int16 |
  | 90-99 | Integer | Signed 32-bit integer, also called Int32 |
  | 100-102 | Text | String |
  | 105 | Handle of an entity | String |
  | 110-119 | Point | Three numbers |
  | 120-149 | Double | Double |
  | 160-169 | Integer | Signed 64-bit integer, also called Int64 |
  | 170-179 | Integer | Signed 16-bit integer, also called Int16 |
  | 210-219 | Point | Three numbers |
  | 220 | Double | Double |
  | 221-223 | Point | Three numbers |
  | 230 | Double | Double |
  | 231-233 | Point | Three numbers |
  | 270-279 | Integer | Signed 16-bit integer, also called Int16 |
  | 280-289 | Integer | Signed 8-bit integer, also called Int8 |
  | 290-299 | Boolean | Boolean |
  | 300-309 | Text | String |
  | 310-319 | Binary chunk | Variable-length binary array; maximum of 127 bytes |
  | 320-369 | Handle of an entity | String |

## Accessors

[IDictionary::CreateXRecord](Interop.dsAutomation~Interop.dsAutomation.IDictionary~CreateXRecord.html)

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

## Access Diagram

DSObjectModel.pdf#XRecord

[XRecord](DSObjectModel.pdf#XRecord)

## See Also

[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
