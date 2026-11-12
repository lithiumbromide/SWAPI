---
title: "ICreateSheetBodyByFaceExtension Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "ICreateSheetBodyByFaceExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~ICreateSheetBodyByFaceExtension.html"
---

# ICreateSheetBodyByFaceExtension Method (IFace)

Obsolete. Superseded by [IFace2::ICreateSheetBodyByFaceExtension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSheetBodyByFaceExtension( _
   ByRef BoxLowIn As System.Double, _
   ByRef BoxHighIn As System.Double _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim BoxLowIn As System.Double
Dim BoxHighIn As System.Double
Dim value As Body

value = instance.ICreateSheetBodyByFaceExtension(BoxLowIn, BoxHighIn)
```

### C#

```csharp
Body ICreateSheetBodyByFaceExtension(
   ref System.double BoxLowIn,
   ref System.double BoxHighIn
)
```

### C++/CLI

```cpp
Body^ ICreateSheetBodyByFaceExtension(
   System.double% BoxLowIn,
   System.double% BoxHighIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BoxLowIn`:
- `BoxHighIn`:

## VBA Syntax

See [Face::ICreateSheetBodyByFaceExtension](ms-its:sldworksapivb6.chm::/sldworks~Face~ICreateSheetBodyByFaceExtension.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
