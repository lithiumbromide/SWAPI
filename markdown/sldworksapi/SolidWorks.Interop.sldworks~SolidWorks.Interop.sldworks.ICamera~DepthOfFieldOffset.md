---
title: "DepthOfFieldOffset Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "DepthOfFieldOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~DepthOfFieldOffset.html"
---

# DepthOfFieldOffset Property (ICamera)

Gets the approximate distance from the camera's focal plane to point where focus is lost.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DepthOfFieldOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Double

instance.DepthOfFieldOffset = value

value = instance.DepthOfFieldOffset
```

### C#

```csharp
System.double DepthOfFieldOffset {get; set;}
```

### C++/CLI

```cpp
property System.double DepthOfFieldOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Approximate distance from the camera's focal plane to the point where focus is lost

## VBA Syntax

See [Camera::DepthOfFieldOffset](ms-its:sldworksapivb6.chm::/sldworks~Camera~DepthOfFieldOffset.html).

## Examples

[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::DepthOfFieldEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~DepthOfFieldEnabled.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
