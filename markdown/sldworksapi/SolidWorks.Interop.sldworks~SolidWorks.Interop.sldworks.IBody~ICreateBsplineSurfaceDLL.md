---
title: "ICreateBsplineSurfaceDLL Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateBsplineSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBsplineSurfaceDLL.html"
---

# ICreateBsplineSurfaceDLL Method (IBody)

Obsolete. Superseded by [IBody2::ICreateBsplineSurfaceDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBsplineSurfaceDLL.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBsplineSurfaceDLL( _
   ByRef Properties As System.Integer, _
   ByRef UKnotArray As System.Double, _
   ByRef VKnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Properties As System.Integer
Dim UKnotArray As System.Double
Dim VKnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Surface

value = instance.ICreateBsplineSurfaceDLL(Properties, UKnotArray, VKnotArray, ControlPointCoordArray)
```

### C#

```csharp
Surface ICreateBsplineSurfaceDLL(
   ref System.int Properties,
   ref System.double UKnotArray,
   ref System.double VKnotArray,
   ref System.double ControlPointCoordArray
)
```

### C++/CLI

```cpp
Surface^ ICreateBsplineSurfaceDLL(
   System.int% Properties,
   System.double% UKnotArray,
   System.double% VKnotArray,
   System.double% ControlPointCoordArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Properties`:
- `UKnotArray`:
- `VKnotArray`:
- `ControlPointCoordArray`:

## VBA Syntax

See [Body::ICreateBsplineSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateBsplineSurfaceDLL.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
