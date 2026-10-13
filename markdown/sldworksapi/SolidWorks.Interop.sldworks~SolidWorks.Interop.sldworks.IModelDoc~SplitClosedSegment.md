---
title: "SplitClosedSegment Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SplitClosedSegment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SplitClosedSegment.html"
---

# SplitClosedSegment Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SplitClosedSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SplitClosedSegment.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SplitClosedSegment( _
   ByVal X0 As System.Double, _
   ByVal Y0 As System.Double, _
   ByVal Z0 As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim X0 As System.Double
Dim Y0 As System.Double
Dim Z0 As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double

instance.SplitClosedSegment(X0, Y0, Z0, X1, Y1, Z1)
```

### C#

```csharp
void SplitClosedSegment(
   System.double X0,
   System.double Y0,
   System.double Z0,
   System.double X1,
   System.double Y1,
   System.double Z1
)
```

### C++/CLI

```cpp
void SplitClosedSegment(
   System.double X0,
   System.double Y0,
   System.double Z0,
   System.double X1,
   System.double Y1,
   System.double Z1
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X0`:
- `Y0`:
- `Z0`:
- `X1`:
- `Y1`:
- `Z1`:

## VBA Syntax

See [ModelDoc::SplitClosedSegment](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SplitClosedSegment.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
