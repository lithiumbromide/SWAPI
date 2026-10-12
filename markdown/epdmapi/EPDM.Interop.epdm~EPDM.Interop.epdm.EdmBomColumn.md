---
title: "EdmBomColumn Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomColumn"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn.html"
---

# EdmBomColumn Structure

Contains information about a single column in a Bill of Materials.

## Syntax

### Visual Basic

```vb
Public Structure EdmBomColumn
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBomColumn : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBomColumn : public System.ValueType
```

## Examples

struct EdmBomColumn{
integer [mlColumnID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn~mlColumnID.html);
integer [mlVariableID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn~mlVariableID.html);
[enum EdmVariableType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableType.html) [mlVariableType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn~mlVariableType.html);
integer [mlFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn~mlFlags.html);
[enum EdmBomColumnType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumnType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn~meType.html);
string [mbsCaption](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn~mbsCaption.html);
integer [mlWidth](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn~mlWidth.html);
};

## Examples

[Access Bill of Materials (VB.NET)](Access_Bill_of_Materials_Example_VBNET.htm)
[Access Bill of Materials (C#)](Access_Bill_of_Materials_Example_CSharp.htm)

## See Also

[EdmBomColumn Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
