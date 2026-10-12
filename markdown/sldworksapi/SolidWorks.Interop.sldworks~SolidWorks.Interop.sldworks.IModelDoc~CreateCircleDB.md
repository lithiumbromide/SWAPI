---
title: "CreateCircleDB Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateCircleDB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCircleDB.html"
---

# CreateCircleDB Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateCircleDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircleDB.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCircleDB( _
   ByVal Cx As System.Double, _
   ByVal Cy As System.Double, _
   ByVal Cz As System.Double, _
   ByVal Radius As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Cx As System.Double
Dim Cy As System.Double
Dim Cz As System.Double
Dim Radius As System.Double
Dim value As System.Boolean

value = instance.CreateCircleDB(Cx, Cy, Cz, Radius)
```

### C#

```csharp
System.bool CreateCircleDB(
   System.double Cx,
   System.double Cy,
   System.double Cz,
   System.double Radius
)
```

### C++/CLI

```cpp
System.bool CreateCircleDB(
   System.double Cx,
   System.double Cy,
   System.double Cz,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cx`:
- `Cy`:
- `Cz`:
- `Radius`:

## VBA Syntax

See [ModelDoc::CreateCircleDB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateCircleDB.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
