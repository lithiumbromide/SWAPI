---
title: "GetCoordinateSystemXformByName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetCoordinateSystemXformByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCoordinateSystemXformByName.html"
---

# GetCoordinateSystemXformByName Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::GetCoordinateSystemTransformByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoordinateSystemXformByName( _
   ByVal NameIn As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim NameIn As System.String
Dim value As System.Object

value = instance.GetCoordinateSystemXformByName(NameIn)
```

### C#

```csharp
System.object GetCoordinateSystemXformByName(
   System.string NameIn
)
```

### C++/CLI

```cpp
System.Object^ GetCoordinateSystemXformByName(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`:

## VBA Syntax

See [ModelDoc2::GetCoordinateSystemXformByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetCoordinateSystemXformByName.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
