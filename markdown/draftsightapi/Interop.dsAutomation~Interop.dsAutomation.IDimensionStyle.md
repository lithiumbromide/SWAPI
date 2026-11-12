---
title: "IDimensionStyle Interface"
project: ""
interface: "IDimensionStyle"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html"
---

# IDimensionStyle Interface

Allows access to a DimensionStyle.

## Syntax

### Visual Basic

```vb
Public Interface IDimensionStyle
```

### C#

```csharp
public interface IDimensionStyle
```

### JScript

```
public interface IDimensionStyle
```

### Managed Extensions for C++

```
public __gc __interface IDimensionStyle
```

### C++/CLI

```cpp
public interface class IDimensionStyle
```

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)
[Get DimensionStyle Names and Options (C#)](Get_DimensionStyle_Names_and_Options_Example_CSharp.htm)
[Get DimensionStyle Names and Options (VB.NET)](Get_DimensionStyle_Names_and_Options_Example_VBNET.htm)
[Get DimensionStyle Names and Options (VBA)](Get_DimensionStyle_Names_and_Options_Example_VBA.htm)
[Get DimensionStyle Names and Options (JavaScript)](Get_DimensionStyle_Names_and_Options_Example_JS.htm)

## Remarks

If you change a DimensionStyle, then all entities using that DimensionStyle are impacted. However, if you use the [IDimensionStyleUserData](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html) interface, then you can change the DimensionStyle of a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity without impacting all other Dimension, Leader, or geometric Tolerance entities using that DimensionStyle.

## Accessors

[IDimensionStyleManager::CreateDimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~CreateDimensionStyle.html)

[IDimensionStyleManager::GetActiveDimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~GetActiveDimensionStyle.html)

[IDimensionStyleManager::GetDimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~GetDimensionStyle.html)

[IDimensionStyleManager::GetDimensionStyles](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~GetDimensionStyles.html)

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[IGeneralDimension::GetDimensionStyleData](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetDimensionStyleData.html)

[ILeader::GetDimensionStyleData](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetDimensionStyleData.html)

[ITolerance::GetDimensionStyleData](Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetDimensionStyleData.html)

## Access Diagram

DSObjectModel.pdf#DimensionStyle

[DimensionStyle](DSObjectModel.pdf#DimensionStyle)

## See Also

[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDimensionStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager.html)
