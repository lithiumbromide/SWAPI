---
title: "CreatePlaneFixed Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreatePlaneFixed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneFixed.html"
---

# CreatePlaneFixed Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreatePlaneFixed2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePlaneFixed2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlaneFixed( _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal UseGlobal As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1 As System.Object
Dim P2 As System.Object
Dim P3 As System.Object
Dim UseGlobal As System.Boolean
Dim value As System.Boolean

value = instance.CreatePlaneFixed(P1, P2, P3, UseGlobal)
```

### C#

```csharp
System.bool CreatePlaneFixed(
   System.object P1,
   System.object P2,
   System.object P3,
   System.bool UseGlobal
)
```

### C++/CLI

```cpp
System.bool CreatePlaneFixed(
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
   System.bool UseGlobal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `P2`:
- `P3`:
- `UseGlobal`:

## VBA Syntax

See [ModelDoc2::CreatePlaneFixed](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreatePlaneFixed.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
