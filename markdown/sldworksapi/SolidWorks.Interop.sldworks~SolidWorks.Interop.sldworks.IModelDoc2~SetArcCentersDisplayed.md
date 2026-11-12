---
title: "SetArcCentersDisplayed Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetArcCentersDisplayed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetArcCentersDisplayed.html"
---

# SetArcCentersDisplayed Method (IModelDoc2)

Sets the current arc centers displayed setting.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetArcCentersDisplayed( _
   ByVal Setting As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Setting As System.Boolean

instance.SetArcCentersDisplayed(Setting)
```

### C#

```csharp
void SetArcCentersDisplayed(
   System.bool Setting
)
```

### C++/CLI

```cpp
void SetArcCentersDisplayed(
   System.bool Setting
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Setting`: True to display arc centers, false to not

## VBA Syntax

See [ModelDoc2::SetArcCentersDisplayed](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetArcCentersDisplayed.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetArcCentersDisplayed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetArcCentersDisplayed.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
