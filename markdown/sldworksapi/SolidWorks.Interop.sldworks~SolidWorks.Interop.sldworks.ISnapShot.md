---
title: "ISnapShot Interface"
project: "SOLIDWORKS API Help"
interface: "ISnapShot"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot.html"
---

# ISnapShot Interface

Allows access to the snapshot of the graphics area of an assembly opened in Large Design Review mode.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISnapShot
```

### Visual Basic (Usage)

```vb
Dim instance As ISnapShot
```

### C#

```csharp
public interface ISnapShot
```

### C++/CLI

```cpp
public interface class ISnapShot
```

## VBA Syntax

See [SnapShot](ms-its:sldworksapivb6.chm::/sldworks~SnapShot.html).

## Examples

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

## Remarks

To open an assembly in Large Design Review mode:

1. Call [ISldWorks::GetOpenDocSpec](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetOpenDocSpec.html) to create an instance of [IDocumentSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification.html).
2. Set [IDocumentSpecification::ViewOnly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~ViewOnly.html) to true.
3. Call [ISldWorks::OpenDoc7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html), passing it the instance of IDocumentSpecification.

- or -

Call [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) with the Options parameter set to swOpenDocOptions_e.swOpenDocOptions_ViewOnly.

## Accessors

[IModelViewManager::AddSnapShot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~AddSnapShot.html)

[IModelViewManager::GetSnapShot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~GetSnapShot.html)

[IModelViewManager::GetSnapShots](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~GetSnapShots.html)

## Access Diagram

[SnapShot](SWObjectModel.pdf#SnapShot)

## See Also

[ISnapShot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
