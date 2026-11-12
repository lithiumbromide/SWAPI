---
title: "MoveSizeFeatures Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "MoveSizeFeatures"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoveSizeFeatures.html"
---

# MoveSizeFeatures Property (IFeatureManager)

Shows or hides the feature Instant3D.

## Syntax

### Visual Basic (Declaration)

```vb
Property MoveSizeFeatures As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.MoveSizeFeatures = value

value = instance.MoveSizeFeatures
```

### C#

```csharp
System.bool MoveSizeFeatures {get; set;}
```

### C++/CLI

```cpp
property System.bool MoveSizeFeatures {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable Instant3D, false to not

## VBA Syntax

See [FeatureManager::MoveSizeFeatures](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~MoveSizeFeatures.html).

## Examples

```vb
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeatMgr As SldWorks.FeatureManager

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swFeatMgr = swModel.FeatureManager

Debug.Print "Is Instant3D enabled? " & swFeatMgr.MoveSizeFeatures
swFeatMgr.MoveSizeFeatures = False
Debug.Print "Is Instant3D enabled? " & swFeatMgr.MoveSizeFeatures
swFeatMgr.MoveSizeFeatures = True
Debug.Print "Is Instant3D enabled? " & swFeatMgr.MoveSizeFeatures

End Sub
```

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
