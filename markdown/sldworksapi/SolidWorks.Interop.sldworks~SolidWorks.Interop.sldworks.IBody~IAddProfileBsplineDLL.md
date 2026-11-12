---
title: "IAddProfileBsplineDLL Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IAddProfileBsplineDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileBsplineDLL.html"
---

# IAddProfileBsplineDLL Method (IBody)

Obsolete. Superseded by [IBody2::IAddProfileBsplineDLL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddProfileBsplineDLL.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileBsplineDLL( _
   ByRef Properties As System.Integer, _
   ByRef KnotArray As System.Double, _
   ByRef ControlPointCoordArray As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Properties As System.Integer
Dim KnotArray As System.Double
Dim ControlPointCoordArray As System.Double
Dim value As Curve

value = instance.IAddProfileBsplineDLL(Properties, KnotArray, ControlPointCoordArray)
```

### C#

```csharp
Curve IAddProfileBsplineDLL(
   ref System.int Properties,
   ref System.double KnotArray,
   ref System.double ControlPointCoordArray
)
```

### C++/CLI

```cpp
Curve^ IAddProfileBsplineDLL(
   System.int% Properties,
   System.double% KnotArray,
   System.double% ControlPointCoordArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Properties`:
- `KnotArray`:
- `ControlPointCoordArray`:

## VBA Syntax

See [Body::IAddProfileBsplineDLL](ms-its:sldworksapivb6.chm::/sldworks~Body~IAddProfileBsplineDLL.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
