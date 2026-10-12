---
title: "EdmBomInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomInfo.html"
---

# EdmBomInfo Structure

Contains information about a Bill of Materials.

## Syntax

### Visual Basic

```vb
Public Structure EdmBomInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBomInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBomInfo : public System.ValueType
```

## Examples

struct EdmBomInfo{
integer [mlBomID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomInfo~mlBomID.html);
[enum EdmBomType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomInfo~meType.html);
string [mbsBomName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomInfo~mbsBomName.html);
};

## Examples

[Access Bill of Materials (VB.NET)](Access_Bill_of_Materials_Example_VBNET.htm)
[Access Bill of Materials (C#)](Access_Bill_of_Materials_Example_CSharp.htm)

## Remarks

Returned by [IEdmFile7::GetDerivedBOMs](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7~GetDerivedBOMs.html).

## See Also

[EdmBomInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
