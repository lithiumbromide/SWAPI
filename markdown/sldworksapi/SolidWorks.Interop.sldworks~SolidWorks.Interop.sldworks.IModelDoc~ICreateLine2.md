---
title: "ICreateLine2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateLine2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateLine2.html"
---

# ICreateLine2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateLine2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateLine2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateLine2( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim P1x As System.Double
Dim P1y As System.Double
Dim P1z As System.Double
Dim P2x As System.Double
Dim P2y As System.Double
Dim P2z As System.Double
Dim value As SketchSegment

value = instance.ICreateLine2(P1x, P1y, P1z, P2x, P2y, P2z)
```

### C#

```csharp
SketchSegment ICreateLine2(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z
)
```

### C++/CLI

```cpp
SketchSegment^ ICreateLine2(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1x`:
- `P1y`:
- `P1z`:
- `P2x`:
- `P2y`:
- `P2z`:

## VBA Syntax

See [ModelDoc::ICreateLine2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateLine2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
