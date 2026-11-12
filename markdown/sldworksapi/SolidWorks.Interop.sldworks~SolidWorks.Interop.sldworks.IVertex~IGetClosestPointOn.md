---
title: "IGetClosestPointOn Method (IVertex)"
project: "SOLIDWORKS API Help"
interface: "IVertex"
member: "IGetClosestPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetClosestPointOn.html"
---

# IGetClosestPointOn Method (IVertex)

Gets the closest point on the vertex using the X, Y, Z input point.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVertex
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Double

value = instance.IGetClosestPointOn(X, Y, Z)
```

### C#

```csharp
System.double IGetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.double IGetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X value of the input point
- `Y`: Y value of the input point
- `Z`: Z value of the input point

### Return Value

- in-process, unmanaged C++: Pointer to an array of five doubles representing the X, Y, Z point on the vertex

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html)
[IVertex::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetClosestPointOn.html)
