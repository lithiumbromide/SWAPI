---
title: "InsertAlignedDimension Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertAlignedDimension"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAlignedDimension.html"
---

# InsertAlignedDimension Method (ISketchManager)

Inserts an aligned linear Dimension.

## Syntax

### Visual Basic

```vb
Function InsertAlignedDimension( _
   ByVal ExtensionLine1PointDblArray As System.Object, _
   ByVal ExtensionLine2PointDblArray As System.Object, _
   ByVal DimensionLinePointDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As AlignedDimension
```

### C#

```csharp
AlignedDimension InsertAlignedDimension(
   System.object ExtensionLine1PointDblArray,
   System.object ExtensionLine2PointDblArray,
   System.object DimensionLinePointDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertAlignedDimension(
   ExtensionLine1PointDblArray : System.Object,
   ExtensionLine2PointDblArray : System.Object,
   DimensionLinePointDblArray : System.Object,
   DimensionTextOverride : System.String
) : AlignedDimension;
```

### Managed Extensions for C++

```
AlignedDimension* InsertAlignedDimension(
   System.Object* ExtensionLine1PointDblArray,
   System.Object* ExtensionLine2PointDblArray,
   System.Object* DimensionLinePointDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
AlignedDimension^ InsertAlignedDimension(
   System.Object^ ExtensionLine1PointDblArray,
   System.Object^ ExtensionLine2PointDblArray,
   System.Object^ DimensionLinePointDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `ExtensionLine1PointDblArray`: Array of three doubles indicating the point where to place the first extension line
- `ExtensionLine2PointDblArray`: Array of three doubles indicating the point where to place the second extension line
- `DimensionLinePointDblArray`: Array of three doubles indicating the point where to place the Dimension
- `DimensionTextOverride`: Text with which to override the default Dimension text

### Return Value

[Aligned linear Dimension](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension.html)

## Examples

[Create Aligned Linear and Ordinate Dimensions (C#)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_CSharp.htm)
[Create Aligned Linear and Ordinate Dimensions (VB.NET)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBNET.htm)
[Create Aligned Linear and Ordinate Dimensions (VBA)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBA.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)

## Remarks

- dsCommandOptionInt16_SetDmRltvMode = 0
  Explode dimension; no association to the two extension lines.
- dsCommandOptionInt16_SetDmRltvMode = 1
  No association to the two extension lines.
- dsCommandOptionInt16_SetDmRltvMode = 2
  Dimension is associated to the two extension lines, if they exist.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.2
