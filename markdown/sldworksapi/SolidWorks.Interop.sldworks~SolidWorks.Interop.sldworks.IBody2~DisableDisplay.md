---
title: "DisableDisplay Property (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DisableDisplay"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DisableDisplay.html"
---

# DisableDisplay Property (IBody2)

Gets or sets whether to hide or show this body.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisableDisplay As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

instance.DisableDisplay = value

value = instance.DisableDisplay
```

### C#

```csharp
System.bool DisableDisplay {get; set;}
```

### C++/CLI

```cpp
property System.bool DisableDisplay {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to hide the body; false to show the body

**NOTE:** If true, then the body is hidden but remains selectable.

## VBA Syntax

See [Body2::DisableDisplay](ms-its:sldworksapivb6.chm::/sldworks~Body2~DisableDisplay.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::HideBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HideBody.html)
[IModelDoc2::HideShowBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideShowBodies.html)
[IModelDoc2::HideSolidBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideSolidBody.html)
[IFeatureManager::ShowBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowBodies.html)
[IFeatureManager::HideBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HideBody.html)
