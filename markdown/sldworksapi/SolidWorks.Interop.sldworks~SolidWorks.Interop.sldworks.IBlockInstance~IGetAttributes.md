---
title: "IGetAttributes Method (IBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "IBlockInstance"
member: "IGetAttributes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~IGetAttributes.html"
---

# IGetAttributes Method (IBlockInstance)

Obsolete. Superseded by [ISketchBlockInstance::IGetAttributes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~IGetAttributes.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAttributes( _
   ByVal NumAttribs As System.Integer _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockInstance
Dim NumAttribs As System.Integer
Dim value As Note

value = instance.IGetAttributes(NumAttribs)
```

### C#

```csharp
Note IGetAttributes(
   System.int NumAttribs
)
```

### C++/CLI

```cpp
Note^ IGetAttributes(
   System.int NumAttribs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumAttribs`:

## VBA Syntax

See [BlockInstance::IGetAttributes](ms-its:sldworksapivb6.chm::/sldworks~BlockInstance~IGetAttributes.html).

## See Also

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.html)
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.html)
