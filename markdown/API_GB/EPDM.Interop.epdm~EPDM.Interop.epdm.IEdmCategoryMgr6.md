---
title: "IEdmCategoryMgr6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCategoryMgr6"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6.html"
---

# IEdmCategoryMgr6 Interface

Allows you to access all of the categories that have been set up in a vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCategoryMgr6
```

### C#

```csharp
public interface IEdmCategoryMgr6
```

### C++/CLI

```cpp
public interface class IEdmCategoryMgr6
```

## Examples

[Get Categories (VB.NET)](Get_Categories_Example_VBNET.htm)
[Get Categories (C#)](Get_Categories_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

To access this interface, call IEdmVault7::CreateUtility with eType = [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_CategoryMgr.

Files in SOLIDWORKS PDM Professional can be categorized according to certain criteria such as card properties, file extensions, etc. The categories are set up using SOLIDWORKS PDM Professional’s administration tool.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmCategoryMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmCategory6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategory6.html)
