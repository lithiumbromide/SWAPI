---
title: "AutoInference Property (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "AutoInference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoInference.html"
---

# AutoInference Property (ISketchManager)

Obsolete. Superseded by [ISldWorks::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html) or [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) and [swUserPreferenceToggle_e.swSketchInference.](ms-its:swconst.chm::/SO_SketchRelationsSnaps.htm)

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoInference As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Boolean

instance.AutoInference = value

value = instance.AutoInference
```

### C#

```csharp
System.bool AutoInference {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoInference {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if automatic inteferencing is on, false if off

## VBA Syntax

See [SketchManager::AutoInference](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~AutoInference.html).

## Remarks

Inferencing mode can be seen when creating a sketch segment and your cursor moves past another sketch enitity. If inferencing is turned on, you see a dashed line from your current cursor position to the inferenced position on the existing sketch entity.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::InferenceMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InferenceMode.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
