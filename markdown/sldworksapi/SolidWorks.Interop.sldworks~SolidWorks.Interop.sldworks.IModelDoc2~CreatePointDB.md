---
title: "CreatePointDB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreatePointDB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePointDB.html"
---

# CreatePointDB Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreatePoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePoint2.html) and [IModelDoc2::ICreatePoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePoint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePointDB( _
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

value = instance.CreatePointDB(X, Y, Z)
```

### C#

```csharp
System.bool CreatePointDB(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool CreatePointDB(
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

See [ModelDoc2::CreatePointDB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreatePointDB.html).

## Remarks

**IMPORTANT:** This method ignores the z value when adding a point to a 3D sketch. Thus, update your code to use the more current method, IModelDoc2::CreatePoint2 or IModelDoc2::ICreatePoint2.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
