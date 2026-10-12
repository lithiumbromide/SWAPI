---
title: "EdmSelectionObject Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmSelectionObject"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject.html"
---

# EdmSelectionObject Structure

Contains data returned from [IEdmSelectionList6::GetNext2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6~GetNext2.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmSelectionObject
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmSelectionObject : System.ValueType
```

### C++/CLI

```cpp
public value class EdmSelectionObject : public System.ValueType
```

## Examples

struct EdmSelectionObject{
[EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject~meType.html);
string [mbsPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject~mbsPath.html);
integer [mlID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject~mlID.html);
integer [mlProjectID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject~mlProjectID.html);
integer [mlGetVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject~mlGetVersion.html);
integer [mlLocalVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject~mlLocalVersion.html);
integer [mlLatestVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject~mlLatestVersion.html);
};

## Examples

[Batch Change States of Files (VB.NET)](Batch_Change_States_of_Files_Example_VBNET.htm)
[Batch Change States of Files (C#)](Batch_Change_States_of_Files_Example_CSharp.htm)

## See Also

[EdmSelectionObject Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
