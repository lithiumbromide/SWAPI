---
title: "IGetDocumentDependencies Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetDocumentDependencies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies.html"
---

# IGetDocumentDependencies Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::IGetDocumentDependencies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDocumentDependencies( _
   ByVal Document As System.String, _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Document As System.String
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.String

value = instance.IGetDocumentDependencies(Document, Traverseflag, Searchflag)
```

### C#

```csharp
System.string IGetDocumentDependencies(
   System.string Document,
   System.int Traverseflag,
   System.int Searchflag
)
```

### C++/CLI

```cpp
System.String^ IGetDocumentDependencies(
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

See [SldWorks::IGetDocumentDependencies](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetDocumentDependencies.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
