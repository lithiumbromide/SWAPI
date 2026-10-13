---
title: "EdmObjectInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmObjectInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectInfo.html"
---

# EdmObjectInfo Structure

Use in calls to [IEdmVault9::GetObjects](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault9~GetObjects.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmObjectInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmObjectInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmObjectInfo : public System.ValueType
```

## Examples

struct EdmObjectInfo

{
[EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectInfo~meType.html);
object [moObjectID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectInfo~moObjectID.html);
[IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html)* [mpoObject](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectInfo~mpoObject.html);
integer [mhResult](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectInfo~mhResult.html);
};

## Examples

[Batch Update Card Variables (C#)](Batch_Update_Variables_Example_CSharp.htm)
[Batch Update Card Variables (VB.NET)](Batch_Update_Variables_Example_VBNET.htm)

## Remarks

The structure contains both input and output.

## See Also

[EdmObjectInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2008
