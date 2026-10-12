---
title: "DeleteFrame Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "DeleteFrame"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~DeleteFrame.html"
---

# DeleteFrame Method (IGtol)

Deletes the specified frame from this Gtol.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteFrame( _
   ByVal FrameNum As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNum As System.Integer
Dim value As System.Boolean

value = instance.DeleteFrame(FrameNum)
```

### C#

```csharp
System.bool DeleteFrame(
   System.int FrameNum
)
```

### C++/CLI

```cpp
System.bool DeleteFrame(
   System.int FrameNum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNum`: One-based index of Gtol to delete

### Return Value

True if successfully deleted, false if not

## VBA Syntax

See [Gtol::DeleteFrame](ms-its:sldworksapivb6.chm::/sldworks~Gtol~DeleteFrame.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

This method is valid only if this Gtol was created in SOLIDWORKS 2022 or later.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
