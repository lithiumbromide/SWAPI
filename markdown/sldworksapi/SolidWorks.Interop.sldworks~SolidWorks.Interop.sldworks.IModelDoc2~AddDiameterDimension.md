---
title: "AddDiameterDimension Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddDiameterDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDiameterDimension.html"
---

# AddDiameterDimension Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::AddDiameterDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddDiameterDimension2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDiameterDimension( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.AddDiameterDimension(X, Y, Z)
```

### C#

```csharp
System.bool AddDiameterDimension(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool AddDiameterDimension(
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

See [ModelDoc2::AddDiameterDimension](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddDiameterDimension.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
