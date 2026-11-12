---
title: "RemoveInnerLoops Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "RemoveInnerLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveInnerLoops.html"
---

# RemoveInnerLoops Method (IFace2)

Removes the inner loops on this face if the face is from a sheet (surface) body.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveInnerLoops( _
   ByVal NumOfLoops As System.Integer, _
   ByVal InnerLoopsIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim NumOfLoops As System.Integer
Dim InnerLoopsIn As System.Object
Dim value As System.Object

value = instance.RemoveInnerLoops(NumOfLoops, InnerLoopsIn)
```

### C#

```csharp
System.object RemoveInnerLoops(
   System.int NumOfLoops,
   System.object InnerLoopsIn
)
```

### C++/CLI

```cpp
System.Object^ RemoveInnerLoops(
   System.int NumOfLoops,
   System.Object^ InnerLoopsIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfLoops`: Number of loops to remove
- `InnerLoopsIn`: Array of the inner loops to remove

### Return Value

Resulting [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Face2::RemoveInnerLoops](ms-its:sldworksapivb6.chm::/sldworks~Face2~RemoveInnerLoops.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IRemoveInnerLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IRemoveInnerLoops.html)
[IFace2::EnumLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~EnumLoops.html)
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.html)
[IFace2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.html)
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
