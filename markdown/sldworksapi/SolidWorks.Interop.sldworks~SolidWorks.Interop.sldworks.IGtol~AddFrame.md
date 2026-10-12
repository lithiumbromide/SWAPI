---
title: "AddFrame Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "AddFrame"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~AddFrame.html"
---

# AddFrame Method (IGtol)

Adds a frame at the end of the list of this Gtol's frames.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFrame() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Boolean

value = instance.AddFrame()
```

### C#

```csharp
System.bool AddFrame()
```

### C++/CLI

```cpp
System.bool AddFrame();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if frame successfully added, false if not

## VBA Syntax

See [Gtol::AddFrame](ms-its:sldworksapivb6.chm::/sldworks~Gtol~AddFrame.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

This method is valid only if this Gtol was created in SOLIDWORKS 2022 or later.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
