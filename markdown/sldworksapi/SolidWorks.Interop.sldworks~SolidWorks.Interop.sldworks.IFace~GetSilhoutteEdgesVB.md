---
title: "GetSilhoutteEdgesVB Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "GetSilhoutteEdgesVB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~GetSilhoutteEdgesVB.html"
---

# GetSilhoutteEdgesVB Method (IFace)

Obsolete. Superseded by [IFace2::GetSilhoutteEdgesVB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSilhoutteEdgesVB( _
   ByVal Xroot As System.Double, _
   ByVal Yroot As System.Double, _
   ByVal Zroot As System.Double, _
   ByVal Xnormal As System.Double, _
   ByVal Ynormal As System.Double, _
   ByVal Znormal As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim Xroot As System.Double
Dim Yroot As System.Double
Dim Zroot As System.Double
Dim Xnormal As System.Double
Dim Ynormal As System.Double
Dim Znormal As System.Double
Dim value As System.Object

value = instance.GetSilhoutteEdgesVB(Xroot, Yroot, Zroot, Xnormal, Ynormal, Znormal)
```

### C#

```csharp
System.object GetSilhoutteEdgesVB(
   System.double Xroot,
   System.double Yroot,
   System.double Zroot,
   System.double Xnormal,
   System.double Ynormal,
   System.double Znormal
)
```

### C++/CLI

```cpp
System.Object^ GetSilhoutteEdgesVB(
   System.double Xroot,
   System.double Yroot,
   System.double Zroot,
   System.double Xnormal,
   System.double Ynormal,
   System.double Znormal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xroot`:
- `Yroot`:
- `Zroot`:
- `Xnormal`:
- `Ynormal`:
- `Znormal`:

## VBA Syntax

See [Face::GetSilhoutteEdgesVB](ms-its:sldworksapivb6.chm::/sldworks~Face~GetSilhoutteEdgesVB.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
