---
title: "IRemoveInnerLoops Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IRemoveInnerLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IRemoveInnerLoops.html"
---

# IRemoveInnerLoops Method (IFace2)

Removes the inner loops on this face if the face is from a sheet (surface) body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IRemoveInnerLoops( _
   ByVal NumOfLoops As System.Integer, _
   ByRef InnerLoopsIn As Loop2 _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim NumOfLoops As System.Integer
Dim InnerLoopsIn As Loop2
Dim value As Face2

value = instance.IRemoveInnerLoops(NumOfLoops, InnerLoopsIn)
```

### C#

```csharp
Face2 IRemoveInnerLoops(
   System.int NumOfLoops,
   ref Loop2 InnerLoopsIn
)
```

### C++/CLI

```cpp
Face2^ IRemoveInnerLoops(
   System.int NumOfLoops,
   Loop2^% InnerLoopsIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfLoops`: Number of loops to remove
- `InnerLoopsIn`: Pointer to an array of the inner [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) to be removed

### Return Value

Pointer to the resulting [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Face2::IRemoveInnerLoops](ms-its:sldworksapivb6.chm::/sldworks~Face2~IRemoveInnerLoops.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::RemoveInnerLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveInnerLoops.html)
[IFace2::EnumLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~EnumLoops.html)
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.html)
[IFace2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.html)
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
