---
title: "HideBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "HideBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HideBody.html"
---

# HideBody Method (IBody2)

Hides or shows this body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub HideBody( _
   ByVal BHide As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim BHide As System.Boolean

instance.HideBody(BHide)
```

### C#

```csharp
void HideBody(
   System.bool BHide
)
```

### C++/CLI

```cpp
void HideBody(
   System.bool BHide
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BHide`: True to hide the body, false to show the body

## VBA Syntax

See [Body2::HideBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~HideBody.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IFeatureManager::ShowBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowBodies.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
