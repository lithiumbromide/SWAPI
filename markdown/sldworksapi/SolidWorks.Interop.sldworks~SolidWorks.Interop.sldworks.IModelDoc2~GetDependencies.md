---
title: "GetDependencies Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetDependencies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDependencies.html"
---

# GetDependencies Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::GetDependencies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetDependencies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDependencies( _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.Object

value = instance.GetDependencies(Traverseflag, Searchflag)
```

### C#

```csharp
System.object GetDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

### C++/CLI

```cpp
System.Object^ GetDependencies(
   System.int Traverseflag,
   System.int Searchflag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Traverseflag`:
- `Searchflag`:

## VBA Syntax

See [ModelDoc2::GetDependencies](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetDependencies.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
