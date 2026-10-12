---
title: "GetFocalDistance Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "GetFocalDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetFocalDistance.html"
---

# GetFocalDistance Method (ICamera)

Gets the camera's focal distance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFocalDistance() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Double

value = instance.GetFocalDistance()
```

### C#

```csharp
System.double GetFocalDistance()
```

### C++/CLI

```cpp
System.double GetFocalDistance();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Camera's focal distance

## VBA Syntax

See [Camera::GetFocalDistance](ms-its:sldworksapivb6.chm::/sldworks~Camera~GetFocalDistance.html).

## Examples

[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

## Remarks

If the camera is locked to a reference, then the return value might be different than the numeric value shown in the Camera PropertyManager.

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
