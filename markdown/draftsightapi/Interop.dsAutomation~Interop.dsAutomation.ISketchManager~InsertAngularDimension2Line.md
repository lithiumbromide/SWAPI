---
title: "InsertAngularDimension2Line Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertAngularDimension2Line"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAngularDimension2Line.html"
---

# InsertAngularDimension2Line Method (ISketchManager)

Inserts an angular Dimension formed by two lines.

## Syntax

### Visual Basic

```vb
Function InsertAngularDimension2Line( _
   ByVal Line1 As Line, _
   ByVal Line2 As Line, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As AngularDimension
```

### C#

```csharp
AngularDimension InsertAngularDimension2Line(
   Line Line1,
   Line Line2,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertAngularDimension2Line(
   Line1 : Line,
   Line2 : Line,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : AngularDimension;
```

### Managed Extensions for C++

```
AngularDimension* InsertAngularDimension2Line(
   Line* Line1,
   Line* Line2,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
AngularDimension^ InsertAngularDimension2Line(
   Line^ Line1,
   Line^ Line2,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `Line1`: First [line](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
- `Line2`: Second [line](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
- `DimensionPositionDblArray`: Array of three doubles indicating the point where to place the angular Dimension
- `DimensionTextOverride`: Text with which to override the default Dimension text

### Return Value

[Angular dimension](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension.html)

## Examples

[Create Angular Dimensions (C#)](Create_Angular_Dimensions_Example_CSharp.htm)
[Create Angular Dimensions (VB.NET)](Create_Angular_Dimensions_Example_VBNET.htm)
[Create Angular Dimensions (VBA)](Create_Angular_Dimensions_Example_VBA.htm)
[Insert Lines and Angular Dimension (JavaScript)](Insert_Lines_and_Angular_Dimension_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertAngularDimension3Point Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAngularDimension3Point.html)
[ISketchManager::InsertAngularDimensionArc Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAngularDimensionArc.html)

## Availability

DraftSight V1R1.2
