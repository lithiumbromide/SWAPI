---
title: "CreateDimensionStyle Method (IDimensionStyleManager)"
project: ""
interface: "IDimensionStyleManager"
member: "CreateDimensionStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~CreateDimensionStyle.html"
---

# CreateDimensionStyle Method (IDimensionStyleManager)

Creates a DimensionStyle.

## Syntax

### Visual Basic

```vb
Sub CreateDimensionStyle( _
   ByVal Name As System.String, _
   ByRef DimensionStyle As DimensionStyle, _
   ByRef Result As dsCreateObjectResult_e _
)
```

### C#

```csharp
void CreateDimensionStyle(
   System.string Name,
   out DimensionStyle DimensionStyle,
   out dsCreateObjectResult_e Result
)
```

### JScript

```
function CreateDimensionStyle(
   Name : System.String,
   DimensionStyle : DimensionStyle,
   Result : dsCreateObjectResult_e
);
```

### Managed Extensions for C++

```
void CreateDimensionStyle(
   System.string* Name,
   [PARAMFLAG::Out] DimensionStyle* DimensionStyle,
   [PARAMFLAG::Out] dsCreateObjectResult_e Result
)
```

### C++/CLI

```cpp
void CreateDimensionStyle(
   System.String^ Name,
   [Out] DimensionStyle^ DimensionStyle,
   [Out] dsCreateObjectResult_e Result
)
```

### Parameters

- `Name`: Name
- `DimensionStyle`: [DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
- `Result`: Status of creating a DimensionStyle as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[IDimensionStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager.html)
[IDimensionStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager_members.html)
[IDimensionStyleManager::RemoveDimensionStyle Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~RemoveDimensionStyle.html)

## Availability

DraftSight V1R1.1
