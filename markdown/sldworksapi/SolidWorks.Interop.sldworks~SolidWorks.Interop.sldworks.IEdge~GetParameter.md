---
title: "GetParameter Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetParameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetParameter.html"
---

# GetParameter Method (IEdge)

Gets the parameterization of the edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParameter( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.GetParameter(X, Y, Z)
```

### C#

```csharp
System.object GetParameter(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ GetParameter(
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

Array containing parameterization of the edge

## VBA Syntax

See [Edge::GetParameter](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetParameter.html).

## Remarks

This method returns an array of 2 doubles:

- retval[0] - Parametric value of the specified point
- retval[1] - BOOL value; True for success, false for failure

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::IGetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetParameter.html)
