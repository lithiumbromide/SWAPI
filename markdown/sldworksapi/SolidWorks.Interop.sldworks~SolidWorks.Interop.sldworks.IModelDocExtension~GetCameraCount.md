---
title: "GetCameraCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCameraCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraCount.html"
---

# GetCameraCount Method (IModelDocExtension)

Gets the number of cameras in the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCameraCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.GetCameraCount()
```

### C#

```csharp
System.int GetCameraCount()
```

### C++/CLI

```cpp
System.int GetCameraCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of cameras in the document

## VBA Syntax

See [ModelDocExtension::GetCameraCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetCameraCount.html).

## Examples

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetCameraById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraById.html)
[IModelDocExtension::GetCameraDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraDefinition.html)
[IModelDocExtension::InsertCamera Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertCamera.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
