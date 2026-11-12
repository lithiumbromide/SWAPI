---
title: "AspectRatio Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "AspectRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~AspectRatio.html"
---

# AspectRatio Property (ICamera)

Gets the aspect ratio (width/height) of the field of view rectangle for the camera.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property AspectRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Double

instance.AspectRatio = value

value = instance.AspectRatio
```

### C#

```csharp
System.double AspectRatio {get; set;}
```

### C++/CLI

```cpp
property System.double AspectRatio {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Width/height ratio of the view rectangle for the camera

## VBA Syntax

See [Camera::AspectRatio](ms-its:sldworksapivb6.chm::/sldworks~Camera~AspectRatio.html).

## Remarks

The rectangle is best-fit into a rendering window to determine the actual composition.

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
