---
title: "GetViewVector Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "GetViewVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetViewVector.html"
---

# GetViewVector Method (ICamera)

Gets the direction in which the camera is looking.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViewVector() As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As MathVector

value = instance.GetViewVector()
```

### C#

```csharp
MathVector GetViewVector()
```

### C++/CLI

```cpp
MathVector^ GetViewVector();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to [IMathVector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object

## VBA Syntax

See [Camera::GetViewVector](ms-its:sldworksapivb6.chm::/sldworks~Camera~GetViewVector.html).

## Remarks

Most of the time, the return value is the vector from the camera position to the target, normalized.

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetUpVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetUpVector.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
