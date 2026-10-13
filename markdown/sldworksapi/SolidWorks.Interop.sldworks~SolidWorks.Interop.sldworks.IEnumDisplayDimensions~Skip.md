---
title: "Skip Method (IEnumDisplayDimensions)"
project: "SOLIDWORKS API Help"
interface: "IEnumDisplayDimensions"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions~Skip.html"
---

# Skip Method (IEnumDisplayDimensions)

Skips the specified number of display dimensions in the display dimensions enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDisplayDimensions
Dim Celt As System.Integer

instance.Skip(Celt)
```

### C#

```csharp
void Skip(
   System.int Celt
)
```

### C++/CLI

```cpp
void Skip(
   System.int Celt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of display dimensions to skip

## VBA Syntax

See [EnumDisplayDimensions::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumDisplayDimensions~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumDisplayDimensions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions.html)
[IEnumDisplayDimensions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions_members.html)
