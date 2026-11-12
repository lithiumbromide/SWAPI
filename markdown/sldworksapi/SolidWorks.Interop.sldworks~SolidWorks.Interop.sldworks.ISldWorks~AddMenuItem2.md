---
title: "AddMenuItem2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddMenuItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem2.html"
---

# AddMenuItem2 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddMenuItem3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenuItem3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuItem2( _
   ByVal DocumentType As System.Integer, _
   ByVal Cookie As System.Integer, _
   ByVal MenuItem As System.String, _
   ByVal Position As System.Integer, _
   ByVal MenuCallback As System.String, _
   ByVal MenuEnableMethod As System.String, _
   ByVal HintString As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocumentType As System.Integer
Dim Cookie As System.Integer
Dim MenuItem As System.String
Dim Position As System.Integer
Dim MenuCallback As System.String
Dim MenuEnableMethod As System.String
Dim HintString As System.String
Dim value As System.Boolean

value = instance.AddMenuItem2(DocumentType, Cookie, MenuItem, Position, MenuCallback, MenuEnableMethod, HintString)
```

### C#

```csharp
System.bool AddMenuItem2(
   System.int DocumentType,
   System.int Cookie,
   System.string MenuItem,
   System.int Position,
   System.string MenuCallback,
   System.string MenuEnableMethod,
   System.string HintString
)
```

### C++/CLI

```cpp
System.bool AddMenuItem2(
   System.int DocumentType,
   System.int Cookie,
   System.String^ MenuItem,
   System.int Position,
   System.String^ MenuCallback,
   System.String^ MenuEnableMethod,
   System.String^ HintString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentType`:
- `Cookie`:
- `MenuItem`:
- `Position`:
- `MenuCallback`:
- `MenuEnableMethod`:
- `HintString`:

## VBA Syntax

See [SldWorks::AddMenuItem2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddMenuItem2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
