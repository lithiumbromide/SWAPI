---
title: "CreatePlaneFixed Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreatePlaneFixed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreatePlaneFixed.html"
---

# CreatePlaneFixed Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreatePlaneFixed](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePlaneFixed.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::CreatePlaneFixed](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreatePlaneFixed.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
