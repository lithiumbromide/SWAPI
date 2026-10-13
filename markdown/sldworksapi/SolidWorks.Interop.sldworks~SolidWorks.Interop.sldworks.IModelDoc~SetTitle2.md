---
title: "SetTitle2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetTitle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetTitle2.html"
---

# SetTitle2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetTitle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetTitle2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTitle2( _
   ByVal NewTitle As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim NewTitle As System.String
Dim value As System.Boolean

value = instance.SetTitle2(NewTitle)
```

### C#

```csharp
System.bool SetTitle2(
   System.string NewTitle
)
```

### C++/CLI

```cpp
System.bool SetTitle2(
   System.String^ NewTitle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewTitle`:

## VBA Syntax

See [ModelDoc::SetTitle2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetTitle2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
