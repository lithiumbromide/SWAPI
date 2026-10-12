---
title: "IGetCoordinateSystemXformByName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetCoordinateSystemXformByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetCoordinateSystemXformByName.html"
---

# IGetCoordinateSystemXformByName Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::GetCoordinateSystemTransformByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCoordinateSystemXformByName( _
   ByVal NameIn As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::IGetCoordinateSystemXformByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetCoordinateSystemXformByName.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
