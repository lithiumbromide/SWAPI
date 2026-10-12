---
title: "Skip Method (IEnumComponents2)"
project: "SOLIDWORKS API Help"
interface: "IEnumComponents2"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2~Skip.html"
---

# Skip Method (IEnumComponents2)

Skips the specified number of components in the components enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumComponents2
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

- `Celt`: Number of components to skip

## VBA Syntax

See [EnumComponents2::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumComponents2~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumComponents2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2.html)
[IEnumComponents2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2_members.html)
