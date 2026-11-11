---
title: "InsertTolerance Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertTolerance"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertTolerance.html"
---

# InsertTolerance Method (ISketchManager)

Inserts a geometric Tolerance.

## Syntax

### Visual Basic

```vb
Function InsertTolerance( _
   ByVal TolerancePositionDblArray As System.Object, _
   ByVal TextString As System.String _
) As Tolerance
```

### C#

```csharp
Tolerance InsertTolerance(
   System.object TolerancePositionDblArray,
   System.string TextString
)
```

### JScript

```
function InsertTolerance(
   TolerancePositionDblArray : System.Object,
   TextString : System.String
) : Tolerance;
```

### Managed Extensions for C++

```
Tolerance* InsertTolerance(
   System.Object* TolerancePositionDblArray,
   System.string* TextString
)
```

### C++/CLI

```cpp
Tolerance^ InsertTolerance(
   System.Object^ TolerancePositionDblArray,
   System.String^ TextString
)
```

### Parameters

- `TolerancePositionDblArray`: Array of three doubles indicating the point where to place the Tolerance
- `TextString`: Datum identifier

### Return Value

[Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)

## Examples

[Create Aligned Linear and Ordinate Dimensions (C#)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_CSharp.htm)
[Create Aligned Linear and Ordinate Dimensions (VB.NET)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBNET.htm)
[Create Aligned Linear and Ordinate Dimensions (VBA)](Create_Aligned_Linear_And_Ordinate_Dimensions_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.2
