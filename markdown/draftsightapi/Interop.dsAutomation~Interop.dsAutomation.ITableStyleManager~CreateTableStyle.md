---
title: "CreateTableStyle Method (ITableStyleManager)"
project: ""
interface: "ITableStyleManager"
member: "CreateTableStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~CreateTableStyle.html"
---

# CreateTableStyle Method (ITableStyleManager)

Creates a TableStyle.

## Syntax

### Visual Basic

```vb
Sub CreateTableStyle( _
   ByVal Name As System.String, _
   ByRef TableStyle As TableStyle, _
   ByRef Result As dsCreateObjectResult_e _
)
```

### C#

```csharp
void CreateTableStyle(
   System.string Name,
   out TableStyle TableStyle,
   out dsCreateObjectResult_e Result
)
```

### JScript

```
function CreateTableStyle(
   Name : System.String,
   TableStyle : TableStyle,
   Result : dsCreateObjectResult_e
);
```

### Managed Extensions for C++

```
void CreateTableStyle(
   System.string* Name,
   [PARAMFLAG::Out] TableStyle* TableStyle,
   [PARAMFLAG::Out] dsCreateObjectResult_e Result
)
```

### C++/CLI

```cpp
void CreateTableStyle(
   System.String^ Name,
   [Out] TableStyle^ TableStyle,
   [Out] dsCreateObjectResult_e Result
)
```

### Parameters

- `Name`: Name
- `TableStyle`: [TableStyle](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
- `Result`: Status of creating TableStyle as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

[Create Table (C#)](Create_Table_Example_CSharp.htm)
[Create Table (VB.NET)](Create_Table_Example_VBNET.htm)
[Create Table (VBA)](Create_Table_Example_VBA.htm)
[Create Table (JavaScript)](Create_Table_Example_JS.htm)

## See Also

[ITableStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager.html)
[ITableStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager_members.html)
[ITableStyleManager::RemoveTableStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~RemoveTableStyle.html)
[ITableStyle::Name Property](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~Name.html)

## Availability

DraftSight V1R3.0
