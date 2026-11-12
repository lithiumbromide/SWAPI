---
title: "Parameter Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "Parameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~Parameter.html"
---

# Parameter Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::Parameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Parameter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Parameter( _
   ByVal StringIn As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim StringIn As System.String
Dim value As System.Object

value = instance.Parameter(StringIn)
```

### C#

```csharp
System.object Parameter(
   System.string StringIn
)
```

### C++/CLI

```cpp
System.Object^ Parameter(
   System.String^ StringIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StringIn`:

## VBA Syntax

See [ModelDoc::Parameter](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~Parameter.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
