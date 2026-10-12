---
title: "AddProfileLine Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "AddProfileLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileLine.html"
---

# AddProfileLine Method (IBody2)

Creates a line profile curve and returns a pointer to that curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddProfileLine( _
   ByVal RootPoint As System.Object, _
   ByVal Direction As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim RootPoint As System.Object
Dim Direction As System.Object
Dim value As System.Object

value = instance.AddProfileLine(RootPoint, Direction)
```

### C#

```csharp
System.object AddProfileLine(
   System.object RootPoint,
   System.object Direction
)
```

### C++/CLI

```cpp
System.Object^ AddProfileLine(
   System.Object^ RootPoint,
   System.Object^ Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`: Array of 3 doubles (x,y,z)
- `Direction`: Array of 3 doubles (x,y,z)

### Return Value

Object for the line profile curve

## VBA Syntax

See [Body2::AddProfileLine](ms-its:sldworksapivb6.chm::/sldworks~Body2~AddProfileLine.html).

## Remarks

You can use this method with [IBody2::CreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateRevolutionSurface.html) to generate a cylindrical surface of revolution or with [IBody2::CreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateExtrusionSurface.html) to generate a tabulated cylinder.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IAddProfileLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLine.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
