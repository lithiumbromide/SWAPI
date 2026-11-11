---
title: "InsertLinearDimension Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertLinearDimension"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertLinearDimension.html"
---

# InsertLinearDimension Method (ISketchManager)

Inserts a linear Dimension.

## Syntax

### Visual Basic

```vb
Function InsertLinearDimension( _
   ByVal ExtensionLine1PointDblArray As System.Object, _
   ByVal ExtensionLine2PointDblArray As System.Object, _
   ByVal DimensionLinePointDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As RotatedDimension
```

### C#

```csharp
RotatedDimension InsertLinearDimension(
   System.object ExtensionLine1PointDblArray,
   System.object ExtensionLine2PointDblArray,
   System.object DimensionLinePointDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertLinearDimension(
   ExtensionLine1PointDblArray : System.Object,
   ExtensionLine2PointDblArray : System.Object,
   DimensionLinePointDblArray : System.Object,
   DimensionTextOverride : System.String
) : RotatedDimension;
```

### Managed Extensions for C++

```
RotatedDimension* InsertLinearDimension(
   System.Object* ExtensionLine1PointDblArray,
   System.Object* ExtensionLine2PointDblArray,
   System.Object* DimensionLinePointDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
RotatedDimension^ InsertLinearDimension(
   System.Object^ ExtensionLine1PointDblArray,
   System.Object^ ExtensionLine2PointDblArray,
   System.Object^ DimensionLinePointDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `ExtensionLine1PointDblArray`: Array of three doubles indicating the origin of the first extension line
- `ExtensionLine2PointDblArray`: Array of three doubles indicating the origin of the second extension line
- `DimensionLinePointDblArray`: Array of three doubles indicating the point where to place the linear Dimension
- `DimensionTextOverride`: Text with which to override the default Dimension text

### Return Value

[Linear Dimension](Interop.dsAutomation~Interop.dsAutomation.IRotatedDimension.html)

## Remarks

Inserting a linear Dimension creates a rotated linear Dimension with a rotation angle of 0°, which results in horizontal Dimension lines and text.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertRotatedDimension Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRotatedDimension.html)

## Availability

DraftSight V1R3.0
