---
title: "AutoInferToggle Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AutoInferToggle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AutoInferToggle.html"
---

# AutoInferToggle Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::AutoInference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AutoInference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub AutoInferToggle()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.AutoInferToggle()
```

### C#

```csharp
void AutoInferToggle()
```

### C++/CLI

```cpp
void AutoInferToggle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::AutoInferToggle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AutoInferToggle.html).

## Remarks

Inferencing mode can be seen when creating a sketch segment and you mouse moves past another sketch item. If inferencing is turned on, you see a dashed line from the current cursor position to the inferenced position on the existing sketch entity.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetInferenceMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetInferenceMode.html)
[IModelDoc2::GetInferenceMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetInferenceMode.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
