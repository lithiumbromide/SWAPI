---
title: "IGetDependencies2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetDependencies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetDependencies2.html"
---

# IGetDependencies2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetDependencies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetDependencies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDependencies2( _
   ByVal Traverseflag As System.Boolean, _
   ByVal Searchflag As System.Boolean, _
   ByVal AddReadOnlyInfo As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Traverseflag As System.Boolean
Dim Searchflag As System.Boolean
Dim AddReadOnlyInfo As System.Boolean
Dim value As System.String

value = instance.IGetDependencies2(Traverseflag, Searchflag, AddReadOnlyInfo)
```

### C#

```csharp
System.string IGetDependencies2(
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

### C++/CLI

```cpp
System.String^ IGetDependencies2(
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Traverseflag`:
- `Searchflag`:
- `AddReadOnlyInfo`:

## VBA Syntax

See [ModelDoc::IGetDependencies2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetDependencies2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
