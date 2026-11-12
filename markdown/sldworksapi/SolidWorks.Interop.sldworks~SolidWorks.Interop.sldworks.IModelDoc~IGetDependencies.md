---
title: "IGetDependencies Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetDependencies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetDependencies.html"
---

# IGetDependencies Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetDependencies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetDependencies.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDependencies( _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.String

value = instance.IGetDependencies(Traverseflag, Searchflag)
```

### C#

```csharp
System.string IGetDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

### C++/CLI

```cpp
System.String^ IGetDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Traverseflag`:
- `Searchflag`:

## VBA Syntax

See [ModelDoc::IGetDependencies](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetDependencies.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
