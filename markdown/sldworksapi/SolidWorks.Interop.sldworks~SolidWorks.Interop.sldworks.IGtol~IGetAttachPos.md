---
title: "IGetAttachPos Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetAttachPos"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetAttachPos.html"
---

# IGetAttachPos Method (IGtol)

Gets the attachment point of the GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAttachPos() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Double

value = instance.IGetAttachPos()
```

### C#

```csharp
System.double IGetAttachPos()
```

### C++/CLI

```cpp
System.double IGetAttachPos();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method is meaningful only if this GTol is attached.

Format of return value is the following array of doubles:

`retval`[0] = X-coordinate of attachment point

`retval`[1] = Y-coordinate of attachment point

`retval`[2] = Z-coordinate of attachment point

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAttachPos.html)
