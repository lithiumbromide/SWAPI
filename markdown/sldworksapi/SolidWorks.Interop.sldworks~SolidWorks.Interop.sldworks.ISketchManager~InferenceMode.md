---
title: "InferenceMode Property (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "InferenceMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InferenceMode.html"
---

# InferenceMode Property (ISketchManager)

Obsolete. Superseded by [ISldWorks::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html) or [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) and [swUserPreferenceToggle_e.swSketchInference.](ms-its:swconst.chm::/SO_SketchRelationsSnaps.htm)

## Syntax

### Visual Basic (Declaration)

```vb
Property InferenceMode As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Boolean

instance.InferenceMode = value

value = instance.InferenceMode
```

### C#

```csharp
System.bool InferenceMode {get; set;}
```

### C++/CLI

```cpp
property System.bool InferenceMode {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if sketch inference mode is on, false if off

## VBA Syntax

See [SketchManager::InferenceMode](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~InferenceMode.html).

## Remarks

This property affects sketch entity snapping and inferring constraints to other geometry during creation.

| Setting inference mode to... | Allows... |
| --- | --- |
| True | Inferencing during sketch operations, subject to other settings that may disable inferencing such as ISketchManager::AutoInference , ISketchManager::AddToDB , and IDrawingDoc::StartDrawing . |
| False | Faster sketching without inferencing, similar to SketchManager::AddToDB, except that using this method does not disable undo operations. |

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
