---
title: "GetDocumentDependenciesCount Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetDocumentDependenciesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependenciesCount.html"
---

# GetDocumentDependenciesCount Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::IGetDocumentDependenciesCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetDocumentDependenciesCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocumentDependenciesCount( _
   ByVal Document As System.String, _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Document As System.String
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.Integer

value = instance.GetDocumentDependenciesCount(Document, Traverseflag, Searchflag)
```

### C#

```csharp
System.int GetDocumentDependenciesCount(
   System.string Document,
   System.int Traverseflag,
   System.int Searchflag
)
```

### C++/CLI

```cpp
System.int GetDocumentDependenciesCount(
   System.String^ Document,
   System.int Traverseflag,
   System.int Searchflag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Document`:
- `Traverseflag`:
- `Searchflag`:

## VBA Syntax

See [SldWorks::GetDocumentDependenciesCount](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetDocumentDependenciesCount.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
