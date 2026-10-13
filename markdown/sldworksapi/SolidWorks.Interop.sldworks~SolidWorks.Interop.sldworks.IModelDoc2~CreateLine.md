---
title: "CreateLine Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateLine.html"
---

# CreateLine Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreateLine2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateLine2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateLine( _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Object
Dim P2 As System.Object
Dim value As System.Boolean

value = instance.CreateLine(P1, P2)
```

### C#

```csharp
System.bool CreateLine(
   System.object P1,
   System.object P2
)
```

### C++/CLI

```cpp
System.bool CreateLine(
   System.Object^ P1,
   System.Object^ P2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `P2`:

## VBA Syntax

See [ModelDoc2::CreateLine](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateLine.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
