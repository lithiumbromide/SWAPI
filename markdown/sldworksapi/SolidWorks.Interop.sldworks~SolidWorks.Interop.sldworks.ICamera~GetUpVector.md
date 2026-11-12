---
title: "GetUpVector Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "GetUpVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetUpVector.html"
---

# GetUpVector Method (ICamera)

Gets the camera's up direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUpVector() As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As MathVector

value = instance.GetUpVector()
```

### C#

```csharp
MathVector GetUpVector()
```

### C++/CLI

```cpp
MathVector^ GetUpVector();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Point to [IMathVector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object

## VBA Syntax

See [Camera::GetUpVector](ms-its:sldworksapivb6.chm::/sldworks~Camera~GetUpVector.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetViewVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetViewVector.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
