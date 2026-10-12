---
title: "SetInferenceMode Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetInferenceMode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetInferenceMode.html"
---

# SetInferenceMode Method (IModelDoc2)

Obsolete. Superseded by [SketchManager::InferenceMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InferenceMode.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetInferenceMode( _
   ByVal InferenceMode As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim InferenceMode As System.Boolean

instance.SetInferenceMode(InferenceMode)
```

### C#

```csharp
void SetInferenceMode(
   System.bool InferenceMode
)
```

### C++/CLI

```cpp
void SetInferenceMode(
   System.bool InferenceMode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InferenceMode`: True to enable sketch inference mode, false to disable it

## VBA Syntax

See [ModelDoc2::SetInferenceMode](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetInferenceMode.html).

## Remarks

| Setting inference mode to... | Allows... |
| --- | --- |
| True | Inferencing during sketch operations, subject to other settings that may disable inferencing such as IModelDoc2::AutoInferToggle , IModelDoc2::SetAddToDB , and IDrawingDoc::StartDrawing . |
| false | Faster sketching without inferencing, similar to IModelDoc2::SetAddToDB , except that using this method does not disable undo operations. |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetInferenceMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetInferenceMode.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
