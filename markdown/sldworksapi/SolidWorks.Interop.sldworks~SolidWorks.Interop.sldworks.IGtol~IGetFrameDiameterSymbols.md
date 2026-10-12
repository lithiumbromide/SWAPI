---
title: "IGetFrameDiameterSymbols Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetFrameDiameterSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameDiameterSymbols.html"
---

# IGetFrameDiameterSymbols Method (IGtol)

Gets whether diameter symbols are displayed for the specified frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFrameDiameterSymbols( _
   ByVal FrameNumber As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Short
Dim value As System.Boolean

value = instance.IGetFrameDiameterSymbols(FrameNumber)
```

### C#

```csharp
System.bool IGetFrameDiameterSymbols(
   System.short FrameNumber
)
```

### C++/CLI

```cpp
System.bool IGetFrameDiameterSymbols(
   System.short FrameNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`: Frame number to examine (1 or 2)

### Return Value

- in-process, unmanaged C++: Pointer to an array of Booleans (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value should be an array of two Booleans, with the following format:

`retval`[0] = True if the first tolerance value has a diameter symbol, false if it does not

`retval`[1] = True if the second tolerance value has a diameter symbol, false if it does not

Use this method in combination with [IGtol::GetFrameSymbols2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetFrameSymbols2.html) that is used to retrieve the frame symbols.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.html)
[IGtol::GetFrameCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.html)
[IGtol::GetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.html)
[IGtol::IGetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols2.html)
[IGtol::IGetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.html)
[IGtol::SetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.html)
[IGtol::SetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues.html)

## Availability

SOLIDWORKS 99, datecode 1999207
