---
title: "GetCoordinateSystemXformByName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetCoordinateSystemXformByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetCoordinateSystemXformByName.html"
---

# GetCoordinateSystemXformByName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetCoordinateSystemXformByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetCoordinateSystemXformByName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoordinateSystemXformByName( _
   ByVal NameIn As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
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

See [ModelDoc::GetCoordinateSystemXformByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetCoordinateSystemXformByName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
