---
title: "InsertJoggedDimensionCircle Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertJoggedDimensionCircle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertJoggedDimensionCircle.html"
---

# InsertJoggedDimensionCircle Method (ISketchManager)

Inserts a jogged Dimension for an Circle.

## Syntax

### Visual Basic

```vb
Function InsertJoggedDimensionCircle( _
   ByVal Circle As Circle, _
   ByVal CenterPositionOverrideDblArray As System.Object, _
   ByVal JogLinePositionDblArray As System.Object, _
   ByVal DimensionTextPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As JoggedDimension
```

### C#

```csharp
JoggedDimension InsertJoggedDimensionCircle(
   Circle Circle,
   System.object CenterPositionOverrideDblArray,
   System.object JogLinePositionDblArray,
   System.object DimensionTextPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertJoggedDimensionCircle(
   Circle : Circle,
   CenterPositionOverrideDblArray : System.Object,
   JogLinePositionDblArray : System.Object,
   DimensionTextPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : JoggedDimension;
```

### Managed Extensions for C++

```
JoggedDimension* InsertJoggedDimensionCircle(
   Circle* Circle,
   System.Object* CenterPositionOverrideDblArray,
   System.Object* JogLinePositionDblArray,
   System.Object* DimensionTextPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
JoggedDimension^ InsertJoggedDimensionCircle(
   Circle^ Circle,
   System.Object^ CenterPositionOverrideDblArray,
   System.Object^ JogLinePositionDblArray,
   System.Object^ DimensionTextPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `Circle`: [Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
- `CenterPositionOverrideDblArray`: Array of three doubles indicating the point where to place the center position override
- `JogLinePositionDblArray`: Array of three doubles indicating the point where to place the jog line
- `DimensionTextPositionDblArray`: Array of three doubles indicating the point where to place the Dimension text
- `DimensionTextOverride`: Text with which to override the default Dimension text

### Return Value

[Jogged Dimension](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertDiameterDimensionArc Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDiameterDimensionArc.html)

## Availability

DraftSight V1R1.2
