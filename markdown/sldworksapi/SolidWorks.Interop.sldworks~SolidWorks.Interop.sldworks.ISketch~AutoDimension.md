---
title: "AutoDimension Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "AutoDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~AutoDimension.html"
---

# AutoDimension Method (ISketch)

Obsolete. Superseded by [ISketch::AutoDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~AutoDimension2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AutoDimension( _
   ByVal EntitiesToDimension As System.Integer, _
   ByVal HorizontalScheme As System.Integer, _
   ByVal HorizontalPlacement As System.Integer, _
   ByVal VerticalScheme As System.Integer, _
   ByVal VerticalPlacement As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim EntitiesToDimension As System.Integer
Dim HorizontalScheme As System.Integer
Dim HorizontalPlacement As System.Integer
Dim VerticalScheme As System.Integer
Dim VerticalPlacement As System.Integer
Dim value As System.Integer

value = instance.AutoDimension(EntitiesToDimension, HorizontalScheme, HorizontalPlacement, VerticalScheme, VerticalPlacement)
```

### C#

```csharp
System.int AutoDimension(
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
)
```

### C++/CLI

```cpp
System.int AutoDimension(
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntitiesToDimension`:
- `HorizontalScheme`:
- `HorizontalPlacement`:
- `VerticalScheme`:
- `VerticalPlacement`:

## VBA Syntax

See [Sketch::AutoDimension](ms-its:sldworksapivb6.chm::/sldworks~Sketch~AutoDimension.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
