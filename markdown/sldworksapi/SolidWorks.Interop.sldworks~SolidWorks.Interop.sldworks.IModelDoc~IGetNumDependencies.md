---
title: "IGetNumDependencies Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetNumDependencies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetNumDependencies.html"
---

# IGetNumDependencies Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetNumDependencies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetNumDependencies.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNumDependencies( _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.Integer

value = instance.IGetNumDependencies(Traverseflag, Searchflag)
```

### C#

```csharp
System.int IGetNumDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

### C++/CLI

```cpp
System.int IGetNumDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Traverseflag`:
- `Searchflag`:

## VBA Syntax

See [ModelDoc::IGetNumDependencies](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetNumDependencies.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
