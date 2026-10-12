---
title: "CreateFormTool2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CreateFormTool2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFormTool2.html"
---

# CreateFormTool2 Method (IFeatureManager)

Creates a forming tool feature with the specified point of insertion in a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFormTool2( _
   ByVal OriginX As System.Double, _
   ByVal OriginY As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim OriginX As System.Double
Dim OriginY As System.Double
Dim value As Feature

value = instance.CreateFormTool2(OriginX, OriginY)
```

### C#

```csharp
Feature CreateFormTool2(
   System.double OriginX,
   System.double OriginY
)
```

### C++/CLI

```cpp
Feature^ CreateFormTool2(
   System.double OriginX,
   System.double OriginY
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OriginX`: x coordinate of insertion point
- `OriginY`: y coordinate of insertion point

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::CreateFormTool2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CreateFormTool2.html).

## Examples

[Create Forming Tool (VBA)](Create_Forming_Tool_Example_VB.htm)
[Create Forming Tool (VB.NET)](Create_Forming_Tool_Example_VBNET.htm)
[Create Forming Tool (C#)](Create_Forming_Tool_Example_CSharp.htm)

## Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html):

1. with Append = True and Mark = 1 to select the stopping face.
2. (optional) one or more times with Append = True and Mark = 2 to select the faces to remove.

To insert a forming tool from the Design Library, call [IFeatureManager::InsertFormToolFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFormToolFeature.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
