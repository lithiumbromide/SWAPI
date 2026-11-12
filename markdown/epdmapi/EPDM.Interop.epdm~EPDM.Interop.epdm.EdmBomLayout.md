---
title: "EdmBomLayout Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomLayout"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout.html"
---

# EdmBomLayout Structure

Contains information about a Bill of Materials layout.

## Syntax

### Visual Basic

```vb
Public Structure EdmBomLayout
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBomLayout : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBomLayout : public System.ValueType
```

## Examples

struct EdmBomLayout{
integer [mlLayoutID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout~mlLayoutID.html);
string [mbsLayoutName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout~mbsLayoutName.html);
};

## Examples

[Access Bill of Materials (VB.NET)](Access_Bill_of_Materials_Example_VBNET.htm)
[Access Bill of Materials (C#)](Access_Bill_of_Materials_Example_CSharp.htm)

## Remarks

Returned by [IEdmBomMgr::GetBomLayouts](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr~GetBomLayouts.html).

## See Also

[EdmBomLayout Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
