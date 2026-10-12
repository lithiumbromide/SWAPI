---
title: "CreateSheetBodyByFaceExtension Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "CreateSheetBodyByFaceExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~CreateSheetBodyByFaceExtension.html"
---

# CreateSheetBodyByFaceExtension Method (IFace)

Obsolete. Superseded by [IFace2:: CreateSheetbodyByFaceExtension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSheetBodyByFaceExtension( _
   ByVal BoxLowIn As System.Object, _
   ByVal BoxHighIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim BoxLowIn As System.Object
Dim BoxHighIn As System.Object
Dim value As System.Object

value = instance.CreateSheetBodyByFaceExtension(BoxLowIn, BoxHighIn)
```

### C#

```csharp
System.object CreateSheetBodyByFaceExtension(
   System.object BoxLowIn,
   System.object BoxHighIn
)
```

### C++/CLI

```cpp
System.Object^ CreateSheetBodyByFaceExtension(
   System.Object^ BoxLowIn,
   System.Object^ BoxHighIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BoxLowIn`:
- `BoxHighIn`:

## VBA Syntax

See [Face::CreateSheetBodyByFaceExtension](ms-its:sldworksapivb6.chm::/sldworks~Face~CreateSheetBodyByFaceExtension.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
