---
title: "SetCompositeFrame2 Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetCompositeFrame2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetCompositeFrame2.html"
---

# SetCompositeFrame2 Method (IGtol)

Sets whether to create a composite frame containing the specified GTol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCompositeFrame2( _
   ByVal Composite As System.Boolean, _
   ByVal FrameNum As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Composite As System.Boolean
Dim FrameNum As System.Short

instance.SetCompositeFrame2(Composite, FrameNum)
```

### C#

```csharp
void SetCompositeFrame2(
   System.bool Composite,
   System.short FrameNum
)
```

### C++/CLI

```cpp
void SetCompositeFrame2(
   System.bool Composite,
   System.short FrameNum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Composite`: True to create a composite frame, false to not (see **Remarks**)
- `FrameNum`: Index of GTol frame

## VBA Syntax

See [Gtol::SetCompositeFrame2](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetCompositeFrame2.html).

## Examples

[Create GTol Composite Frame (VBA)](Create_Gtol_Composite_Frame_Example_VB.htm)
[Create GTol Composite Frame (VB.NET)](Create_Gtol_Composite_Frame_Example_VBNET.htm)
[Create GTol Composite Frame (C#)](Create_Gtol_Composite_Frame_Example_CSharp.htm)

## Remarks

If Composite is true, this method creates a composite frame containing adjacent GTol frames:

- Frame with index FrameNum.
- Frame directly below.

Both GTol frames must have the same symbol.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetCompositeFrame2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetCompositeFrame2.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
