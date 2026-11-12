---
title: "CreateLineDB Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateLineDB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateLineDB.html"
---

# CreateLineDB Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateLineDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateLineDB.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateLineDB( _
   ByVal Sx As System.Double, _
   ByVal Sy As System.Double, _
   ByVal Sz As System.Double, _
   ByVal Ex As System.Double, _
   ByVal Ey As System.Double, _
   ByVal Ez As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Sx As System.Double
Dim Sy As System.Double
Dim Sz As System.Double
Dim Ex As System.Double
Dim Ey As System.Double
Dim Ez As System.Double
Dim value As System.Boolean

value = instance.CreateLineDB(Sx, Sy, Sz, Ex, Ey, Ez)
```

### C#

```csharp
System.bool CreateLineDB(
   System.double Sx,
   System.double Sy,
   System.double Sz,
   System.double Ex,
   System.double Ey,
   System.double Ez
)
```

### C++/CLI

```cpp
System.bool CreateLineDB(
   System.double Sx,
   System.double Sy,
   System.double Sz,
   System.double Ex,
   System.double Ey,
   System.double Ez
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sx`:
- `Sy`:
- `Sz`:
- `Ex`:
- `Ey`:
- `Ez`:

## VBA Syntax

See [ModelDoc::CreateLineDB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateLineDB.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
