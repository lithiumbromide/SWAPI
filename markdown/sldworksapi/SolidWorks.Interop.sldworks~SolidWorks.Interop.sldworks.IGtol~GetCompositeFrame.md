---
title: "GetCompositeFrame Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetCompositeFrame"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetCompositeFrame.html"
---

# GetCompositeFrame Method (IGtol)

Obsolete. Superseded by [IGtol::GetCompositeFrame2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetCompositeFrame2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCompositeFrame() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Boolean

value = instance.GetCompositeFrame()
```

### C#

```csharp
System.bool GetCompositeFrame()
```

### C++/CLI

```cpp
System.bool GetCompositeFrame();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the first two frames of this Gtol are in a composite frame, false if not

## VBA Syntax

See [Gtol::GetCompositeFrame](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetCompositeFrame.html).

## Remarks

Gets whether the first two frames of this Gtol are in a composite frame. Use [IGtol::SetCompositeFrame](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~SetCompositeFrame.html) to set this value.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 998Plus, datecode 1998319
