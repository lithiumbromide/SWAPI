---
title: "IAddHorizontalDimension2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IAddHorizontalDimension2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IAddHorizontalDimension2.html"
---

# IAddHorizontalDimension2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IAddHorizontalDimension2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IAddHorizontalDimension2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddHorizontalDimension2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As DisplayDimension

value = instance.IAddHorizontalDimension2(X, Y, Z)
```

### C#

```csharp
DisplayDimension IAddHorizontalDimension2(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
DisplayDimension^ IAddHorizontalDimension2(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [ModelDoc::IAddHorizontalDimension2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IAddHorizontalDimension2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
