---
title: "Clone Method (IEnumSketchHatches)"
project: "SOLIDWORKS API Help"
interface: "IEnumSketchHatches"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches~Clone.html"
---

# Clone Method (IEnumSketchHatches)

Clones the sketch hatches enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumSketchHatches _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumSketchHatches
Dim Ppenum As EnumSketchHatches

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumSketchHatches Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumSketchHatches^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the cloned sketch hatches enumeration

## VBA Syntax

See [EnumSketchHatches::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumSketchHatches~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumSketchHatches Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches.html)
[IEnumSketchHatches Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
