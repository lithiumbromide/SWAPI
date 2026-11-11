---
title: "InsertRotatedDimension Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertRotatedDimension"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRotatedDimension.html"
---

# InsertRotatedDimension Method (ISketchManager)

Inserts a rotated Dimension.

## Syntax

### Visual Basic

```vb
Function InsertRotatedDimension( _
   ByVal ExtensionLine1PointDblArray As System.Object, _
   ByVal ExtensionLine2PointDblArray As System.Object, _
   ByVal DimensionLinePointDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String, _
   ByVal RotationAngle As System.Double _
) As RotatedDimension
```

### C#

```csharp
RotatedDimension InsertRotatedDimension(
   System.object ExtensionLine1PointDblArray,
   System.object ExtensionLine2PointDblArray,
   System.object DimensionLinePointDblArray,
   System.string DimensionTextOverride,
   System.double RotationAngle
)
```

### JScript

```
function InsertRotatedDimension(
   ExtensionLine1PointDblArray : System.Object,
   ExtensionLine2PointDblArray : System.Object,
   DimensionLinePointDblArray : System.Object,
   DimensionTextOverride : System.String,
   RotationAngle : System.double
) : RotatedDimension;
```

### Managed Extensions for C++

```
RotatedDimension* InsertRotatedDimension(
   System.Object* ExtensionLine1PointDblArray,
   System.Object* ExtensionLine2PointDblArray,
   System.Object* DimensionLinePointDblArray,
   System.string* DimensionTextOverride,
   System.double RotationAngle
)
```

### C++/CLI

```cpp
RotatedDimension^ InsertRotatedDimension(
   System.Object^ ExtensionLine1PointDblArray,
   System.Object^ ExtensionLine2PointDblArray,
   System.Object^ DimensionLinePointDblArray,
   System.String^ DimensionTextOverride,
   System.double RotationAngle
)
```

### Parameters

- `ExtensionLine1PointDblArray`: Array of three doubles indicating the origin of the first extension line
- `ExtensionLine2PointDblArray`: Array of three doubles indicating the origin of the second extension line
- `DimensionLinePointDblArray`: Array of three doubles indicating the point where to place the rotated Dimension
- `DimensionTextOverride`: Text with which to override the default Dimension text
- `RotationAngle`: Angle by which to rotate the Dimension (see **Remarks**)

### Return Value

[Rotated Dimension](Interop.dsAutomation~Interop.dsAutomation.IRotatedDimension.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## Remarks

The value specified for RotationAngle affects the angle of the Dimension lines and text. Setting RotationAngle to:

- 0 results in horizontal Dimension lines and text.
- a non-0 value results in vertical Dimension lines and text.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertLinearDimension Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertLinearDimension.html)

## Availability

DraftSight V1R1.2
