---
title: "EdmRefVar Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRefVar"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar.html"
---

# EdmRefVar Structure

Holds information about a single file reference variable; i.e., a variable stored on the reference relationship between an assembly file and one of its part files.

## Syntax

### Visual Basic

```vb
Public Structure EdmRefVar
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmRefVar : System.ValueType
```

### C++/CLI

```cpp
public value class EdmRefVar : public System.ValueType
```

## Examples

struct EdmRefVar{
integer [mlVarID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~mlVarID.html);
integer [mlParentFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~mlParentFileID.html);
integer [mlParentVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~mlParentVersion.html);
integer [mlChildFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~mlChildFileID.html);
string [mbsChildCfgName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~mbsChildCfgName.html);
string [mbsParentCfgName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~mbsParentCfgName.html);
object [moValue](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~moValue.html);
integer [mhResult](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar~mhResult.html);
};

## Examples

[Batch Get and Set Reference Variables (VB.NET)](Batch_Get_and_Set_Reference_Variables_Example_VBNET.htm)
[Batch Get and Set Reference Variables (C#)](Batch_Get_and_Set_Reference_Variables_Example_CSharp.htm)

## Remarks

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

Each component of the assembly is in a separate reference relationship with the assembly. The BOM column configured to **Look for variable in reference specific values** contains reference variable values. Use [IEdmBatchRefVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars.html) to get and set these reference variable values.

## See Also

[EdmRefVar Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
