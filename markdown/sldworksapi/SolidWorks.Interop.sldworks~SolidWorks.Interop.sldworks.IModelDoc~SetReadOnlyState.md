---
title: "SetReadOnlyState Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetReadOnlyState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetReadOnlyState.html"
---

# SetReadOnlyState Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetReadOnlyState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetReadOnlyState.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetReadOnlyState( _
   ByVal SetReadOnly As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim SetReadOnly As System.Boolean
Dim value As System.Boolean

value = instance.SetReadOnlyState(SetReadOnly)
```

### C#

```csharp
System.bool SetReadOnlyState(
   System.bool SetReadOnly
)
```

### C++/CLI

```cpp
System.bool SetReadOnlyState(
   System.bool SetReadOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SetReadOnly`:

## VBA Syntax

See [ModelDoc::SetReadOnlyState](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetReadOnlyState.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
