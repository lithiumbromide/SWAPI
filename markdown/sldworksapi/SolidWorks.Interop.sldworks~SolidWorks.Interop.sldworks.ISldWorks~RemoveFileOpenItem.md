---
title: "RemoveFileOpenItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveFileOpenItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileOpenItem.html"
---

# RemoveFileOpenItem Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::RemoveFileOpenItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveFileOpenItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveFileOpenItem( _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal Description As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CallbackFcnAndModule As System.String
Dim Description As System.String
Dim value As System.Boolean

value = instance.RemoveFileOpenItem(CallbackFcnAndModule, Description)
```

### C#

```csharp
System.bool RemoveFileOpenItem(
   System.string CallbackFcnAndModule,
   System.string Description
)
```

### C++/CLI

```cpp
System.bool RemoveFileOpenItem(
   System.String^ CallbackFcnAndModule,
   System.String^ Description
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CallbackFcnAndModule`:
- `Description`:

## VBA Syntax

See [SldWorks::RemoveFileOpenItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveFileOpenItem.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
