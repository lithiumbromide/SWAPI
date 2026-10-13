---
title: "IGetCustomInfoNames2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetCustomInfoNames2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetCustomInfoNames2.html"
---

# IGetCustomInfoNames2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetCustomInfoNames2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetCustomInfoNames2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCustomInfoNames2( _
   ByVal Configuration As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Configuration As System.String
Dim value As System.String

value = instance.IGetCustomInfoNames2(Configuration)
```

### C#

```csharp
System.string IGetCustomInfoNames2(
   System.string Configuration
)
```

### C++/CLI

```cpp
System.String^ IGetCustomInfoNames2(
   System.String^ Configuration
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Configuration`:

## VBA Syntax

See [ModelDoc::IGetCustomInfoNames2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetCustomInfoNames2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
