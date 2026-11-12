---
title: "IGetParameter Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "IGetParameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetParameter.html"
---

# IGetParameter Method (IEdge)

Gets the parameterization of the edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetParameter( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Double

value = instance.IGetParameter(X, Y, Z)
```

### C#

```csharp
System.double IGetParameter(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.double IGetParameter(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X value
- `Y`: Y value
- `Z`: Z value

### Return Value

Pointer to an array of doubles (see **Remarks**)

## VBA Syntax

See [Edge::IGetParameter](ms-its:sldworksapivb6.chm::/sldworks~Edge~IGetParameter.html).

## Remarks

This method returns an array of 2 doubles:

- retval[0] - Parametric value of the specified point
- retval[1] - BOOL value; True for success, false for failure

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetParameter.html)
