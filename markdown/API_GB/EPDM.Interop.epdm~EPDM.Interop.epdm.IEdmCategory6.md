---
title: "IEdmCategory6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCategory6"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategory6.html"
---

# IEdmCategory6 Interface

Allows you to access a category.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCategory6
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmCategory6 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmCategory6 : public IEdmObject5
```

## Examples

[Get Categories (VB.NET)](Get_Categories_Example_VBNET.htm)
[Get Categories (C#)](Get_Categories_Example_CSharp.htm)

## Remarks

This interface inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).

To access this interface, call IEdmVault5::GetObject with eType = [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_Category.

## Accessors

[IEdmCategoryMgr6::GetNextCategory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6~GetNextCategory.html)

[IEdmFile6::Category](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6~Category.html)

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

## See Also

[IEdmCategory6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategory6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
