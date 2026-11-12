---
title: "GetBoundingBox Method (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "GetBoundingBox"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetBoundingBox.html"
---

# GetBoundingBox Method (IEmbeddedObject)

Gets the bounding box enclosing the embedded object.

## Syntax

### Visual Basic

```vb
Sub GetBoundingBox( _
   ByRef X1 As System.Double, _
   ByRef Y1 As System.Double, _
   ByRef Z1 As System.Double, _
   ByRef X2 As System.Double, _
   ByRef Y2 As System.Double, _
   ByRef Z2 As System.Double _
)
```

### C#

```csharp
void GetBoundingBox(
   out System.double X1,
   out System.double Y1,
   out System.double Z1,
   out System.double X2,
   out System.double Y2,
   out System.double Z2
)
```

### JScript

```
function GetBoundingBox(
   X1 : System.double,
   Y1 : System.double,
   Z1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   Z2 : System.double
);
```

### Managed Extensions for C++

```
void GetBoundingBox(
   [PARAMFLAG::Out] System.double X1,
   [PARAMFLAG::Out] System.double Y1,
   [PARAMFLAG::Out] System.double Z1,
   [PARAMFLAG::Out] System.double X2,
   [PARAMFLAG::Out] System.double Y2,
   [PARAMFLAG::Out] System.double Z2
)
```

### C++/CLI

```cpp
void GetBoundingBox(
   [Out] System.double X1,
   [Out] System.double Y1,
   [Out] System.double Z1,
   [Out] System.double X2,
   [Out] System.double Y2,
   [Out] System.double Z2
)
```

### Parameters

- `X1`: x coordinate of a corner of the bounding box
- `Y1`: y coordinate of a corner of the bounding box
- `Z1`: z coordinate of a corner of the bounding box
- `X2`: x coordinate of the diagonal corner of the bounding box
- `Y2`: y coordinate of the diagonal corner of the bounding box
- `Z2`: z coordinate of the diagonal corner of the bounding box

## Examples

[Insert Embedded Object (JavaScript)](Insert_Embedded_Object_Example_JS.htm)
[Insert Embedded Object (VB.NET)](Insert_Embedded_Object_Example_VBNET.htm)
[Insert Embedded Object (C#)](Insert_Embedded_Object_Example_CSharp.htm)
[Insert Embedded Object (VBA)](Insert_Embedded_Object_Example_VBA.htm)

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)

## Availability

DraftSight V1R1.4
