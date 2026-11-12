---
title: "IGetStandardViewRotation Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetStandardViewRotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetStandardViewRotation.html"
---

# IGetStandardViewRotation Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetStandardViewRotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetStandardViewRotation.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetStandardViewRotation( _
   ByVal ViewId As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ViewId As System.Integer
Dim value As System.Double

value = instance.IGetStandardViewRotation(ViewId)
```

### C#

```csharp
System.double IGetStandardViewRotation(
   System.int ViewId
)
```

### C++/CLI

```cpp
System.double IGetStandardViewRotation(
   System.int ViewId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewId`:

## VBA Syntax

See [ModelDoc::IGetStandardViewRotation](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetStandardViewRotation.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
