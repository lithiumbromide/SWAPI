---
title: "HeaderOrientation Property (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "HeaderOrientation"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~HeaderOrientation.html"
---

# HeaderOrientation Property (ITableStyle)

Gets or sets whether the Table is created downward or upward from the insertion point.

## Syntax

### Visual Basic

```vb
Property HeaderOrientation As dsTableHeaderOrientation_e
```

### C#

```csharp
dsTableHeaderOrientation_e HeaderOrientation {get; set;}
```

### JScript

```
function get,set HeaderOrientation : dsTableHeaderOrientation_e
```

### Managed Extensions for C++

```
__property dsTableHeaderOrientation_e get_HeaderOrientation();
__property void set_HeaderOrientation(
   dsTableHeaderOrientation_e value
);
```

### C++/CLI

```cpp
property dsTableHeaderOrientation_e HeaderOrientation {
   dsTableHeaderOrientation_e get();
   void set (    dsTableHeaderOrientation_e value);
}
```

### Property Value

Direction in which to create the Table from the insertion point as defined in [dsTableHeaderOrientation_e](Interop.dsAutomation~Interop.dsAutomation.dsTableHeaderOrientation_e.html)

## Examples

[Create Table (C#)](Create_Table_Example_CSharp.htm)
[Create Table (VB.NET)](Create_Table_Example_VBNET.htm)
[Create Table (VBA)](Create_Table_Example_VBA.htm)
[Create Table (JavaScript)](Create_Table_Example_JS.htm)

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)

## Availability

DraftSight V1R3.0
