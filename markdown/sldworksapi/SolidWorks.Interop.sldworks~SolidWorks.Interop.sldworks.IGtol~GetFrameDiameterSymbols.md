---
title: "GetFrameDiameterSymbols Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFrameDiameterSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.html"
---

# GetFrameDiameterSymbols Method (IGtol)

Gets whether diameter symbols are displayed for the specified frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrameDiameterSymbols( _
   ByVal FrameNumber As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Short
Dim value As System.Object

value = instance.GetFrameDiameterSymbols(FrameNumber)
```

### C#

```csharp
System.object GetFrameDiameterSymbols(
   System.short FrameNumber
)
```

### C++/CLI

```cpp
System.Object^ GetFrameDiameterSymbols(
   System.short FrameNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`: Frame number to examine (1 or 2)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Gtol::GetFrameDiameterSymbols](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFrameDiameterSymbols.html).

## Remarks

This method is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.

The return value should be an array of two Booleans, with the following format:

`retval`[0] = True if the first tolerance value has a diameter symbol, false if it does not

`retval`[1] = True if the second tolerance value has a diameter symbol, false if it does not

Use this method in combination with [IGtol::GetFrameSymbols2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetFrameSymbols2.html) that is used to retrieve the frame symbols.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetFrameCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.html)
[IGtol::GetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.html)
[IGtol::GetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.html)
[IGtol::IGetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols2.html)
[IGtol::IGetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.html)
[IGtol::SetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.html)
[IGtol::SetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues.html)

## Availability

SOLIDWORKS 99, datecode 1999207
