---
title: "GetTranslateSurface Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "GetTranslateSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetTranslateSurface.html"
---

# GetTranslateSurface Method (ISurfExtrudeFeatureData)

Gets the translate surface setting for this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTranslateSurface( _
   ByVal Fwd As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Fwd As System.Boolean
Dim value As System.Boolean

value = instance.GetTranslateSurface(Fwd)
```

### C#

```csharp
System.bool GetTranslateSurface(
   System.bool Fwd
)
```

### C++/CLI

```cpp
System.bool GetTranslateSurface(
   System.bool Fwd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Fwd`: True gets the translate surface setting in the forward direction, false gets it in the reverse direction

### Return Value

True if the translate surface setting is enabled, false if it is disabled

## VBA Syntax

See [SurfExtrudeFeatureData::GetTranslateSurface](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~GetTranslateSurface.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfTranslateFeatureData::SetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetTranslateSurface.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
