---
title: "GetNumDependencies Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetNumDependencies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetNumDependencies.html"
---

# GetNumDependencies Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetNumDependencies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetNumDependencies.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNumDependencies( _
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

value = instance.GetNumDependencies(Traverseflag, Searchflag)
```

### C#

```csharp
System.int GetNumDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

### C++/CLI

```cpp
System.int GetNumDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Traverseflag`:
- `Searchflag`:

## VBA Syntax

See [ModelDoc::GetNumDependencies](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetNumDependencies.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
