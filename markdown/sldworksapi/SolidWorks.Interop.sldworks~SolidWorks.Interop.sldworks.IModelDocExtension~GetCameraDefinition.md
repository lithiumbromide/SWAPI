---
title: "GetCameraDefinition Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCameraDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraDefinition.html"
---

# GetCameraDefinition Method (IModelDocExtension)

Gets a camera, but does not add the newly created camera to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCameraDefinition() As Camera
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As Camera

value = instance.GetCameraDefinition()
```

### C#

```csharp
Camera GetCameraDefinition()
```

### C++/CLI

```cpp
Camera^ GetCameraDefinition();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDocExtension::GetCameraDefinition](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetCameraDefinition.html).

## Remarks

The model is unchanged.

You should find this method helpful when developing a renderer add-in.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::InsertCamera Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertCamera.html)
[IModelDocExtension::GetCameraById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraById.html)
[IModelDocExtension::GetCameraCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraCount.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
