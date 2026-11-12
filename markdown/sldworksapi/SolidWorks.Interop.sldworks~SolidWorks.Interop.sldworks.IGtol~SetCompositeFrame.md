---
title: "SetCompositeFrame Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetCompositeFrame"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetCompositeFrame.html"
---

# SetCompositeFrame Method (IGtol)

Obsolete. Superseded by [IGtol::SetCompositeFrame2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetCompositeFrame2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCompositeFrame( _
   ByVal Composite As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Composite As System.Boolean

instance.SetCompositeFrame(Composite)
```

### C#

```csharp
void SetCompositeFrame(
   System.bool Composite
)
```

### C++/CLI

```cpp
void SetCompositeFrame(
   System.bool Composite
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Composite`: True to put the first two frames of this Gtol into a composite frame, false to not

## VBA Syntax

See [Gtol::SetCompositeFrame](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetCompositeFrame.html).

## Remarks

Sets whether to put the first two frames of this Gtol into a composite frame.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetCompositeFrame Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetCompositeFrame.html)

## Availability

SOLIDWORKS 998Plus, datecode 1998319
