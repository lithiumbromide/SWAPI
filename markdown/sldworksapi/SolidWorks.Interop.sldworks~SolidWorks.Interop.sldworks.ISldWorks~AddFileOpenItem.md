---
title: "AddFileOpenItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddFileOpenItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileOpenItem.html"
---

# AddFileOpenItem Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddFileOpenItem3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddFileOpenItem3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFileOpenItem( _
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

value = instance.AddFileOpenItem(CallbackFcnAndModule, Description)
```

### C#

```csharp
System.bool AddFileOpenItem(
   System.string CallbackFcnAndModule,
   System.string Description
)
```

### C++/CLI

```cpp
System.bool AddFileOpenItem(
   System.String^ CallbackFcnAndModule,
   System.String^ Description
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CallbackFcnAndModule`:
- `Description`:

## VBA Syntax

See [SldWorks::AddFileOpenItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddFileOpenItem.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
