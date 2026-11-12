---
title: "RemoveFileSaveAsItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveFileSaveAsItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileSaveAsItem.html"
---

# RemoveFileSaveAsItem Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::RemoveFileSaveAsItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveFileSaveAsItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveFileSaveAsItem( _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal Description As System.String, _
   ByVal Type As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CallbackFcnAndModule As System.String
Dim Description As System.String
Dim Type As System.Integer
Dim value As System.Boolean

value = instance.RemoveFileSaveAsItem(CallbackFcnAndModule, Description, Type)
```

### C#

```csharp
System.bool RemoveFileSaveAsItem(
   System.string CallbackFcnAndModule,
   System.string Description,
   System.int Type
)
```

### C++/CLI

```cpp
System.bool RemoveFileSaveAsItem(
   System.String^ CallbackFcnAndModule,
   System.String^ Description,
   System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CallbackFcnAndModule`:
- `Description`:
- `Type`:

## VBA Syntax

See [SldWorks::RemoveFileSaveAsItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveFileSaveAsItem.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
