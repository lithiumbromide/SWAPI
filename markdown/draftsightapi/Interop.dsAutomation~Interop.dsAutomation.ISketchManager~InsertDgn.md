---
title: "InsertDgn Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertDgn"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDgn.html"
---

# InsertDgn Method (ISketchManager)

Inserts a DGN image.

## Syntax

### Visual Basic

```vb
Function InsertDgn( _
   ByVal PathName As System.String, _
   ByVal ModelName As System.String, _
   ByVal ConversionUnit As dsDgnConversionUnitType_e, _
   ByVal InsertX As System.Double, _
   ByVal InsertY As System.Double, _
   ByVal InsertZ As System.Double, _
   ByVal Scale As System.Double, _
   ByVal Rotation As System.Double _
) As DgnReference
```

### C#

```csharp
DgnReference InsertDgn(
   System.string PathName,
   System.string ModelName,
   dsDgnConversionUnitType_e ConversionUnit,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### JScript

```
function InsertDgn(
   PathName : System.String,
   ModelName : System.String,
   ConversionUnit : dsDgnConversionUnitType_e,
   InsertX : System.double,
   InsertY : System.double,
   InsertZ : System.double,
   Scale : System.double,
   Rotation : System.double
) : DgnReference;
```

### Managed Extensions for C++

```
DgnReference* InsertDgn(
   System.string* PathName,
   System.string* ModelName,
   dsDgnConversionUnitType_e ConversionUnit,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### C++/CLI

```cpp
DgnReference^ InsertDgn(
   System.String^ PathName,
   System.String^ ModelName,
   dsDgnConversionUnitType_e ConversionUnit,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### Parameters

- `PathName`: Path and file name of the DGN image to insert
- `ModelName`: Model name
- `ConversionUnit`: Conversion unit as defined in [dsDgnConversionUnitType_e](Interop.dsAutomation~Interop.dsAutomation.dsDgnConversionUnitType_e.html)
- `InsertX`: x coordinate where to insert the DGN image
- `InsertY`: y coordinate where to insert the DGN image
- `InsertZ`: z coordinate where to insert the DGN image
- `Scale`: Scale factor for each axis
- `Rotation`: Angle by which to rotate the DGN image

### Return Value

[IDgnReference](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)

## Examples

[Insert Picture (VBA)](Insert_Picture_Example_VBA.htm)
[Insert Picture (VB.NET)](Insert_Picture_Example_VBNET.htm)
[Insert Picture (C#)](Insert_Picture_Example_CSharp.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight 2020 SP0
