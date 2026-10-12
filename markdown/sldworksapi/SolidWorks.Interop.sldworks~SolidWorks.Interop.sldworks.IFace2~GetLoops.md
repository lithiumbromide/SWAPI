---
title: "GetLoops Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoops.html"
---

# GetLoops Method (IFace2)

Gets all of the loops on this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLoops() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetLoops()
```

### C#

```csharp
System.object GetLoops()
```

### C++/CLI

```cpp
System.Object^ GetLoops();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of all of the [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) on the face (see **Remarks**)

## VBA Syntax

See [Face2::GetLoops](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetLoops.html).

## Remarks

If a face has one or more holes on it, then this method gets the one loop for the face and a loop for every hole on the face.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IGetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetLoops.html)
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.html)
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.html)
[IFace2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.html)
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.html)
[ILoop2::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
