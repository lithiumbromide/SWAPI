---
title: "GetAttachPos Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetAttachPos"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAttachPos.html"
---

# GetAttachPos Method (IGtol)

Gets the attachment point of the GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachPos() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Object

value = instance.GetAttachPos()
```

### C#

```csharp
System.object GetAttachPos()
```

### C++/CLI

```cpp
System.Object^ GetAttachPos();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Gtol::GetAttachPos](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetAttachPos.html).

## Remarks

This method is meaningful only if this GTol is attached.

Format of return value is the following array of doubles:

`retval`[0] = X-coordinate of attachment point

`retval`[1] = Y-coordinate of attachment point

`retval`[2] = Z-coordinate of attachment point

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::IGetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetAttachPos.html)
