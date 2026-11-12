---
title: "SetBendState Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetBendState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetBendState.html"
---

# SetBendState Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetBendState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBendState.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBendState( _
   ByVal BendState As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim BendState As System.Integer
Dim value As System.Integer

value = instance.SetBendState(BendState)
```

### C#

```csharp
System.int SetBendState(
   System.int BendState
)
```

### C++/CLI

```cpp
System.int SetBendState(
   System.int BendState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BendState`:

## VBA Syntax

See [ModelDoc::SetBendState](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetBendState.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
