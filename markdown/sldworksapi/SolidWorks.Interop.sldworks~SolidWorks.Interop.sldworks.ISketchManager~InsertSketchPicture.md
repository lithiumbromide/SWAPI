---
title: "InsertSketchPicture Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "InsertSketchPicture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchPicture.html"
---

# InsertSketchPicture Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::InsertSketchPicture2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchPicture2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSketchPicture( _
   ByVal FileName As System.String _
) As SketchPicture
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim FileName As System.String
Dim value As SketchPicture

value = instance.InsertSketchPicture(FileName)
```

### C#

```csharp
SketchPicture InsertSketchPicture(
   System.string FileName
)
```

### C++/CLI

```cpp
SketchPicture^ InsertSketchPicture(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path to image file including file extension

### Return Value

[Picture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture.html)

## VBA Syntax

See [SketchManager::InsertSketchPicture](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~InsertSketchPicture.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
