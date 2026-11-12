---
title: "CreateArc Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArc.html"
---

# CreateArc Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreateArc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateArc2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateArc( _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal Dir As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Object
Dim P2 As System.Object
Dim P3 As System.Object
Dim Dir As System.Short
Dim value As System.Boolean

value = instance.CreateArc(P1, P2, P3, Dir)
```

### C#

```csharp
System.bool CreateArc(
   System.object P1,
   System.object P2,
   System.object P3,
   System.short Dir
)
```

### C++/CLI

```cpp
System.bool CreateArc(
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
   System.short Dir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `P2`:
- `P3`:
- `Dir`:

## VBA Syntax

See [ModelDoc2::CreateArc](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateArc.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
