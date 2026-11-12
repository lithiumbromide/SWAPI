---
title: "IGetLoops Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetLoops.html"
---

# IGetLoops Method (IFace2)

Gets all of the loops on this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLoops( _
   ByVal NumberOfLoops As System.Integer _
) As Loop2
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim NumberOfLoops As System.Integer
Dim value As Loop2

value = instance.IGetLoops(NumberOfLoops)
```

### C#

```csharp
Loop2 IGetLoops(
   System.int NumberOfLoops
)
```

### C++/CLI

```cpp
Loop2^ IGetLoops(
   System.int NumberOfLoops
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumberOfLoops`: Number of loops on the face

### Return Value

- in-process, unmanaged C++: Pointer to an array of all of the [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) on the face (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IFace2::GetLoopCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetLoopCount.html) to get NumberOfLoops.

If a face has one or more holes on it, then this method gets a loop for the face and a loop for every hole on the face.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoops.html)
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.html)
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.html)
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.html)
[ILoop2::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
