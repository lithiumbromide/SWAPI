---
title: "IAddProfileLineDLL Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IAddProfileLineDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLineDLL.html"
---

# IAddProfileLineDLL Method (IBody2)

Adds a profile line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileLineDLL( _
   ByRef RootPoint As System.Double, _
   ByRef Direction As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim RootPoint As System.Double
Dim Direction As System.Double
Dim value As Curve

value = instance.IAddProfileLineDLL(RootPoint, Direction)
```

### C#

```csharp
Curve IAddProfileLineDLL(
   ref System.double RootPoint,
   ref System.double Direction
)
```

### C++/CLI

```cpp
Curve^ IAddProfileLineDLL(
   System.double% RootPoint,
   System.double% Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`: Pointer to an array of 3 doubles (x,y,z)
- `Direction`: Pointer to an array of 3 doubles (x,y,z)

### Return Value

Pointer to the profile line [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Body2::IAddProfileLineDLL](ms-its:sldworksapivb6.chm::/sldworks~Body2~IAddProfileLineDLL.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
