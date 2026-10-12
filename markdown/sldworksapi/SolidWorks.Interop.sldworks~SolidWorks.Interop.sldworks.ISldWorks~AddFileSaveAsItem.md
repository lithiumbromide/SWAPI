---
title: "AddFileSaveAsItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddFileSaveAsItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileSaveAsItem.html"
---

# AddFileSaveAsItem Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddFileSaveAsItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddFileSaveAsItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFileSaveAsItem( _
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

value = instance.AddFileSaveAsItem(CallbackFcnAndModule, Description, Type)
```

### C#

```csharp
System.bool AddFileSaveAsItem(
   System.string CallbackFcnAndModule,
   System.string Description,
   System.int Type
)
```

### C++/CLI

```cpp
System.bool AddFileSaveAsItem(
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

See [SldWorks::AddFileSaveAsItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddFileSaveAsItem.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
