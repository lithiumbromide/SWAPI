---
title: "IGetNext Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext.html"
---

# IGetNext Method (ILoop2)

Gets the next loop in the face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As Loop2
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As Loop2

value = instance.IGetNext()
```

### C#

```csharp
Loop2 IGetNext()
```

### C++/CLI

```cpp
Loop2^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) on the face, or NULL if it is the last loop

## VBA Syntax

See [Loop2::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~Loop2~IGetNext.html).

## Remarks

See [ILoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) accessors for a list of methods and properties that return loops.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
