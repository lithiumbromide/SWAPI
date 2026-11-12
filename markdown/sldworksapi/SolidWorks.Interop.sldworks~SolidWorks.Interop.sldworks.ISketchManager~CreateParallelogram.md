---
title: "CreateParallelogram Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateParallelogram"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateParallelogram.html"
---

# CreateParallelogram Method (ISketchManager)

Creates a parallelogram.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateParallelogram( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal X3 As System.Double, _
   ByVal Y3 As System.Double, _
   ByVal Z3 As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim X3 As System.Double
Dim Y3 As System.Double
Dim Z3 As System.Double
Dim value As System.Object

value = instance.CreateParallelogram(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3)
```

### C#

```csharp
System.object CreateParallelogram(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3
)
```

### C++/CLI

```cpp
System.Object^ CreateParallelogram(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`: X coordinate for point 1
- `Y1`: coordinate for point 1
- `Z1`: Z coordinate for point 1
- `X2`: X coordinate for point 2
- `Y2`: Y coordinate for point 2
- `Z2`: Z coordinate for point 2
- `X3`: X coordinate for point 3
- `Y3`: Y coordinate for point 3
- `Z3`: Z coordinate for point 3

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the parallelogram

## VBA Syntax

See [SketchManager::CreateParallelogram](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateParallelogram.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
