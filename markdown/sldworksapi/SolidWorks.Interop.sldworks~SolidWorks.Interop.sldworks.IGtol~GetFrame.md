---
title: "GetFrame Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFrame"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrame.html"
---

# GetFrame Method (IGtol)

Gets the Gtol frame at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrame( _
   ByVal FrameIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameIndex As System.Integer
Dim value As System.Object

value = instance.GetFrame(FrameIndex)
```

### C#

```csharp
System.object GetFrame(
   System.int FrameIndex
)
```

### C++/CLI

```cpp
System.Object^ GetFrame(
   System.int FrameIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameIndex`: One-based index of Gtol frame to retrieve

### Return Value

[IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html)

## VBA Syntax

See [Gtol::GetFrame](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFrame.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

This method is valid only if this Gtol was created in SOLIDWORKS 2022 or later.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
