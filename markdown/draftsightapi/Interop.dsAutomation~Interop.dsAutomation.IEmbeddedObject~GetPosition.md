---
title: "GetPosition Method (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "GetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetPosition.html"
---

# GetPosition Method (IEmbeddedObject)

Gets the coordinates of the insertion point of this embedded object.

## Syntax

### Visual Basic

```vb
Sub GetPosition( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetPosition(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetPosition(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetPosition(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetPosition(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## Examples

[Insert Embedded Object (C#)](Insert_Embedded_Object_Example_CSharp.htm)
[Insert Embedded Object (VB.NET)](Insert_Embedded_Object_Example_VBNET.htm)
[Insert Embedded Object (JavaScript)](Insert_Embedded_Object_Example_JS.htm)
[Insert Embedded Object (VBA)](Insert_Embedded_Object_Example_VBA.htm)

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)
[IEmbeddedObject::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~SetPosition.html)

## Availability

DraftSight V1R1.4
