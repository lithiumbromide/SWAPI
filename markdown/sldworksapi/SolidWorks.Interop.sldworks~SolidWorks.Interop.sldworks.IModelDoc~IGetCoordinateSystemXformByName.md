---
title: "IGetCoordinateSystemXformByName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetCoordinateSystemXformByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetCoordinateSystemXformByName.html"
---

# IGetCoordinateSystemXformByName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetCoordinateSystemXformByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetCoordinateSystemXformByName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCoordinateSystemXformByName( _
   ByVal NameIn As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim NameIn As System.String
Dim value As System.Double

value = instance.IGetCoordinateSystemXformByName(NameIn)
```

### C#

```csharp
System.double IGetCoordinateSystemXformByName(
   System.string NameIn
)
```

### C++/CLI

```cpp
System.double IGetCoordinateSystemXformByName(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`:

## VBA Syntax

See [ModelDoc::IGetCoordinateSystemXformByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetCoordinateSystemXformByName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
