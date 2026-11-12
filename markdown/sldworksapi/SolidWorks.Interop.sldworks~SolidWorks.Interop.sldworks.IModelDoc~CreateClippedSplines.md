---
title: "CreateClippedSplines Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateClippedSplines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateClippedSplines.html"
---

# CreateClippedSplines Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateClippedSplines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateClippedSplines.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateClippedSplines( _
   ByVal ParamsIn As System.Object, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ParamsIn As System.Object
Dim X1 As System.Double
Dim Y1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim value As System.Object

value = instance.CreateClippedSplines(ParamsIn, X1, Y1, X2, Y2)
```

### C#

```csharp
System.object CreateClippedSplines(
   System.object ParamsIn,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
)
```

### C++/CLI

```cpp
System.Object^ CreateClippedSplines(
   System.Object^ ParamsIn,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamsIn`:
- `X1`:
- `Y1`:
- `X2`:
- `Y2`:

## VBA Syntax

See [ModelDoc::CreateClippedSplines](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateClippedSplines.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
