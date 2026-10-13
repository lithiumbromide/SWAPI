---
title: "DepthOfFieldEnabled Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "DepthOfFieldEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~DepthOfFieldEnabled.html"
---

# DepthOfFieldEnabled Property (ICamera)

Gets whether depth of field effects are enabled or disabled.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DepthOfFieldEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Boolean

instance.DepthOfFieldEnabled = value

value = instance.DepthOfFieldEnabled
```

### C#

```csharp
System.bool DepthOfFieldEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool DepthOfFieldEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if depth of field effects are enabled, false if they are disabled

## VBA Syntax

See [Camera::DepthOfFieldEnabled](ms-its:sldworksapivb6.chm::/sldworks~Camera~DepthOfFieldEnabled.html).

## Examples

[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::DepthOfFieldOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~DepthOfFieldOffset.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
