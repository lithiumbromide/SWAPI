---
title: "IDimensionStyleUserData Interface"
project: ""
interface: "IDimensionStyleUserData"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html"
---

# IDimensionStyleUserData Interface

Allows access to the DimensionStyle of a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

## Syntax

### Visual Basic

```vb
Public Interface IDimensionStyleUserData
```

### C#

```csharp
public interface IDimensionStyleUserData
```

### JScript

```
public interface IDimensionStyleUserData
```

### Managed Extensions for C++

```
public __gc __interface IDimensionStyleUserData
```

### C++/CLI

```cpp
public interface class IDimensionStyleUserData
```

## Examples

[Change DimensionStyle Options of Leader (C#)](Change_DimensionStyle_Options_of_Leader_Example_CSharp.htm)
[Change DimensionStyle Options of Leader (VB.NET)](Change_DimensionStyle_Options_of_Leader_Example_VBNET.htm)
[Change DimensionStyle Options of Leader (VBA)](Change_DimensionStyle_Options_of_Leader_Example_VBA.htm)

## Remarks

If you change a [DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html), then all entities using that DimensionStyle also change. However, if you use the IDimensionStyleUserData interface, then you can change the DimensionStyle of a specific Dimension, Leader, or geometric Tolerance entity and not change all other Dimension, Leader, or geometric Tolerance entities using that DimensionStyle.

## Accessors

[IGeneralDimension::GetDimensionStyleUserData](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetDimensionStyleUserData.html)

[ILeader::GetDimensionStyleUserData](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetDimensionStyleUserData.html)

[ITolerance::GetDimensionStyleUserData](Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetDimensionStyleUserData.html)

## Access Diagram

DSObjectModel.pdf#DimensionStyleUserData

[DimensionStyleUserData](DSObjectModel.pdf#DimensionStyleUserData)

## See Also

[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
