---
title: "InsertCamera Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertCamera"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertCamera.html"
---

# InsertCamera Method (IModelDocExtension)

Inserts a camera in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCamera() As Camera
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As Camera

value = instance.InsertCamera()
```

### C#

```csharp
Camera InsertCamera()
```

### C++/CLI

```cpp
Camera^ InsertCamera();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Camera](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICamera.html)

## VBA Syntax

See [ModelDocExtension::InsertCamera](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertCamera.html).

## Examples

[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
