---
title: "IEdmBom Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBom"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom.html"
---

# IEdmBom Interface

Allows you to access a Bill of Materials (BOM).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBom
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmBom : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmBom : public IEdmObject5
```

## Examples

[Access Bill of Materials (VB.NET)](Access_Bill_of_Materials_Example_VBNET.htm)
[Access Bill of Materials (C#)](Access_Bill_of_Materials_Example_CSharp.htm)

## Remarks

This interface inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).

To access this interface:

1. Call IEdmVault5::GetObject with eType = [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_BOM.

- or -

1. Create an [EdmObjectInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectInfo.html) structure with meType = EdmObjectType.EdmObject_BOM.
2. Call IEdmVault9::GetObjects with ppoObjects set to the EdmObjectInfo structure created in step 1.

## Accessors

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

[IEdmVault9::GetObjects](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault9~GetObjects.html)

## See Also

[IEdmBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmFile7::GetDerivedBOMs Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7~GetDerivedBOMs.html)
