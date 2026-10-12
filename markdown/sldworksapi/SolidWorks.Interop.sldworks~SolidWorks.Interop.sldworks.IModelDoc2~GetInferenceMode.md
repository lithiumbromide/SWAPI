---
title: "GetInferenceMode Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetInferenceMode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetInferenceMode.html"
---

# GetInferenceMode Method (IModelDoc2)

Obsolete. Superseded by [SketchManager::InferenceMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InferenceMode.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInferenceMode() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.GetInferenceMode()
```

### C#

```csharp
System.bool GetInferenceMode()
```

### C++/CLI

```cpp
System.bool GetInferenceMode();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::GetInferenceMode](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetInferenceMode.html).

## Remarks

This method affects sketch-entity snapping or inferring constraints to other geometry during creation.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AutoInferToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AutoInferToggle.html)
[IModelDoc2::SetInferenceMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetInferenceMode.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
