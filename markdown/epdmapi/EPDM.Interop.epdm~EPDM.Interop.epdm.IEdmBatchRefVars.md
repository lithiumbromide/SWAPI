---
title: "IEdmBatchRefVars Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchRefVars"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars.html"
---

# IEdmBatchRefVars Interface

Allows you to access several file reference variables all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchRefVars
```

### C#

```csharp
public interface IEdmBatchRefVars
```

### C++/CLI

```cpp
public interface class IEdmBatchRefVars
```

## Examples

[Batch Get and Set Reference Variables (VB.NET)](Batch_Get_and_Set_Reference_Variables_Example_VBNET.htm)
[Batch Get and Set Reference Variables (C#)](Batch_Get_and_Set_Reference_Variables_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

Reference variables are used in Bill of Materials columns that are configured to look for reference-specific values. To create a reference variable:

1. Open the SOLIDWORKS PDM Professional Administration tool.
2. Log into a vault.
3. Double-click **Bill of Materials > BOM**.
4. Click a column in the **Columns** list.
5. Select **Look for variable in reference specific values**.
6. Click **OK**.
7. In a vault view, check out an assembly.
8. Click the **Bill of Materials** tab.
9. In the column configured to use reference-specific values, type text.
10. Click **Save** in the Bill of Materials toolbar.

Each component of the assembly is in a separate reference relationship with the assembly. The BOM column configured to **Look for variable in reference specific values** contains reference variable values. Use this interface to get and set these reference variable values.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchRefVars Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
