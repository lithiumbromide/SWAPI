---
title: "GetCompositeFrame2 Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetCompositeFrame2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetCompositeFrame2.html"
---

# GetCompositeFrame2 Method (IGtol)

Gets whether the GTol frame with the specified index is part of a composite frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCompositeFrame2( _
   ByVal FrameNum As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNum As System.Short
Dim value As System.Boolean

value = instance.GetCompositeFrame2(FrameNum)
```

### C#

```csharp
System.bool GetCompositeFrame2(
   System.short FrameNum
)
```

### C++/CLI

```cpp
System.bool GetCompositeFrame2(
   System.short FrameNum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNum`: Index of GTol frame

### Return Value

True if GTol frame is part of a composite frame, false if not

## VBA Syntax

See [Gtol::GetCompositeFrame2](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetCompositeFrame2.html).

## Examples

[Create GTol Composite Frame (VBA)](Create_Gtol_Composite_Frame_Example_VB.htm)
[Create GTol Composite Frame (VB.NET)](Create_Gtol_Composite_Frame_Example_VBNET.htm)
[Create GTol Composite Frame (C#)](Create_Gtol_Composite_Frame_Example_CSharp.htm)

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::SetCompositeFrame2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetCompositeFrame2.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
