---
title: "Clone Method (IEnumComponents2)"
project: "SOLIDWORKS API Help"
interface: "IEnumComponents2"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2~Clone.html"
---

# Clone Method (IEnumComponents2)

Clones the components enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumComponents2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumComponents2
Dim Ppenum As EnumComponents2

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumComponents2 Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumComponents2^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the cloned [components enumeraton](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumComponents2.html)

## VBA Syntax

See [EnumComponents2::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumComponents2~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumComponents2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2.html)
[IEnumComponents2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
