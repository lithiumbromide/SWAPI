---
title: "EdmBomVersion Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomVersion"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion.html"
---

# EdmBomVersion Structure

Contains information about a Bill of Materials version, revision, or label.

## Syntax

### Visual Basic

```vb
Public Structure EdmBomVersion
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBomVersion : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBomVersion : public System.ValueType
```

## Examples

struct EdmBomVersion{
[enum EdmBomVersionType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersionType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion~meType.html);
integer [mlVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion~mlVersion.html);
datetime [moDate](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion~moDate.html);
string [mbsTag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion~mbsTag.html);
string [mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion~mbsComment.html);
};

## Examples

[Access Bill of Materials (VB.NET)](Access_Bill_of_Materials_Example_VBNET.htm)
[Access Bill of Materials (C#)](Access_Bill_of_Materials_Example_CSharp.htm)

## See Also

[EdmBomVersion Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
